# Replit 100 Days of Python Challenge - Lessons Split

This repository contains all 100 lessons from the Replit 100 Days of Python Challenge, each split into its own Python file for easy testing and exploration.

## Structure
- All lessons are located in the `lessons/` directory as `lessonXX.py` (e.g., `lesson01.py`, `lesson02.py`, ...).
- Each lesson is refactored to be testable and runnable as a standalone script or function.
- Lessons that require user input now use function parameters or mocks for testability.
- Lessons that require external APIs, credentials, or complex integrations are stubbed with clear placeholder functions.

## How to Run a Lesson
To run a specific lesson, execute the corresponding file. For example:

```bash
python lessons/lesson01.py
```

Many lessons include an `if __name__ == "__main__":` block with example usage.

## Unit Tests
A comprehensive test suite is provided in `test_lessons.py` to validate the output of each lesson.

### To run all tests:

```bash
python -m unittest test_lessons.py
```

This will run the tests for all lessons that have been implemented and refactored for testability.

## Notes
- Lessons that require API keys, credentials, or external services are stubbed and will not perform real network operations.
- GUI and HTML/CSS lessons are skipped or stubbed, as they are not Python code.
- You can use the lesson files as a reference or as a starting point for your own projects.

---

**Enjoy exploring and testing the 100 Days of Python lessons!** 