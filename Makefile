.PHONY: run run_commands unit_test

run: 
	python main.py

run_commands:
	python run_commands.py

unit_test:
	python -m unittest