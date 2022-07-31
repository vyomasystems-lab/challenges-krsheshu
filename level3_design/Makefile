# See LICENSE.vyoma for details

TOPLEVEL_LANG ?= verilog

PWD=$(shell pwd)

VERILOG_SOURCES = $(PWD)/src/*.v

TOPLEVEL := timer
MODULE   := tb.tests.run_test_reset,tb.tests.run_test_rst_capture,tb.tests.run_test_captured_out

PYTHONPATH = $PYTHONPATH:$PWD

include $(shell cocotb-config --makefiles)/Makefile.sim

view_wave:
	gtkwave waves/${TOPLEVEL}.vcd -a waves/${TOPLEVEL}.gtkw

clean_all: clean
	rm -rf *.xml sim_build __pycache__
