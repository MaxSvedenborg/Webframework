from persistence import Document, db


class User(Document):
    collection = db.users
