
# mongoengine http://mongoengine.org/
from mongoengine import *
from persistence.db_settings import *

connect(
    DB,
    host="mongodb://" +
    USER + ":" +
    PASSWORD + "@" +
    HOST + ":" +
    PORT + '/?authSource=admin'
)


def main():
    pass


if __name__ == '__main__':
    main()
