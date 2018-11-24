import cocotb
from cocotb.clock import Clock
from cocotb.triggers import Timer, RisingEdge, FallingEdge, Edge, Event
from cocotb.result import TestFailure, TestError, ReturnValue, SimFailure
from cocotb.binary import BinaryValue
from random import randint


CLK_PERIOD = 10

@cocotb.coroutine
def Reset(dut):
    dut.A_i     <= 0
    dut.B_i     <= 0
    dut.C_i     <= 0
    dut.Reg_W_i <= 0
    dut.CLK_i   <= 0
    dut.W_c_i   <= 0
    dut.RST_i   <= 0
    yield Timer(CLK_PERIOD * 1.2)
    dut.RST_i <=  1
    yield Timer(CLK_PERIOD * 1.2)
    dut.RST_i  <= 0


@cocotb.test()
def test(dut):
    """
    Description:
        Test del Banco de Registros
    """
    cocotb.fork(Clock(dut.CLK_i, CLK_PERIOD).start())

    yield Reset(dut)

    dut._log.info('Lleno el Banco de Registros con 32 valores aleatorios.')
    listOfNumbers = [0]
    for x in range (0, 32):
        listOfNumbers.append(randint(0, 2**64-1))

    dut.Reg_W_i <= 1
    
    for i in range(0,32):
        dut.C_i <= i
        dut.W_c_i <= listOfNumbers[i]
        yield RisingEdge(dut.CLK_i)

    dut.Reg_W_i <= 0
    dut.C_i <= 0 

    yield RisingEdge(dut.CLK_i)

    for i in range(0,32):
        dut.A_i <= i
        print(listOfNumbers[i])
        yield RisingEdge(dut.CLK_i)
        print(dut.R_a_o.value.integer)
        if(listOfNumbers[i] != dut.R_a_o.value.integer):
            raise TestFailure("Error! No se logro leer adecuandamente la salida del Registro A")
                    

    yield RisingEdge(dut.CLK_i)

    for i in range(0,32):
        dut.B_i <= i
        print(listOfNumbers[i])
        yield RisingEdge(dut.CLK_i)
        print(dut.R_b_o.value.integer)
        if(listOfNumbers[i] != dut.R_b_o.value.integer):
            raise TestFailure("Error! No se logro leer adecuandamente la salida del Registro B")

    dut.A_i <= 2
    dut.B_i <= 3

    yield RisingEdge(dut.CLK_i)
    yield RisingEdge(dut.CLK_i)