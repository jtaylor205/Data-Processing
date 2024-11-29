class InMemoryDB:
    def __init__(self):
        # Main database to store committed data
        self.main_db = {}
        # Transaction log to store temporary changes during a transaction
        self.transaction_log = {}
        # Flag to track if a transaction is currently active
        self.in_transaction = False

    def begin_transaction(self):
        """
        Starts a new transaction. Only one transaction can exist at a time.
        """
        if self.in_transaction:
            raise Exception("A transaction is already in progress.")
        self.in_transaction = True
        self.transaction_log = {}  # Initialize a new transaction log

    def put(self, key, value):
        """
        Adds or updates a key-value pair in the transaction log.
        Raises an exception if no transaction is in progress.
        """
        if not isinstance(key, str):
            raise TypeError("Key must be a string.")
        if not isinstance(value, int):
            raise TypeError("Value must be an integer.")
        if not self.in_transaction:
            raise Exception("No transaction in progress. Use begin_transaction() first.")
        # Store changes in the transaction log
        self.transaction_log[key] = value

    def get(self, key):
        """
        Returns the value associated with the key.
        Returns None if the key doesn't exist or if its changes are uncommitted.
        """
        if not isinstance(key, str):
            raise TypeError("Key must be a string.")
        # If in a transaction and the key exists in the transaction log, return None
        if self.in_transaction and key in self.transaction_log:
            return None
        # Otherwise, return the value from the main database
        return self.main_db.get(key)

    def commit(self):
        """
        Applies all changes in the transaction log to the main database
        and ends the transaction.
        """
        if not self.in_transaction:
            raise Exception("No transaction in progress to commit.")
        # Apply changes from transaction log to the main database
        for key, value in self.transaction_log.items():
            self.main_db[key] = value
        # Clear transaction log and end the transaction
        self.transaction_log = {}
        self.in_transaction = False

    def rollback(self):
        """
        Discards all changes in the transaction log and ends the transaction.
        """
        if not self.in_transaction:
            raise Exception("No transaction in progress to rollback.")
        # Discard transaction log and end the transaction
        self.transaction_log = {}
        self.in_transaction = False
