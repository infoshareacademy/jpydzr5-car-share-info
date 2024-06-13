from feature1 import get_rental_location
from json_handler import json_user_data_writer
# from json_handler import json_user_data_reader


def main():
    try:
        # Unpacking values from feature1
        street, postal_code, city = get_rental_location()  # type: ignore

        # Prepare get_rental_location function to save to json
        data = {
            "street": street,
            "postal_code": postal_code,
            "city": city,
        }

        # JSON user_data_writer
        json_user_data_writer(path="json/user_data.json", function_data=data)

        # JSON user_data_reader
        # data = json_user_data_reader(path="json/user_data.json")
        # print(data)
    except Exception as e:
        return e


if __name__ == "__main__":
    main()
