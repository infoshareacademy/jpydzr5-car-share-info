from feature1 import get_rental_location
from feature2 import get_rental_period
from feature3 import choose_car_category
from feature4 import choose_extras
from feature5 import get_personal_data
from feature6 import get_user_address
from json_handler import json_user_data_reader, json_user_data_writer


def main():
    try:
        # Unpacking values from feature1
        street, postal_code, city = get_rental_location()  # type: ignore

        # Unpacking values from feature2
        start_date, start_time, end_date, end_time = get_rental_period()  # type: ignore

        # Unpacking values from feature3
        car_category = choose_car_category()
        if car_category is False:
            raise

        # Unpacking values from feature4
        insurance = choose_extras()
        if insurance is False:
            raise

        # Unpacking values from feature5
        first_name, last_name, email, phone, pesel, license_number = get_personal_data()  # type: ignore

        # Unpacking values from feature6
        street_, apartment_number_, postal_code_, city_, country_ = get_user_address()  # type: ignore

        # Prepare functions to save to json
        data = {
            # feature1
            "street": street,
            "postal_code": postal_code,
            "city": city,
            # feature2
            "start_date": start_date,
            "start_time": start_time,
            "end_date": end_date,
            "end_time": end_time,
            # feature3
            "car_category": car_category,
            # feature4
            "insurance": insurance,
            # feature5
            "first_name": first_name,
            "last_name": last_name,
            "email": email,
            "phone": phone,
            "pesel": pesel,
            "license_number": license_number,
            # feature6
            "street_": street_,
            "apartment_number_": apartment_number_,
            "postal_code_": postal_code_,
            "city_": city_,
            "country_": country_,
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
