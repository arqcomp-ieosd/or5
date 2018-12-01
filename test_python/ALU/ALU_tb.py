import cocotb
from cocotb.clock import Clock
from cocotb.triggers import Timer, RisingEdge, FallingEdge, Edge, Event
from cocotb.result import TestFailure, TestError, ReturnValue, SimFailure
from cocotb.binary import BinaryValue
from random import randint


PERIOD = 10


OPERATIONS = {
    'AND_IN':  0,
    'OR_IN':  1,
    'ADD':  2,
    'XOR_IN':  5,
    'SUB':  6,
    'SLL_IN':  8,
    'SRL_IN':  9,
    'SLA_IN': 10,
    'SRA_IN': 11,
}


def operation_expected_result(val_a, val_b, operation):
    if operation == 'SRL_IN':
        return (val_a % 0x10000000000000000) >> val_b
    elif operation == 'SRA_IN':
        return (val_a >> val_b)
    elif operation == 'SLL_IN':
        return ((val_a << val_b) & 0xFFFFFFFFFFFFFFFF)
    elif operation == 'SLA_IN':
        return ((val_a << val_b) & 0xFFFFFFFFFFFFFFFF)
    elif operation == 'ADD':
        return (val_a + val_b)
    elif operation == 'SUB':
        return (val_a - val_b)
    elif operation == 'AND_IN':
        return (val_a & val_b)
    elif operation == 'OR_IN':
        return (val_a | val_b)
    elif operation == 'XOR_IN':
        return (val_a ^ val_b)
    else:
        return 0


@cocotb.coroutine
def InitSignals(dut):
    dut.A_i <= 0
    dut.B_i <= 0
    dut.ALUop_i <= 0xFF
    yield Timer(PERIOD)


@cocotb.coroutine
def OperationTest(dut, operation):

    yield InitSignals(dut)

    dut.ALUop_i <= OPERATIONS[operation]

    for i in range(0, 10):
        i_rand = randint(0, 2**63 - 1)
        for j in range(0, 10):
            if 'S' in operation:
                j_rand = randint(0, 64)
            else:
                j_rand = randint(0, 2**63 - 1)
            dut.A_i <= i_rand
            dut.B_i <= j_rand
            yield Timer(PERIOD)

            if (operation_expected_result(i_rand, j_rand, operation) != dut.OUTPUT_o):
                raise TestFailure(
                    "Error in result of %s operation!" % operation)


@cocotb.test()
def test_add(dut):
    """
    Description:
        ALU ADD Test
    """

    yield OperationTest(dut, 'ADD')


@cocotb.test()
def test_and(dut):
    """
    Description:
        ALU AND Test
    """

    yield OperationTest(dut, 'OR_IN')


@cocotb.test()
def test_or(dut):
    """
    Description:
        ALU OR Test
    """

    yield OperationTest(dut, 'OR_IN')


@cocotb.test()
def test_xor(dut):
    """
    Description:
        ALU XOR Test
    """

    yield OperationTest(dut, 'XOR_IN')


@cocotb.test()
def test_srl(dut):
    """
    Description:
        ALU SRL Test
    """

    yield OperationTest(dut, 'SRL_IN')


@cocotb.test()
def test_sra(dut):
    """
    Description:
        ALU SRA Test
    """

    yield OperationTest(dut, 'SRA_IN')


@cocotb.test()
def test_sll(dut):
    """
    Description:
        ALU SLL Test
    """

    yield OperationTest(dut, 'SLL_IN')


@cocotb.test()
def test_sla(dut):
    """
    Description:
        ALU SLA Test
    """

    yield OperationTest(dut, 'SLA_IN')
