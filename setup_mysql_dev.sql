-- prepares a MySQL server for the project

CREATE DATABASE IF NOT EXISTS geolens_dev_db;
CREATE USER IF NOT EXISTS 'geolens_dev'@'localhost' IDENTIFIED BY 'geolens_dev_pwd';
GRANT ALL PRIVILEGES ON `geolens_dev_db`.* TO 'geolens_dev'@'localhost';
GRANT SELECT ON `performance_schema`.* TO 'geolens_dev'@'localhost';
FLUSH PRIVILEGES;
