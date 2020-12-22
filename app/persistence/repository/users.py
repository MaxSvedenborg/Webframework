from persistence.mongo_models import *
import persistence.repository.crud_functions as cf


def get_all_users():
    return cf.get_all_assets(User)


def add_user(insert_dict):
    return cf.add(User, insert_dict)


def get_resource():
    return cf.get_resource(User)


def main():
    print(get_resource())


if __name__ == "__main__":
    main()
