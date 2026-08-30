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
