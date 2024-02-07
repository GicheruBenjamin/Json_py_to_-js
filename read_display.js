
// Get the fs module
const fs = require('fs');

// A func to read the json
function readJson(filePath) {
    const jsonString = fs.readFileSync(filePath);
    return JSON.parse(jsonString);
}
//A func to display maintenance information
function displayMaintenanceInfo(data) {
    console.log('Maintenance Records:');
    data.maintenanceRecords.forEach(record => {
        console.log(`Date: ${record.date}, Description: ${record.description}, Cost: $${record.cost}`);
        if (record.date >= "2021-10-01") {
            console.log('Updated: Yes');
        } else {
            console.log('Updated: No');
        }
    });
}

// Simulate receiving data from Python
const receivedData = readJson('car_data.json');
displayMaintenanceInfo(receivedData);
