import cocotb
from cocotb.clock import Clock
from cocotb.triggers import Timer, RisingEdge, FallingEdge, Edge, Event
from cocotb.result import TestFailure, TestError, ReturnValue, SimFailure
from cocotb.binary import BinaryValue

CLK_PERIOD = 10

@cocotb.coroutine
def Reset(dut):
    dut.RST_i <=  0
    yield Timer(CLK_PERIOD * 10)
    dut.RST_i  <= 1

@cocotb.test()
def test(dut):
    """
    Description:
        Test RISC-V Simple Implementation
    """
    cocotb.fork(Clock(dut.CLK_i, CLK_PERIOD).start())
    yield Reset(dut)

    yield Timer(CLK_PERIOD * 5)