all:
	@ echo Choose a target command!
	
install:
	@ pip install -r doc/requirements.txt

run:
	@ python3 main.py
