
import json

# Update maintenance date and put new cost
with open('car_data.json', 'r') as file:
    car_data = json.load(file)

# Update the date and cost of the last maintenance record
last_record = car_data['maintenanceRecords'][-1]
last_record['date'] = "2022-02-10"
last_record['cost'] = 60.00

# Write updated JSON data back to the file
with open('car_data.json', 'w') as file:
    json.dump(car_data, file, indent=2)

print('Maintenance date and cost updated in car_data.json.')
