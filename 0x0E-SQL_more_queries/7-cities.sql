-- script that creates the database hbtn_0d_2 and the user_0d_2 user

CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;

USE hbtn_0d_usa;

-- Create table
CREATE TABLE IF NOT EXISTS `cities`(id INT AUTO_INCREMENT PRIMARY KEY,
state_id INT NOT NULL,
FOREIGN KEY (state_id) REFERENCES states(id),
name VARCHAR(256) NOT NULL);