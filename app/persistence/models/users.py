from persistence import *



class User(Document):
    email = StringField(required=True)
    password = StringField(min_length=8, max_length=14)
    first_name = StringField(max_length=50)
    last_name = StringField(max_length=50)
    username = StringField(max_length=50)


def main():
    pass


if __name__ == '__main__':
    main()
