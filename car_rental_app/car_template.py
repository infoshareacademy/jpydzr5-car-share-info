from pydantic import BaseModel
import datetime
from json_handler import json_car_writer, json_car_reader


class Car(BaseModel):
    """
    Basic Car Information:

    Brand: String representing the car manufacturer (e.g., "Ford", "Toyota", "BMW").
    Model: String representing the specific car model (e.g., "Fiesta", "Corolla", "X5").
    Year: Integer representing the year the car was manufactured (e.g., 2023, 2018, 2005).
    Car_category : String representing the car's category (e.g., "A", "B", "C", "S").
    License_plate_number: String representing the car's unique license plate number (e.g., "ABC-123", "XYZ-456").
    Mileage: Integer representing the total distance the car has traveled (e.g., 30000, 55000, 120000).
    Engine_size: Float representing the engine displacement of the car in liters (e.g., 1.6, 2.0, 3.5).
    Fuel_type: String representing the type of fuel the car uses (e.g., "Petrol", "Diesel", "Hybrid", "Electric").
    Gearbox: String representing transmission the car has (e.g., "Automatic", "Manual").
    Air_condition: It can be included as a boolean attribute (True/False) or a string ("Yes"/"No").
    Number_of_seats: Integer representing the number of passenger seats the car has (e.g., 5, 7, 8).
    Number_of_doors: Integer representing the number of doors the car has (e.g., 5, 7, 8).

    Rental Information:

    Status: String representing the current availability of the car (e.g., "Available", "Rented", "In Repair").
    Daily_rental_rate: Float representing the daily cost to rent the car (e.g., 50.00, 75.50, 120.75).
    rental_history: List of previous rentals for the car.

    Additional Car Details:

    color: String representing the exterior color of the car (e.g., "Red", "Silver", "Black").
    body_style: String representing the type of car body (e.g., "Sedan", "SUV", "Hatchback").
    features: List of additional features the car has (e.g., "Android Auto", "Apple Carplay", "Sunroof").
    images: List of URLs or file paths to images of the car.
    insurance: Information about the car's insurance coverage (format can be defined based on your needs).
    location: Information about the car's current location (e.g., coordinates or address).
    maintenance_history: Record of the car's maintenance history.
    inspection_due_date: Date when the next car inspection is due.
    damage_report: Record of any known damage to the car.
    additional_notes: Any additional notes or information about the car.
    """

    # Basic Car Information
    brand: str
    model: str
    year: int
    car_category: str
    license_plate_number: str
    mileage: float
    engine_size: float
    fuel_type: str
    gearbox: str
    air_condition: bool
    number_of_seats: int
    number_of_doors: int
    color: str
    body_style: str

    # Rental Information
    status: str = "Not Available"
    daily_rental_rate: float = 0.0
    rental_start_date: datetime.datetime | None = None
    rental_end_date: datetime.datetime | None = None
    rental_history: list[dict] = []

    # Additional Car Details
    features: list[str] = []
    images: list[str] = []
    insurance: list[dict] = []
    location: dict = {}
    maintenance_history: list[dict] = []
    inspection_due_date: dict = {}
    damage_report: list[dict] = []
    additional_notes: dict = {}


class Vehicle(Car):
    def __init__(self, *args, **kwargs):
        # Call the superclass constructor with the required arguments
        super().__init__(**kwargs)  # *args if needed

        # Add specific attributes (if any) here
        # ...


# Create an instance of the vehicle class
id_001 = Vehicle(
    brand="Toyota",
    model="Aygo",
    year=2024,
    car_category="Mini",
    license_plate_number="PO4575",
    mileage=12000,
    engine_size=1.0,
    fuel_type="Hybrid",
    gearbox="Automatic",
    air_condition=True,
    number_of_seats=5,
    number_of_doors=4,
    color="Barcelona Red",
    body_style="Hatchback",
)

id_002 = Vehicle(
    brand="Fiat",
    model="500",
    year=2023,
    car_category="Mini",
    license_plate_number="PO8796",
    mileage=35000,
    engine_size=1.2,
    fuel_type="Petrol",
    gearbox="Manual",
    air_condition=False,
    number_of_seats=4,
    number_of_doors=2,
    color="Blue Sky",
    body_style="Hatchback",
)

id_003 = Vehicle(
    brand="Opel",
    model="Corsa",
    year=2023,
    car_category="Economy",
    license_plate_number="WA4532",
    mileage=66000,
    engine_size=1.2,
    fuel_type="Petrol",
    gearbox="Manual",
    air_condition=False,
    number_of_seats=5,
    number_of_doors=4,
    color="Azure Red",
    body_style="Hatchback",
)

id_004 = Vehicle(
    brand="Toyota",
    model="Yaris",
    year=2024,
    car_category="Economy",
    license_plate_number="WA2324",
    mileage=42000,
    engine_size=1.0,
    fuel_type="Hybrid",
    gearbox="Automatic",
    air_condition=True,
    number_of_seats=5,
    number_of_doors=4,
    color="Silver Sky",
    body_style="Hatchback",
)

id_005 = Vehicle(
    brand="Volkswagen",
    model="Polo",
    year=2023,
    car_category="Economy",
    license_plate_number="GD4226",
    mileage=68000,
    engine_size=1.2,
    fuel_type="Petrol",
    gearbox="Manual",
    air_condition=True,
    number_of_seats=5,
    number_of_doors=4,
    color="Pure White",
    body_style="Hatchback",
)

id_006 = Vehicle(
    brand="Skoda",
    model="Fabia",
    year=2022,
    car_category="Economy",
    license_plate_number="PO7812",
    mileage=112000,
    engine_size=1.2,
    fuel_type="Petrol",
    gearbox="Manual",
    air_condition=True,
    number_of_seats=5,
    number_of_doors=4,
    color="Ocean Blue",
    body_style="Hatchback",
)

id_007 = Vehicle(
    brand="Opel",
    model="Astra",
    year=2023,
    car_category="Compact",
    license_plate_number="PO5642",
    mileage=89000,
    engine_size=1.2,
    fuel_type="Petrol",
    gearbox="Manual",
    air_condition=True,
    number_of_seats=5,
    number_of_doors=4,
    color="Black",
    body_style="Hatchback",
)

id_008 = Vehicle(
    brand="Toyota",
    model="Corolla",
    year=2023,
    car_category="Compact",
    license_plate_number="WA2354",
    mileage=75000,
    engine_size=1.0,
    fuel_type="Hybrid",
    gearbox="Automatic",
    air_condition=True,
    number_of_seats=5,
    number_of_doors=4,
    color="Pearl",
    body_style="Hatchback",
)

id_009 = Vehicle(
    brand="Volkswagen",
    model="Golf",
    year=2024,
    car_category="Compact",
    license_plate_number="DW4521",
    mileage=22000,
    engine_size=2.0,
    fuel_type="Diesel",
    gearbox="Manual",
    air_condition=True,
    number_of_seats=5,
    number_of_doors=4,
    color="Arctic Blue",
    body_style="Hatchback",
)

id_010 = Vehicle(
    brand="Skoda",
    model="Kamiq",
    year=2023,
    car_category="SUV",
    license_plate_number="PO4112",
    mileage=54000,
    engine_size=1.8,
    fuel_type="Petrol",
    gearbox="Manual",
    air_condition=True,
    number_of_seats=5,
    number_of_doors=4,
    color="Cappucino Beige",
    body_style="SUV",
)

id_011 = Vehicle(
    brand="BMW",
    model="X3",
    year=2024,
    car_category="SUV",
    license_plate_number="GD7102",
    mileage=15000,
    engine_size=2.0,
    fuel_type="Diesel",
    gearbox="Automatic",
    air_condition=True,
    number_of_seats=5,
    number_of_doors=4,
    color="Grey Black",
    body_style="SUV",
)

id_012 = Vehicle(
    brand="AudiQ3",
    model="Q3",
    year=2023,
    car_category="SUV",
    license_plate_number="WA6425",
    mileage=43000,
    engine_size=1.8,
    fuel_type="Petrol",
    gearbox="Manual",
    air_condition=True,
    number_of_seats=5,
    number_of_doors=4,
    color="Seville Red",
    body_style="SUV",
)

id_013 = Vehicle(
    brand="Toyota",
    model="RAV4",
    year=2024,
    car_category="SUV",
    license_plate_number="WA7896",
    mileage=29000,
    engine_size=2.5,
    fuel_type="Hybrid",
    gearbox="Automatic",
    air_condition=True,
    number_of_seats=5,
    number_of_doors=4,
    color="Cavalry Blue",
    body_style="SUV",
)

id_014 = Vehicle(
    brand="BMW",
    model="3",
    year=2023,
    car_category="Medium",
    license_plate_number="RZ2390",
    mileage=30000,
    engine_size=2.0,
    fuel_type="Petrol",
    gearbox="Automatic",
    air_condition=True,
    number_of_seats=5,
    number_of_doors=4,
    color="Alpine White",
    body_style="Sedan",
)

id_015 = Vehicle(
    brand="Mercedes-Benz",
    model="Class C",
    year=2023,
    car_category="Medium",
    license_plate_number="GD4568",
    mileage=57000,
    engine_size=1.8,
    fuel_type="Petrol",
    gearbox="Automatic",
    air_condition=True,
    number_of_seats=5,
    number_of_doors=4,
    color="Midnight Blue",
    body_style="Sedan",
)

id_016 = Vehicle(
    brand="Audi",
    model="A4",
    year=2023,
    car_category="Medium",
    license_plate_number="WA2586",
    mileage=89000,
    engine_size=2.0,
    fuel_type="Diesel",
    gearbox="Automatic",
    air_condition=True,
    number_of_seats=5,
    number_of_doors=4,
    color="Terra Grey",
    body_style="Combi",
)

id_017 = Vehicle(
    brand="Skoda",
    model="Octavia",
    year=2023,
    car_category="Medium",
    license_plate_number="GD6854",
    mileage=125000,
    engine_size=1.8,
    fuel_type="Petrol",
    gearbox="Manual",
    air_condition=True,
    number_of_seats=5,
    number_of_doors=4,
    color="Candy White",
    body_style="Combi",
)

# Convert an instance to JSON file
json_car_writer(path="json/car_catalog.json", inst_str="id_001", inst_var=id_001)
json_car_writer(path="json/car_catalog.json", inst_str="id_002", inst_var=id_002)
json_car_writer(path="json/car_catalog.json", inst_str="id_003", inst_var=id_003)
json_car_writer(path="json/car_catalog.json", inst_str="id_004", inst_var=id_004)
json_car_writer(path="json/car_catalog.json", inst_str="id_005", inst_var=id_005)
json_car_writer(path="json/car_catalog.json", inst_str="id_006", inst_var=id_006)
json_car_writer(path="json/car_catalog.json", inst_str="id_007", inst_var=id_007)
json_car_writer(path="json/car_catalog.json", inst_str="id_008", inst_var=id_008)
json_car_writer(path="json/car_catalog.json", inst_str="id_009", inst_var=id_009)
json_car_writer(path="json/car_catalog.json", inst_str="id_010", inst_var=id_010)
json_car_writer(path="json/car_catalog.json", inst_str="id_011", inst_var=id_011)
json_car_writer(path="json/car_catalog.json", inst_str="id_012", inst_var=id_012)
json_car_writer(path="json/car_catalog.json", inst_str="id_013", inst_var=id_013)
json_car_writer(path="json/car_catalog.json", inst_str="id_014", inst_var=id_014)
json_car_writer(path="json/car_catalog.json", inst_str="id_015", inst_var=id_015)
json_car_writer(path="json/car_catalog.json", inst_str="id_016", inst_var=id_016)
json_car_writer(path="json/car_catalog.json", inst_str="id_017", inst_var=id_017)

# Read from the JSON file
car_catalog = json_car_reader(path="json/car_catalog.json")

# Print values from the instance
print(f"Brand: {car_catalog['id_017']['brand']}") # type: ignore
print(f"Model: {car_catalog['id_017']['model']}") # type: ignore
