# Contact-Management-System
Contact Management System in Python

****Requirements and Installation****

Use pip3 instead of pip for Linux and Mac.

Install PyMySQL
☛pip install PyMySQL

Install Tkinter
☛pip install tk



****Install MySQL server****



****Create a Database and a Table****

Create a database with this name: "contact_management_system"
☛create database contact_management_system;

Create a table "contact_register_system" under the "contact_management_system" database.
☛CREATE TABLE contact_register_system (
  first_name VARCHAR(255) NOT NULL,
  last_name VARCHAR(255) NOT NULL,
  company VARCHAR(255),
  contact VARCHAR(20) NOT NULL,
  email VARCHAR(255) NOT NULL,
  website VARCHAR(255),
  address_unit_number VARCHAR(20),
  address_civic_number VARCHAR(20),
  address_street VARCHAR(255),
  address_city VARCHAR(255),
  address_province CHAR(2) NOT NULL,
  address_postal_code CHAR(7) NOT NULL
);

Create a table "users" under the "contact_management_system" database.
☛create table users(
	username VARCHAR(10) NOT NULL,
	password VARCHAR(10) NOT NULL
);


