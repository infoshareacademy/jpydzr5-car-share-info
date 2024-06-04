import json
from os import path as path_


# JSON car instance writer v.01
# def json_car_writer(path, inst_str, inst_var):
#     try:
#         blueprint = {inst_str: dict(inst_var)}
#         with open(path, "w") as f:
#             json.dump(blueprint, f, indent=4)
#     except Exception as e:
#         print(e.args)

# JSON car instance writer v.02
def json_car_writer(path, inst_str, inst_var):
    try:
        if not path_.exists(path):
            blueprint = {inst_str: dict(inst_var)}
        else:
            with open(path, "r") as f:
                try:
                    blueprint = json.load(f)
                    # blueprint = {}
                except json.JSONDecodeError:
                    blueprint = {}

        blueprint[inst_str] = dict(inst_var)

        with open(path, "w") as f:
            json.dump(blueprint, f, indent=4)

    except Exception as e:
        print(e.args)


# JSON car instance reader
def json_car_reader(path):
    try:
        with open(path, "r") as f:
            data = json.load(f)
            return data
    except Exception as e:
        return e.args


# JSON user data writer
def json_user_data_writer(path, function_data: dict):
    with open(path, "w") as f:
        json.dump(function_data, f, indent=4)
