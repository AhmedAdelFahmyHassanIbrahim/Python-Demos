class Loggable:
    def __init__(self):
        self.title = ''
    def log(self):
        print(f"Log message from {self.title}")
    
class Connection:
    def __init__(self):
        self.server = ''
    def connect(self):
        print(f"Connecting to the database {self.connect}")

#This is the framework
def framework(item):
    if isinstance(item, Connection):
        item.connect()
    if isinstance(item , Loggable):
        item.log()


# Using the framework
# Inherit from Connection adn Loggable
class SqlDatabase(Connection, Loggable):
    def __init__(self):
        self.title = "Sql Connection Demo"
        self.server = "Some_server"

#sql_database = SqlDatabase()

class JustLog(Loggable):
    def __init__(self):
        self.title = "Just Logging"

justlog = JustLog()
framework(justlog)

