# Employee Management System

A Python-based Employee Management System developed using Object-Oriented Programming (OOP), JSON data storage, and a Streamlit graphical user interface.

## Project Overview

The Employee Management System is designed to manage employees and departments in an organized way. It provides functionality for employee registration, department management, employee search, salary management, performance rating, incentive calculation, promotion management, employee reports, and employee deletion.

The project is implemented with a separate core application and graphical user interface.

- `core/` contains the Python core implementation and console-based application.
- `gui/` contains the Streamlit graphical user interface.
- `data/` contains JSON files used for persistent data storage.

## Features

### Employee Management

- Add new employees
- Search employees by Employee ID
- Update employee salary
- Delete employees
- View employee information
- Validate employee inputs
- Prevent duplicate employee IDs

### Department Management

- Add departments
- View departments
- Update departments
- Delete departments
- Assign employees to departments

### Salary Management

- Store employee salary information
- Update employee salary
- Calculate salary based on employee role
- Apply role-specific salary allowances

### Performance Rating

- Enter performance ratings manually
- Accept ratings between 1 and 5
- Automatically classify employee performance
- Store performance rating in JSON

Performance levels are determined based on the employee's rating.

### Incentive Calculation

- Calculate incentive percentage based on performance
- Calculate incentive amount
- Store incentive information
- Display incentive details in employee reports

### Promotion Management

The system provides role-based promotion paths.

| Current Role | Promotion Path |
|--------------|----------------|
| Intern | Intern → Developer |
| Developer | Developer → Senior Developer |
| Senior Developer | Senior Developer → Manager |
| Manager | Manager → Senior Manager |

Promotion eligibility depends on the employee's role, performance rating, and other required conditions.

For Senior Developer promotion:

- Performance Rating >= 4.0
- Experience >= 5 years

The system displays the current role, performance rating, experience where applicable, promotion path, required conditions, and final promotion status.

### Employee Reports

The Employee Reports section displays:

- Employee ID
- Name
- Age
- Department
- Salary
- Role
- Experience for Senior Developers
- Performance Rating
- Performance
- Incentive Percentage
- Incentive
- Promotion Status

## Object-Oriented Programming Concepts

This project demonstrates the following Python OOP concepts:

- Classes and Objects
- Inheritance
- Multilevel Inheritance
- Method Overriding
- Encapsulation
- Polymorphism
- Class Methods
- Static Methods
- Abstract Methods

## Class Structure

The employee classes are organized using inheritance.

```text
Employee
|
|-- Developer
|   |
|   |-- SeniorDeveloper
|
|-- Manager
|
|-- Intern
```
Employee

Employee is the base class containing common employee attributes and functionality.

Developer

Developer inherits from Employee and provides developer-specific work and salary behavior.

SeniorDeveloper

SeniorDeveloper inherits from Developer.

It additionally stores:

Experience
Senior developer work behavior
Senior developer salary calculation
Promotion logic
Manager

Manager inherits from Employee and provides manager-specific work, salary, and promotion behavior.

Intern
Intern inherits from Employee and provides intern-specific work, salary, and promotion behavior.

Method Overriding
Different employee roles override methods according to their responsibilities.

Class Method
The project includes a class method for performing an operation related to the Employee class rather than a particular employee object.

Static Method
The project includes a static method for performing salary validation without requiring an employee object.

Abstract Method
The base Employee class defines common behavior that is implemented by the derived employee classes.

Polymorphism
Polymorphism is demonstrated by calling the same method on different employee objects and allowing each employee role to provide its own implementation
```
Project Structure--
Employee-Management-System/
|
|-- core/
|   |-- __init__.py
|   |-- employee.py
|   |-- roles.py
|   |-- department.py
|   |-- validation.py
|   |-- data_manager.py
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

```

Core Modules

core/employee.py
Contains the base Employee class and common employee functionality.

core/roles.py
Contains the different employee role classes:

Developer
SeniorDeveloper
Manager
Intern

core/department.py
Contains department-related functionality.

core/validation.py
Contains input validation functions used to validate employee and department information.

core/data_manager.py
Handles JSON data storage and retrieval.


core/main.py
Contains the console-based Employee Management System.

The application provides a menu-driven interface for:
1. Add Department
2. Add Employee
3. Search Employee
4. Update Salary
5. Delete Employee
6. View Departments
7. Update Department
8. Delete Department
9. View Employees
10. Employee Work
11. Salary Calculation
12. Performance Rating
13. Incentive Calculation
14. Promotion
15. Employee Reports
16. Class Method
17. Static Method
18. Exit
Graphical User Interface

The graphical interface is developed using Streamlit.

The GUI provides modules for:

Dashboard
Employee Registration
Department Management
Search Employee
Salary Calculation
Performance Rating
Incentive Calculation
Promotion
Employee Reports
OOP Concepts
Employee Deletion

The GUI provides a user-friendly interface for interacting with the employee management functionality.

Data Storage
The application uses JSON files for persistent data storage.

Employee information is stored in:data/employees.json

Department information is stored in:data/departments.json

Technologies Used
Python 3
Streamlit
JSON
Object-Oriented Programming
Git
GitHub

Install Streamlit using:pip install streamlit

Installation
Clone the repository:git clone https://github.com/ajithabhiram/Employee-Management-System.git

Running the Console Application
Run the core application using:python core/main.py

Running the GUI Application
Run the Streamlit application using:streamlit run gui/app.py

Project Objective

The main objective of this project is to apply Python programming and Object-Oriented Programming concepts to a practical real-world Employee Management System.

The project combines:

Python OOP
Role-based employee behavior
Input validation
Salary calculation
Performance evaluation
Incentive calculation
Promotion rules
JSON data persistence
Streamlit GUI

The project demonstrates how a Python core application can be combined with a graphical interface and persistent data storage to create a complete management system.

Author
Abhiram Ajith

GitHub:
https://github.com/ajithabhiram

Repository
https://github.com/ajithabhiram/Employee-Management-System
