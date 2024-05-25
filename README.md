# Snake and Ladders Game


Welcome to the Snake and Ladders game!

## Getting Started
To play the Snake and Ladders game, follow these steps:

1. Make sure you have Python installed on your computer.

2. Clone or download the repository to your local machine.

3. Open a terminal or command prompt and navigate to the directory where the game files are located.

4. Run the following command to start the game:
```bash
make run
```

## Running with Predefined Commands
You can also run the game with a predefined commands file. This is useful if you want to automate gameplay or test specific scenarios. Follow these steps:

1. Create a commands.txt file with your desired game settings and player inputs (A sample is attached in the repo). The format should match the example provided.

2. Run the following command to start the game with the predefined commands:

```bash
make run_commands
```
This command will execute the run_commands.py file and run the game using the commands specified in the commands.txt file.


## Unit Testing
Unit tests are available to ensure the correctness of the game logic. To run the unit tests, follow these steps:

1. Ensure you have the unittest module installed in your Python environment.
2. Run the following command to execute the unit tests:


```bash
make unit_test
```
This command will run all unit tests and display the results in the terminal.

### Note
- The output from the game will be stored in the output.txt file.
- Feel free to modify the commands.txt file to create your own custom game scenarios.
- Enjoy playing Snake and Ladders!
