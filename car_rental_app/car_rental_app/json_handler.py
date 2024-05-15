import json


# JSON Writer
def json_writer(path, inst_var, inst_str):
    try:
        blueprint = {inst_str: dict(inst_var)}
        with open(path, "w") as f:
            json.dump(blueprint, f, indent=4)
    except Exception as e:
        print(e.args)


# JSON Reader
def json_reader(path):
    try:
        with open(path, "r") as f:
            data = json.load(f)
            return data
    except Exception as e:
        return e.args
