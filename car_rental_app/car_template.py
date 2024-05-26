from pydantic import BaseModel
import datetime
from json_handler import json_writer, json_reader


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
    Fuel_type: String representing the type of fuel the car uses (e.g., "Gasoline", "Diesel", "Hybrid", "Electric").
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


class BMW3(Car):
    def __init__(self, *args, **kwargs):
        # Call the superclass constructor with the required arguments
        super().__init__(**kwargs)  # *args if needed

        # Add specific BMW3 attributes (if any) here
        # ...


# Create an instance of the BMW3 class
id_001 = BMW3(
    brand="BMW",
    model="3 Series",
    year=2023,
    car_category="S",
    license_plate_number="RZ2390",
    mileage=30000,
    engine_size=2.0,
    fuel_type="Gasoline",
    gearbox="Automatic",
    air_condition=True,
    number_of_seats=5,
    number_of_doors=4,
    color="Alpine White",
    body_style="Sedan",
)
# Convert an instance to JSON file®
json_writer(path="json/cars.json", inst_var=id_001, inst_str="id_001")

# Read from the JSON file
instance_001 = json_reader(path="json/cars.json")

# Print values from the instance
print(f"Brand: {instance_001['id_001']['brand']}")
print(f"Model: {instance_001['id_001']['model']}")
