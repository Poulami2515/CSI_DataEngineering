-- giving privilege access of a new database to localhost
CREATE USER 'poulami'@'localhost' IDENTIFIED BY '{your_password}';
GRANT ALL PRIVILEGES ON master.* TO 'poulami'@'localhost';
FLUSH PRIVILEGES;
