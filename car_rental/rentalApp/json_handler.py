import json
import os

# JSON car instance writer
def json_car_writer(path, inst_str, inst_var):
    try:
        if not os.path.exists(path):
            blueprint = {inst_str: dict(inst_var)}
        else:
            with open(path, "r") as f:
                try:
                    blueprint = json.load(f)
                except json.JSONDecodeError:
                    blueprint = {}

        blueprint[inst_str] = dict(inst_var)

        with open(path, "w", encoding="utf8") as f:
            json.dump(blueprint, f, indent=4, ensure_ascii=False)

    except Exception as e:
        print(f"Error in json_car_writer: {e}")
        # Optionally, raise the exception to propagate it further if needed


# JSON car instance reader
def json_car_reader(path):
    try:
        with open(path, "r") as f:
            data = json.load(f)
            return data
    except Exception as e:
        print(f"Error in json_car_reader: {e}")
        return None


# JSON user data writer
def json_user_data_writer(path, function_data):
    try:
        if os.path.exists(path):
            with open(path, 'r', encoding='utf-8') as file:
                try:
                    data = json.load(file)
                except json.JSONDecodeError:
                    data = {}
        else:
            data = {}

        # Update data with function_data
        data.update(function_data)

        # Save updated data to JSON file
        with open(path, 'w', encoding='utf-8') as file:
            json.dump(data, file, indent=4, ensure_ascii=False)

    except Exception as e:
        print(f"Error in json_user_data_writer: {e}")
        # Optionally, raise the exception to propagate it further if needed


# JSON user data reader
def json_user_data_reader(path):
    try:
        with open(path, "r") as f:
            data = json.load(f)
            return data
    except Exception as e:
        print(f"Error in json_user_data_reader: {e}")
        return None
