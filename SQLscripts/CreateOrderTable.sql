DROP TABLE IF EXISTS Orders;
CREATE table Orders (
	ID INT NOT NULL AUTO_INCREMENT KEY,
    CreateDate INT,
    PickupDate INT,
    PickupStore INT,
    ReturnDate INT,
    ReturnStore INT,
    CustomerID INT,
    CarID INT
);

LOAD DATA INFILE 'C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/Order.csv' 
INTO TABLE Orders
FIELDS TERMINATED BY ',' 
LINES TERMINATED BY '\n'
IGNORE 1 ROWS;

ALTER TABLE Orders
ADD FOREIGN KEY (PickupStore) REFERENCES Stores(ID);

ALTER TABLE Orders
ADD FOREIGN KEY (ReturnStore) REFERENCES Stores(ID);

ALTER TABLE Orders
ADD FOREIGN KEY (CustomerID) REFERENCES Customers(ID);

ALTER TABLE Orders
ADD FOREIGN KEY (CarID) REFERENCES Cars(id);