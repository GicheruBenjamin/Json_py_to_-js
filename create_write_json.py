
# Import json module
import json

# Create and write JSON file
car_data = {
    "manufacturer": "Toyota",
    "model": "Camry",
    "maintenanceRecords": [
        {
            "date": "2021-09-15",
            "description": "Oil Change",
            "cost": 50.00
        },
        {
            "date": "2021-11-20",
            "description": "Brake Inspection",
            "cost": 40.00
        }
    ]
}

with open('car_data.json', 'w') as file:
    json.dump(car_data, file, indent=2)

print('Car data created and written to car_data.json.')
