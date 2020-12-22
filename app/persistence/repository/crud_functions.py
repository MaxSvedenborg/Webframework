def get_all_assets(mongo_object):
    return mongo_object.all()


def add(mongo_object, insert_dict):
    return mongo_object.insert_one(insert_dict)


def get_resource(mongo_object):
    'Returns key structure of the requested resource'
    dummy_request = mongo_object.find().first_or_none()
    if dummy_request is not None:
        return [key for key in dummy_request.__dict__]
    else:
        return []


if __name__ == "__main__":
    pass

