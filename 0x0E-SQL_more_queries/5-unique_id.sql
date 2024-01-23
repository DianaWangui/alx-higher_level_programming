-- script that creates the table unique_id on your MySQL server

CREATE TABLE IF NOT EXISTS `unique_id`(id INT DEFAULT 1 UNIQUE, name VARCHAR(256) NOT NULL);