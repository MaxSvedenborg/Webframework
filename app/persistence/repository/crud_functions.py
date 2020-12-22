def get_all_assets(mongo_object):
    return mongo_object.all()


def add_row(mongo_object, insert_dict):
    return mongo_object.insert_one(insert_dict)


if __name__ == "__main__":
    pass

