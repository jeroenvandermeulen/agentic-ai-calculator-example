# TDD Calculator Application

A simple GUI calculator built using Python, Test-Driven Development (TDD), and Tkinter.

## Prompt Used

```markdown
Here is a prompt for an agentic AI to create a simple GUI calculator using Python and TDD:

"You are an autonomous Python TDD agent. Your goal is to create a simple GUI calculator application using Python.

You have a live shell. You must use pytest for all testing and Tkinter for the GUI.

Your core development must strictly separate the calculation logic from the GUI code. The TDD process will focus on the non-GUI calculation engine first.

Your core algorithm is a mandatory Red-Green-Refactor loop. You must build the calculator's logic iteratively, one feature at a time.

Red Step: First, add one new, small, failing test to your pytest test file (e.g., tests/test_calculator.py). Run pytest and confirm that this new test fails as expected.

Green Step: Next, write the minimum possible code in your logic module (e.g., src/calculator.py) required to make the new test pass, while ensuring all old tests still pass. Run pytest and confirm all tests are 'Green'.

Refactor Step: Finally, improve the code you just wrote for clarity, performance, or structure, without adding new functionality. After refactoring, you must run pytest one more time to guarantee your changes are safe.

Your overall plan is as follows:

Set up a clean project structure with a src directory for your application code and a tests directory for your tests.

Begin the TDD loop for the calculator logic module.

Start with the first feature, such as 'addition of two numbers'.

Iteratively repeat the TDD loop to add more features: subtraction, multiplication, division, and basic error handling (like division by zero).

Only after the calculation logic is fully TDD-developed and tested, you will create the Tkinter GUI (e.g., in src/main.py). This GUI will import and use your fully-tested logic module to perform its operations.

Report your actions, test outputs, and decisions at each step of the Red-Green-Refactor process.

Begin."
```

## Project Structure

```
tdd-example/
├── src/
│   ├── __init__.py
│   ├── calculator.py      # Core calculation logic (TDD-developed)
│   └── main.py            # Tkinter GUI application
└── tests/
    ├── __init__.py
    └── test_calculator.py # Pytest test suite
```

## Features

The calculator supports:
- ✅ Addition
- ✅ Subtraction
- ✅ Multiplication
- ✅ Division (with error handling for division by zero)

## Development Process

This project was built following strict **Red-Green-Refactor** TDD methodology:

### TDD Cycle Applied

1. **RED**: Write a failing test first
2. **GREEN**: Write minimal code to make the test pass
3. **REFACTOR**: Improve code while keeping tests green

### Features Developed (in order)

1. Addition of positive numbers
2. Addition with negative numbers and zero
3. Subtraction
4. Multiplication
5. Division
6. Division by zero error handling

Each feature was fully tested before moving to the next one.

## Running Tests

```bash
# Run all tests
pytest -v

# Run tests with coverage
pytest --cov=src --cov-report=term-missing
```

## Running the Application

```bash
# From the project root directory
python src/main.py

# OR navigate to src first
cd src
python main.py
```

## Testing Results

All 7 tests pass:
- ✓ test_add_two_positive_numbers
- ✓ test_add_negative_numbers
- ✓ test_add_with_zero
- ✓ test_subtract_two_numbers
- ✓ test_multiply_two_numbers
- ✓ test_divide_two_numbers
- ✓ test_divide_by_zero_raises_error

## Design Principles

- **Separation of Concerns**: Calculator logic is completely separate from GUI
- **Test-First Development**: All logic was written test-first
- **Clean Code**: Simple, readable, maintainable code
- **Error Handling**: Proper handling of edge cases (division by zero)

## Requirements

- Python 3.x
- pytest (for testing)
- tkinter (usually included with Python)

## Install Dependencies

```bash
# Install pytest
pip install pytest

# Install tkinter (Linux only)
# On Fedora/RHEL/CentOS:
sudo dnf install python3-tkinter

# On Ubuntu/Debian:
sudo apt-get install python3-tk

# On Arch Linux:
sudo pacman -S tk
```

Note: Tkinter comes pre-installed with Python on Windows and macOS. On Linux, it typically needs to be installed separately as shown above.
# agentic-ai-calculator-example
