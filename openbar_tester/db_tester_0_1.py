import openbar.db

class Connected(openbar.db.Connected):
    def test(self):
        with self as cursor:
            cursor.execute("SELECT 42")

def connector(name):
    return openbar.db.connector(name, Connected)
