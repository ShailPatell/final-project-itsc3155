DROP DATABASE IF EXISTS petFinder;

CREATE DATABASE IF NOT EXISTS PetFinder;

USE petFinder;

CREATE TABLE IF NOT EXISTS user (
    user_id INT AUTO_INCREMENT NOT NULL,
    user_username VARCHAR(255) NOT NULL,
    user_password VARCHAR(225) NOT NULL,
    first_name VARCHAR(255) NOT NULL,
    last_name VARCHAR(255) NOT NULL,
    user_age INT NOT NULL,
    user_gender VARCHAR(255) NOT NULL,
    user_email_address VARCHAR(255) NOT NULL,
    PRIMARY KEY (user_id)
);

