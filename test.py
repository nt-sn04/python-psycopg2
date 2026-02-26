from db import Database

db = Database()

db.add_user("test@gmail.com")

print(db.get_all_users()[-1])
