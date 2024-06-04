import json
import re
from feature1 import get_rental_location
from json_handler import json_user_data_writer


def main():
    # Unpacking values from function
    street, postal_code, city = get_rental_location()

    # Prepare get_rental_location function to save to json
    data = {
        "street": street,
        "postal_code": postal_code,
        "city": city,
    }

    # JSON handler
    json_user_data_writer(path="json/user_data.json", function_data=data)


if __name__ == "__main__":
    main()
