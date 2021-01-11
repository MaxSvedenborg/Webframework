from persistence.models.users import *


def create_user(data):
    user = User(email=data['email'])
    user.password = data['password']
    user.username = data['username']
    user.first_name = data['first_name']
    user.last_name = data['last_name']
    user.save()
    return user
