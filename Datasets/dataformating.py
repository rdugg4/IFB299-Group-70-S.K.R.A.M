# Read CSV file into the python file
import csv
with open('InitialDataSet.csv', newline='') as csvfile:
    data = list(csv.reader(csvfile))

#Detete all the rows with NULL values
width = len(data[0])
height = len(data)
noNullData = [[0 for x in range(width)] for y in range(height)]
nullCounter = 0
for i in range(0, len(data)):
    NoNull = True
    for j in range (0, len(data[0])):
        if (data[i][j] == 'NULL'):
            NoNull = False
        if ',' in data[i][j]:
            data[i][j] = data[i][j].replace(',', '')
    if (NoNull):
        noNullData[i-nullCounter] = data[i]
    else:
        nullCounter = nullCounter + 1

# Create the a correctly size array conatining the dataset without NULL values
dataSet = noNullData[0:(height-nullCounter)]

# Split the data up ready for entry to each table in the database
storeData = [[0 for x in range(6)] for y in range(len(dataSet)*2)]
carData = [[0 for x in range(15)] for y in range(len(dataSet))]
customerData = [[0 for x in range(9)] for y in range(len(dataSet))]
orderData = [[0 for x in range(9)] for y in range(len(dataSet))]
for i in range(0, len(dataSet)):
    for j in range(0, len(data[0])):
        if (j >= 0 and j < 4):
            orderData[i][j] = dataSet[i][j]
        if (j >= 3 and j < 9):
            storeData[2*i][j-3] = dataSet[i][j]
        if (j >= 9 and j < 11):
            orderData[i][j-5] = dataSet[i][j]
        if (j >= 10 and j < 16):
            storeData[2*i+1][j-10] = dataSet[i][j]
        if (j == 16):
            orderData[i][j-9] = dataSet[i][j]
        if (j >= 16 and j < 23):
            customerData[i][j-16] = dataSet[i][j]
        if (j == 23):
            orderData[i][j-15] = dataSet[i][j]
        if (j >= 23 and j < 38):
            carData[i][j-23] = dataSet[i][j]

# Remove Duplicates from the store data set
storeDataNoDuplicates = [[0 for x in range(6)] for y in range(len(dataSet)*2)]
duplicateCounter = 0
for i in range(0, len(storeData)):
    alreadyExists = False
    if (i == 1):
        alreadyExists = True
    for j in range(0, i):
        if (storeData[i][0] == storeData[j][0]):
            alreadyExists = True
    if (alreadyExists):
        duplicateCounter = duplicateCounter + 1
    else:
        storeDataNoDuplicates[i - duplicateCounter] = storeData[i]
storeDataFinal = storeDataNoDuplicates[0:(len(storeDataNoDuplicates)-duplicateCounter)]

# Remove Duplicates from the customer and car data sets
carDataNoDuplicates = [[0 for x in range(15)] for y in range(len(dataSet))]
customerDataNoDuplicates = [[0 for x in range(9)] for y in range(len(dataSet))]
orderDataNoDuplicates = [[0 for x in range(9)] for y in range(len(dataSet))]
duplicateCounter_car = 0
duplicateCounter_customer = 0
duplicateCounter_order = 0
for i in range(0, len(dataSet)):
    alreadyExists_car = False
    alreadyExists_customer = False
    alreadyExists_order = False
    for j in range(0, i):
        # Check if a particular line of data already exists in final dataset
        if (carData[i][0] == carData[j][0]):
            alreadyExists_car = True
        if (customerData[i][0] == customerData[j][0]):
            alreadyExists_customer = True
        if (orderData[i][0] == orderData[j][0]):
            alreadyExists_order = True
    # Update the amount of data duplicates or add the data to the non-dulipcate set
    if (alreadyExists_car):
        duplicateCounter_car = duplicateCounter_car + 1
    else:
        carDataNoDuplicates[i - duplicateCounter_car] = carData[i]
    if (alreadyExists_customer):
        duplicateCounter_customer = duplicateCounter_customer + 1
    else:
        customerDataNoDuplicates[i - duplicateCounter_customer] = customerData[i]
        customerDataNoDuplicates[i - duplicateCounter_customer][7] = 'NULL'
        customerDataNoDuplicates[i - duplicateCounter_customer][8] = 'NULL'
    if (alreadyExists_order):
        duplicateCounter_order = duplicateCounter_order + 1
    else:
        orderDataNoDuplicates[i - duplicateCounter_order] = orderData[i]
        orderDataNoDuplicates[i - duplicateCounter_order][6] = 'True'
carDataFinal = carDataNoDuplicates[0:(len(carDataNoDuplicates)-duplicateCounter_car)]
customerDataFinal = customerDataNoDuplicates[0:(len(customerDataNoDuplicates)-duplicateCounter_customer)]
orderDataFinal = orderDataNoDuplicates[0:(len(orderDataNoDuplicates)-duplicateCounter_order)]

# Define the titles of some new columns
customerDataFinal[0][7] = 'Username'
customerDataFinal[0][8] = 'Password'
orderDataFinal[0][6] = 'Dropped Off'

# Write the CSV files for each data set
with open('customer.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile, delimiter=',',
                            quotechar='|', quoting=csv.QUOTE_MINIMAL)
    for i in range(0, len(customerDataFinal)):
        writer.writerow(customerDataFinal[i])

with open('car.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile, delimiter=',',
                            quotechar='|', quoting=csv.QUOTE_MINIMAL)
    for i in range(0, len(carDataFinal)):
        writer.writerow(carDataFinal[i])

with open('store.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile, delimiter=',',
                            quotechar='|', quoting=csv.QUOTE_MINIMAL)
    for i in range(0, len(storeDataFinal)):
        writer.writerow(storeDataFinal[i])

with open('order.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile, delimiter=',',
                            quotechar='|', quoting=csv.QUOTE_MINIMAL)
    for i in range(0, len(orderDataFinal)):
        writer.writerow(orderDataFinal[i])
