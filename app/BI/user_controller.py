from persistence.repository import users as ur


def create_user(user_data):
    ur.create_user(user_data)
