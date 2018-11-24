import cocotb
from cocotb.clock import Clock
from cocotb.triggers import Timer, RisingEdge, FallingEdge, Edge, Event
from cocotb.result import TestFailure, TestError, ReturnValue, SimFailure
from cocotb.binary import BinaryValue

CLK_PERIOD = 10

@cocotb.coroutine
def Reset(dut):
    dut.RST_i  <= 0
    yield Timer(CLK_PERIOD * 1.2)
    dut.RST_i <=  1
    yield Timer(CLK_PERIOD * 1.2)
    dut.RST_i  <= 0

@cocotb.test()
def test(dut):
    """
    Description:
        Test del Program Counter
    """
    cocotb.fork(Clock(dut.CLK_i, CLK_PERIOD).start())

    dut.EN_i <= 0
    dut.DATA_i <= 0


    yield Reset(dut)

    yield RisingEdge(dut.CLK_i)

    dut.EN_i <= 1
    dut.DATA_i <= 25
    yield RisingEdge(dut.CLK_i)

    dut.DATA_i <= 16
    yield RisingEdge(dut.CLK_i)

    dut.EN_i <= 0
    yield RisingEdge(dut.CLK_i)

    dut.DATA_i <= 40
    yield RisingEdge(dut.CLK_i)

    dut.DATA_i <= 11
    yield RisingEdge(dut.CLK_i)

    dut.EN_i <= 1
    yield RisingEdge(dut.CLK_i)

    dut.DATA_i <= 41
    yield RisingEdge(dut.CLK_i)

    dut.DATA_i <= 12
    yield RisingEdge(dut.CLK_i)
    yield RisingEdge(dut.CLK_i)

    raise TestFailure(
        "Error vieja!")