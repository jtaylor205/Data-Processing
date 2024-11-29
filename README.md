# In-Memory Key-Value Database

This project implements an in-memory key-value database with transaction support. The database provides the ability to perform atomic operations (all-or-nothing updates) within transactions, ensuring consistency and correctness for operations like `put`, `get`, `commit`, and `rollback`.

## Features

- **Key-Value Store**: Keys must be strings. Values must be integers. Provides basic operations such as adding, updating, and retrieving key-value pairs.
- **Transaction Support**: Allows changes to be isolated within a transaction and applied only after a commit. Rollback functionality to discard changes made during a transaction.
- **Error Handling**: Validates that keys are strings and values are integers. Raises appropriate exceptions when methods are misused (e.g., `put` called without an active transaction).

## Setup and Test Instructions

1. **Clone the Repository**: `git clone https://github.com/jtaylor205/Data-Processing.git` `cd Data-processing`
2. **Ensure Python is Installed**: The implementation and tests require Python.
3. **Run the Implementation**: Save the implementation in `InMemoryDB.py`. Use the `InMemoryDB` class in your own scripts or in an interactive Python shell.
4. **Run the Tests**: The test cases are located in `test_memoryDB.py`. Execute the tests using: `python test_memoryDB.py`.

If a grader wants to implement their own test cases, alter the `test_memoryDB.py` file and run `python test_memoryDB.py` again.

## Improvement Suggestions for Official Assignment

1. **Expand Functional Requirements**:
   - Add support for nested or concurrent transactions to simulate real-world scenarios where multiple transactions may occur simultaneously.
   - Include batch operations like `put_many(keys, values)` or `get_many(keys)` to handle multiple key-value pairs at once, enhancing usability for larger datasets.

2. **Clarify Instructions**:
   - Clearly define the behavior of edge cases, such as operations on empty keys, null values, or attempting to commit or roll back without an active transaction.
   - Include detailed explanations about expected error handling, such as the specific exception types to be raised for invalid inputs or unsupported operations.

3. **Provide Starter Code**:
   - Include basic starter code for the database interface and transaction logic to ensure all students begin with a consistent framework.
   - This can reduce ambiguity and allow graders to focus on the quality of the implementation rather than debugging structural issues.
