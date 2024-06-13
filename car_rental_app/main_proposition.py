from feature1 import get_rental_location
from feature2 import get_rental_period
from json_handler import json_user_data_reader, json_user_data_writer


def main():
    try:
        # Unpacking values from feature1
        street, postal_code, city = get_rental_location()  # type: ignore

        # Unpacking values from feature2
        start_date, start_time, end_date, end_time = get_rental_period()  # type: ignore

        # Prepare functions to save to json
        data = {
            "street": street,
            "postal_code": postal_code,
            "city": city,
            "start_date": start_date,
            "start_time": start_time,
            "end_date": end_date,
            "end_time": end_time,
        }

        # JSON user_data_writer
        json_user_data_writer(path="json/user_data.json", function_data=data)

        # JSON user_data_reader
        data = json_user_data_reader(path="json/user_data.json")
        print(data)

    except Exception as e:
        return e


if __name__ == "__main__":
    main()
