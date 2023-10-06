# Database-Project

Data Base project (3 deliveries)


This repository contains a database project that focuses on various aspects of database management, SQL query design, and the development of a web application prototype. The project is part of the Bases de Dados course for the academic year 2022/2023.

## Project Overview

The project is divided into several sections, each addressing different aspects of database management and application development:

1. **Database Loading**: In this phase, we load a predefined database schema and populate it with data. It is essential to ensure that all SQL and OLAP queries produce valid and non-empty results.

2. **Integrity Constraints**: We implement complex integrity constraints using SQL procedural extensions like Stored Procedures and Triggers. These constraints ensure data consistency and accuracy within the database.

3. **SQL Queries**: The project includes the design of advanced SQL queries to answer specific questions related to the database schema. These queries demonstrate proficiency in SQL query writing.

4. **Views**: A view is created to summarize key information about product sales by combining data from various database tables. The view schema is defined to facilitate data analysis.

5. **Web Application Prototype**: A prototype of a web application is developed using Python CGI scripts and HTML pages. The application enables functionalities like product and supplier registration, price updates, customer management, order placement, and payment simulation. Security measures are taken to prevent SQL injection, and data operations are handled atomically using transactions.

6. **OLAP Queries**: Using the previously created view, we write OLAP (Online Analytical Processing) queries to analyze data, such as calculating product sales by various dimensions like city, month, day, and week.

## Project Structure

- `populate.sql`: Contains SQL instructions for loading data into the database.
- `ICs.sql`: Includes SQL code for implementing integrity constraints using Stored Procedures and Triggers.
- `queries.sql`: Contains SQL queries designed to answer specific questions about the database.
- `view.sql`: Provides instructions for creating the view that summarizes product sales information.
- `analytics.sql`: Contains OLAP queries for data analysis.
- `web/`: This directory contains Python CGI scripts and HTML pages that form the web application prototype.
