import unittest
from InMemoryDB import InMemoryDB  # Import the InMemoryDB implementation

class TestInMemoryDB(unittest.TestCase):
    def setUp(self):
        # This method is called before every test. It creates a fresh instance of the database for each test.
        self.db = InMemoryDB()

    def test_get_nonexistent_key(self):
        # Test that getting a non-existent key returns None.
        # "A" does not exist in the database yet.
        self.assertIsNone(self.db.get("A"))

    def test_put_without_transaction(self):
        # Test that trying to put a key-value pair without an active transaction raises an exception.
        # No transaction started, should raise an exception.
        with self.assertRaises(Exception):
            self.db.put("A", 5)

    def test_begin_transaction(self):
        # Test that a transaction can be started, values can be added, and changes are visible only after commit.
        self.db.begin_transaction()  # Start a transaction.
        self.db.put("A", 5)  # Add a key-value pair within the transaction.
        # Value should not be visible until committed.
        self.assertIsNone(self.db.get("A"))
        self.db.commit()  # Commit the transaction.
        # Now the value should be visible in the main database.
        self.assertEqual(self.db.get("A"), 5)

    def test_commit(self):
        # Test that committing a transaction applies changes to the main database.
        self.db.begin_transaction()  # Start a transaction.
        self.db.put("B", 10)  # Add a key-value pair.
        self.db.commit()  # Commit the transaction.
        # Value should now be visible in the main database.
        self.assertEqual(self.db.get("B"), 10)

    def test_rollback(self):
        # Test that rolling back a transaction discards all changes made during the transaction.
        self.db.begin_transaction()  # Start a transaction.
        self.db.put("C", 15)  # Add a key-value pair.
        self.db.rollback()  # Rollback the transaction.
        # Value should not exist since the transaction was rolled back.
        self.assertIsNone(self.db.get("C"))

    def test_invalid_key_type(self):
        # Test that providing a non-string key raises a TypeError.
        self.db.begin_transaction()  # Start a transaction.
        # Key is an integer, should raise a TypeError.
        with self.assertRaises(TypeError):
            self.db.put(123, 5)

    def test_invalid_value_type(self):
        # Test that providing a non-integer value raises a TypeError.
        self.db.begin_transaction()  # Start a transaction.
        # Value is a string, should raise a TypeError.
        with self.assertRaises(TypeError):
            self.db.put("A", "invalid")

    def test_double_transaction(self):
        # Test that starting a transaction while another transaction is already active raises an exception.
        self.db.begin_transaction()  # Start the first transaction.
        # Attempt to start another transaction, should raise an exception.
        with self.assertRaises(Exception):
            self.db.begin_transaction()

if __name__ == "__main__":
    # Run all the tests
    unittest.main()
