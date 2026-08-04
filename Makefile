PYTHON := python

prepare:
	cd python && $(PYTHON) convert_mpc.py

debias:
	cd cpp && make clean && make all && nohup ./daboss > log.txt &

classify:
	cd python && $(PYTHON) classify.py

masses:
	cd python && $(PYTHON) masses.py

.PHONY: prepare debias classify masses