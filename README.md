Employee Management System

A Python-based Employee Management System developed using Object-Oriented Programming (OOP) concepts, JSON data storage, and a Streamlit graphical user interface.

Project Overview

The Employee Management System is designed to manage employee and department information in an organized way. It provides functionality for employee registration, department management, salary calculation, performance evaluation, incentive calculation, promotion management, employee search, deletion, and reporting.

The project is implemented in two parts:

core/ contains the console-based core implementation.
gui/ contains the Streamlit-based graphical user interface.

Employee and department data are stored persistently using JSON files.

Features
Employee Management
Add new employees
Search employees
Update employee salary
Delete employees
View employee details
Validate employee information
Prevent duplicate employee IDs
Department Management
Add departments
View departments
Update departments
Delete departments
Assign employees to departments
Salary Management
Store employee salary
Update salary
Calculate salary according to employee role
Apply role-specific allowances
Performance Rating
Enter performance ratings manually
Accept ratings from 1 to 5
Automatically classify employee performance
Store performance ratings in JSON
Incentive Calculation
Calculate incentive percentage based on performance
Calculate incentive amount
Store incentive information
Promotion Management

The system provides role-based promotion paths.

Current Role	Promotion
Intern	Intern → Developer
Developer	Developer → Senior Developer
Senior Developer	Senior Developer → Manager
Manager	Manager → Senior Manager

For Senior Developers, promotion is based on both performance rating and experience.

Requirements:

Performance Rating >= 4.0
Experience >= 5 years

The system displays the promotion path and eligibility result.

Employee Reports

Employee reports display important employee information including:

Employee ID
Name
Age
Department
Salary
Role
Experience where applicable
Performance Rating
Performance
Incentive Percentage
Incentive
Promotion Status
Object-Oriented Programming Concepts

The project demonstrates several Python OOP concepts.

Classes and Objects

The system uses classes to represent employees, departments, and different employee roles.

Inheritance

The project uses inheritance to create specialized employee roles.

Employee
|
|-- Developer
|   |
|   |-- SeniorDeveloper
|
|-- Manager
|
|-- Intern
Multilevel Inheritance

SeniorDeveloper inherits from Developer, which inherits from Employee.

Method Overriding

Different employee roles implement their own versions of methods such as:

work()
calculate_salary()
promotion()
Encapsulation

Employee attributes and methods are organized inside classes to manage employee data and behavior.

Class Method

A class method is used for operations related to the Employee class.

Static Method

A static method is used for salary validation.

Abstract Method

The base Employee class defines functionality that is implemented by the derived employee classes.

Polymorphism

The same method can behave differently depending on the employee's role.

Project Structure
Employee-Management-System/
|
|-- core/
|   |-- employee.py
|   |-- roles.py
|   |-- validation.py
|   |-- data_manager.py
|   |-- department.py
|   |-- main.py
|
|-- gui/
|   |-- app.py
|
|-- data/
|   |-- employees.json
|   |-- departments.json
|
|-- .vscode/
|
|-- .gitignore
|
|-- README.md
Core Modules
employee.py

Contains the base Employee class and common employee functionality.

roles.py

Contains the different employee roles:

Developer
SeniorDeveloper
Manager
Intern
department.py

Contains department-related functionality.

validation.py

Contains input validation functions for employee information such as:

Positive integers
Age
Salary
Names
Ratings
Experience
data_manager.py

Handles persistent data storage.

Main functions include:

load_employees()
save_employees()
load_departments()
save_departments()
create_employee_objects()
main.py

Contains the console-based Employee Management System and provides a menu-driven interface.

Graphical User Interface

The GUI is developed using Streamlit.

The GUI provides modules for:

Dashboard
Employee Registration
Department Management
Employee Search
Salary Calculation
Performance Rating
Incentive Calculation
Promotion
Employee Reports
OOP Concepts

The GUI provides an easier way to interact with the core functionality without using the command-line menu.

Data Storage

The application uses JSON files for persistent storage.

Employee data is stored in:

data/employees.json

Department data is stored in:

data/departments.json

The data_manager.py module is responsible for loading and saving this information.

Technologies Used
Python
Streamlit
JSON
Object-Oriented Programming
Git
GitHub
Requirements

Python 3.x is required to run the project.

Install Streamlit using:

pip install streamlit
How to Run
Run the Console Application

From the project root directory:

python core/main.py
Run the Streamlit GUI

From the project root directory:

streamlit run gui/app.py

The Streamlit application will open in the browser.

Example Workflow

A typical workflow in the application is:

Add Department
       |
       v
Register Employee
       |
       v
Calculate Salary
       |
       v
Enter Performance Rating
       |
       v
Calculate Incentive
       |
       v
Check Promotion
       |
       v
View Employee Report
Promotion Example

For a Developer with a performance rating of 4.5:

Current Role: Developer
Performance Rating: 4.5

Promotion Path:
Developer → Senior Developer

Result:
Selected for Promotion

For a Senior Developer:

Current Role: Senior Developer
Performance Rating: 4.5
Experience: 5 years

Promotion Path:
Senior Developer → Manager

Result:
Selected for Promotion
Project Objective

The main objective of this project is to apply Python programming and Object-Oriented Programming concepts to a practical real-world Employee Management System.

The project also demonstrates how a Python core application can be connected to a graphical user interface and persistent JSON data storage.

Author

Abhiram Ajith

GitHub: https://github.com/ajithabhiram