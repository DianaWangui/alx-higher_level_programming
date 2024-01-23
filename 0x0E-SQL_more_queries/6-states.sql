-- script that creates the database hbtn_0d_2 and the user_0d_2 user

CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;

USE hbtn_0d_usa;

-- Create table
CREATE TABLE IF NOT EXISTS `states`(id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(256) NOT NULL);