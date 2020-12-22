from persistence.mongo_models import *
import persistence.repository.crud_functions as cf


def get_all_users():
    return cf.get_all_assets(User)


def add_user(insert_dict):
    return cf.add_row(User, insert_dict)


def get_columns():
    return cf.get_columns(User)


def main():
    print(get_columns())


if __name__ == "__main__":
    main()
