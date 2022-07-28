# See LICENSE.vyoma for details

TOPLEVEL_LANG ?= verilog

PWD=$(shell pwd)

VERILOG_SOURCES = $(PWD)/src/*.v

TOPLEVEL := timer
MODULE   := tb.tests.run_test_reset,tb.tests.run_test_rst_capture

PYTHONPATH = $PYTHONPATH:$PWD

include $(shell cocotb-config --makefiles)/Makefile.sim

clean_all: clean
	rm -rf *.xml sim_build __pycache__
