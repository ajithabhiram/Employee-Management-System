import json
import os

from roles import (
    Developer,
    SeniorDeveloper,
    Manager,
    Intern
)


# ==================================================
# Project Paths
# ==================================================

BASE_DIR = os.path.dirname(
    os.path.dirname(
        os.path.abspath(__file__)
    )
)

DATA_DIR = os.path.join(
    BASE_DIR,
    "data"
)

EMPLOYEE_FILE = os.path.join(
    DATA_DIR,
    "employees.json"
)

DEPARTMENT_FILE = os.path.join(
    DATA_DIR,
    "departments.json"
)


# ==================================================
# Create Data Folder
# ==================================================

def create_data_folder():

    if not os.path.exists(DATA_DIR):

        os.makedirs(DATA_DIR)


# ==================================================
# Department Data
# ==================================================

def load_departments():

    create_data_folder()

    if not os.path.exists(
        DEPARTMENT_FILE
    ):

        return []

    try:

        with open(
            DEPARTMENT_FILE,
            "r"
        ) as file:

            return json.load(file)

    except (
        json.JSONDecodeError,
        FileNotFoundError
    ):

        return []


def save_departments(departments):

    create_data_folder()

    data = []

    for department in departments:

        data.append(
            {
                "department_id":
                    department.department_id,

                "department_name":
                    department.department_name
            }
        )

    with open(
        DEPARTMENT_FILE,
        "w"
    ) as file:

        json.dump(
            data,
            file,
            indent=4
        )


# ==================================================
# Employee Data
# ==================================================

def load_employees():

    create_data_folder()

    if not os.path.exists(
        EMPLOYEE_FILE
    ):

        return []

    try:

        with open(
            EMPLOYEE_FILE,
            "r"
        ) as file:

            return json.load(file)

    except (
        json.JSONDecodeError,
        FileNotFoundError
    ):

        return []


def save_employees(employees):

    create_data_folder()

    data = []

    for employee in employees:

        employee_data = {

            "employee_id":
                employee.employee_id,

            "name":
                employee.name,

            "age":
                employee.age,

            "department":
                employee.department,

            "salary":
                employee.get_salary(),

            "role":
                employee.__class__.__name__,

            "rating":
                employee.rating,

            "performance":
                employee.performance,

            "incentive":
                employee.incentive,

            "incentive_percentage":
                employee.incentive_percentage,

            "promotion_status":
                employee.promotion_status
        }


        # ------------------------------------------
        # Save experience for Senior Developer
        # ------------------------------------------

        if (
            employee.__class__.__name__
            == "SeniorDeveloper"
        ):

            employee_data["experience"] = (
                employee.experience
            )


        data.append(
            employee_data
        )


    with open(
        EMPLOYEE_FILE,
        "w"
    ) as file:

        json.dump(
            data,
            file,
            indent=4
        )


# ==================================================
# Create Employee Objects
# ==================================================

def create_employee_objects(employee_data):

    employees = []

    for data in employee_data:

        role = data.get(
            "role",
            ""
        )


        # ------------------------------------------
        # Developer
        # ------------------------------------------

        if role == "Developer":

            employee = Developer(
                data["employee_id"],
                data["name"],
                data["age"],
                data["department"],
                data["salary"]
            )


        # ------------------------------------------
        # Senior Developer
        # ------------------------------------------

        elif role == "SeniorDeveloper":

            employee = SeniorDeveloper(
                data["employee_id"],
                data["name"],
                data["age"],
                data["department"],
                data["salary"],
                data.get(
                    "experience",
                    0
                )
            )


        # ------------------------------------------
        # Manager
        # ------------------------------------------

        elif role == "Manager":

            employee = Manager(
                data["employee_id"],
                data["name"],
                data["age"],
                data["department"],
                data["salary"]
            )


        # ------------------------------------------
        # Intern
        # ------------------------------------------

        elif role == "Intern":

            employee = Intern(
                data["employee_id"],
                data["name"],
                data["age"],
                data["department"],
                data["salary"]
            )


        else:

            print(
                "Unknown employee role:",
                role
            )

            continue


        # ------------------------------------------
        # Restore saved employee data
        # ------------------------------------------

        employee.rating = data.get(
            "rating"
        )

        employee.performance = data.get(
            "performance",
            ""
        )

        employee.incentive = data.get(
            "incentive",
            0
        )

        employee.incentive_percentage = data.get(
            "incentive_percentage",
            0
        )

        employee.promotion_status = data.get(
            "promotion_status",
            "Not Eligible"
        )


        # ------------------------------------------
        # Restore Senior Developer experience
        # ------------------------------------------

        if role == "SeniorDeveloper":

            employee.experience = data.get(
                "experience",
                0
            )


        employees.append(
            employee
        )


    return employees