-- CREATE DATABASE webapp;
CREATE USER 'root'@'db' IDENTIFIED BY 'mypassword';
GRANT ALL PRIVILEGES ON webapp.* TO 'root'@'db';
-- CREATE USER 'root'@'localhost' IDENTIFIED BY 'mypassword';
-- GRANT ALL PRIVILEGES ON webapp.* TO 'root'@'localhost';
FLUSH PRIVILEGES;

USE webapp;
CREATE TABLE employees (  id INT(11) NOT NULL AUTO_INCREMENT,  name VARCHAR(255) NOT NULL,  email VARCHAR(255) NOT NULL,  PRIMARY KEY (id));
INSERT INTO employees (name, email) VALUES   ('John Doe', 'john.doe@example.com');
INSERT INTO employees (name, email) VALUES   ('Smith', 'Smith@example.com');
INSERT INTO employees (name, email) VALUES   ('Cena', 'Cena@example.com');