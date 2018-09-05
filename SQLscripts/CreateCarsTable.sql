DROP TABLE IF EXISTS cars;

CREATE TABLE `cars` (
	  `id` int(11) NOT NULL AUTO_INCREMENT,
	  `Car_MakeName` varchar(255) NOT NULL,
	  `Car_Model` varchar(255) NOT NULL,
	  `Car_Series` varchar(255) NOT NULL,
	  `Car_SeriesYear` int(11) NOT NULL,
	  `Car_PriceNew` int(11) NOT NULL,
	  `Car_EngineSize` varchar(255) NOT NULL,
	  `Car_FuelSystem` varchar(255) NOT NULL,
	  `Car_TankCapacity` varchar(255) NOT NULL,
	  `Car_Power` varchar(255) NOT NULL,
	  `Car_SeatingCapacity` int(11) NOT NULL,
	  `Car_StandardTransmission` varchar(255) NOT NULL,
	  `Car_BodyType` varchar(255) NOT NULL,
	  `Car_Drive` varchar(3) NOT NULL,
	  `Car_Wheelbase` varchar(255) NOT NULL,
	  PRIMARY KEY (`id`)
);

LOAD DATA INFILE 'C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/car.csv' 
INTO TABLE cars
FIELDS TERMINATED BY ',' 
LINES TERMINATED BY '\n'
IGNORE 1 ROWS;