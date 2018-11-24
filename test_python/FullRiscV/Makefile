PWD=$(shell pwd)

WPWD=$(shell pwd)
PYTHONPATH := $(WPWD)/../model:$(WPWD)/../utils:$(PYTHONPATH)

SIM_ARGS = --wave=axi_reg_tb.ghw --ieee-asserts=disable-at-0 

VHDL_SRCS = ALU.vhd   \
            DataMem.vhd   \
            ImmGen.vhd   \
            PC.vhd   \
            ProgMem.vhd   \
            RegBank.vhd   \
            UC.vhd   \
            or5_up.vhd 

VHDL_FILES := $(addprefix $(WPWD)/../src/,$(VHDL_SRCS))


TOPLEVEL_LANG ?= vhdl

ifeq ($(TOPLEVEL_LANG),verilog)
    VERILOG_SOURCES = $(VERILOG_FILES)
    SIM=icarus
else ifeq ($(TOPLEVEL_LANG),vhdl)
    VHDL_SOURCES = $(VHDL_FILES)
    SIM=ghdl
else
    $(error "A valid value (verilog or vhdl) was not provided for TOPLEVEL_LANG=$(TOPLEVEL_LANG)")
endif

TOPLEVEL := or5_up
MODULE   := risc-v

include $(COCOTB)/makefiles/Makefile.inc
include $(COCOTB)/makefiles/Makefile.sim
