import _sqlite3

class DatabaseConnection:
    def __init__(self, host):
        self.connection = None
        self.host = host

    def __enter__(self):
        self.connection = _sqlite3.connect('data.db')
        return self.connection

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_tb or exc_val or exc_type:
            self.connection.close()
        self.connection.commit()
        self.connection.close()
