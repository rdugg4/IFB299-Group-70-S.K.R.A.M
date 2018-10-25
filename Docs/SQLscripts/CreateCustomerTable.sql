DROP TABLE IF EXISTS Customers;
CREATE table Customers (
	ID INT NOT NULL AUTO_INCREMENT KEY,
    Name VARCHAR(255),
    Phone VARCHAR(20),
    Address VARCHAR(255),
    DOB VARCHAR(20),
    Occupation VARCHAR(255),
    Gender VARCHAR(3),
    Email VARCHAR(255),
    Password VARCHAR(255)
);

LOAD DATA INFILE 'C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/customer.csv' 
INTO TABLE Customers
FIELDS TERMINATED BY ',' 
LINES TERMINATED BY '\n'
IGNORE 1 ROWS;

SET SQL_SAFE_UPDATES = 0;
UPDATE customers
SET Email = NULL
Where Email = 'NULL';

UPDATE customers
SET Password = NULL;

