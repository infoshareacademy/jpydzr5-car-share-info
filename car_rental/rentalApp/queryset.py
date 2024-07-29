import os
import sys

from django import setup

project_path = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(project_path))

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "car_rental.settings")
setup()


from rentalApp.models import Contact  # noqa: E402

query = Contact.objects.all()
print(query)
