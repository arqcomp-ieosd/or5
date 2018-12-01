PWD=$(shell pwd)

WPWD=$(shell pwd)
PYTHONPATH := $(WPWD)/../model:$(WPWD)/../utils:$(PYTHONPATH)

SIM_ARGS = --wave=axi_reg_tb.ghw --ieee-asserts=disable-at-0 

VHDL_SRCS = ALU.vhd

VHDL_FILES := $(addprefix $(WPWD)/../../src/,$(VHDL_SRCS))

TOPLEVEL_LANG ?= vhdl

VHDL_SOURCES = $(VHDL_FILES)
SIM=ghdl

TOPLEVEL := alu
MODULE   := ALU_tb

include $(COCOTB)/makefiles/Makefile.inc
include $(COCOTB)/makefiles/Makefile.sim
