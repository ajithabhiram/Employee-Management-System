from employee import Employee
from department import Department

from roles import (
    Developer,
    SeniorDeveloper,
    Manager,
    Intern
)

from validation import (
    get_positive_integer,
    get_age,
    get_positive_float,
    get_name,
    get_rating,
    get_experience
)

from data_manager import (
    load_employees,
    save_employees,
    load_departments,
    save_departments,
    create_employee_objects
)


# ==================================================
# Find Employee
# ==================================================

def find_employee(
    employees,
    employee_id
):

    for employee in employees:

        if employee.employee_id == employee_id:

            return employee

    return None


# ==================================================
# Find Department
# ==================================================

def find_department(
    departments,
    department_id
):

    for department in departments:

        if department.department_id == department_id:

            return department

    return None


# ==================================================
# Add Department
# ==================================================

def add_department(departments):

    print(
        "\n----- Add Department -----"
    )


    department_id = get_positive_integer(
        "Enter Department ID: "
    )


    if find_department(
        departments,
        department_id
    ):

        print(
            "Department ID already exists."
        )

        return


    department_name = get_name(
        "Enter Department Name: "
    )


    department = Department(
        department_id,
        department_name
    )


    departments.append(
        department
    )


    save_departments(
        departments
    )


    print(
        "Department added successfully."
    )


# ==================================================
# Add Employee
# ==================================================

def add_employee(
    employees,
    departments
):

    print(
        "\n----- Add Employee -----"
    )


    if not departments:

        print(
            "Please add a department first."
        )

        return


    employee_id = get_positive_integer(
        "Enter Employee ID: "
    )


    if find_employee(
        employees,
        employee_id
    ):

        print(
            "Employee ID already exists."
        )

        return


    name = get_name(
        "Enter Employee Name: "
    )


    age = get_age(
        "Enter Employee Age: "
    )


    print(
        "\nAvailable Departments:"
    )


    for department in departments:

        print(
            f"{department.department_id} - "
            f"{department.department_name}"
        )


    department_id = get_positive_integer(
        "Enter Department ID: "
    )


    selected_department = find_department(
        departments,
        department_id
    )


    if selected_department is None:

        print(
            "Department not found."
        )

        return


    department = (
        selected_department.department_name
    )


    salary = get_positive_float(
        "Enter Salary: "
    )


    if not Employee.check_salary(
        salary
    ):

        print(
            "Invalid salary."
        )

        return


    print(
        "\nSelect Employee Role:"
    )

    print("1. Developer")
    print("2. Senior Developer")
    print("3. Manager")
    print("4. Intern")


    role_choice = input(
        "Enter your choice: "
    )


    if role_choice == "1":

        employee = Developer(
            employee_id,
            name,
            age,
            department,
            salary
        )


    elif role_choice == "2":

        experience = get_experience(
            "Enter Experience in years: "
        )


        employee = SeniorDeveloper(
            employee_id,
            name,
            age,
            department,
            salary,
            experience
        )


    elif role_choice == "3":

        employee = Manager(
            employee_id,
            name,
            age,
            department,
            salary
        )


    elif role_choice == "4":

        employee = Intern(
            employee_id,
            name,
            age,
            department,
            salary
        )


    else:

        print(
            "Invalid role."
        )

        return


    employees.append(
        employee
    )


    save_employees(
        employees
    )


    print(
        "Employee added successfully."
    )


# ==================================================
# Search Employee
# ==================================================

def search_employee(employees):

    print(
        "\n----- Search Employee -----"
    )


    employee_id = get_positive_integer(
        "Enter Employee ID: "
    )


    employee = find_employee(
        employees,
        employee_id
    )


    if employee is None:

        print(
            "Employee not found."
        )

        return


    employee.display_details()


# ==================================================
# Update Salary
# ==================================================

def update_salary(employees):

    print(
        "\n----- Update Salary -----"
    )


    employee_id = get_positive_integer(
        "Enter Employee ID: "
    )


    employee = find_employee(
        employees,
        employee_id
    )


    if employee is None:

        print(
            "Employee not found."
        )

        return


    print(
        f"Current Salary: "
        f"{employee.get_salary()}"
    )


    new_salary = get_positive_float(
        "Enter New Salary: "
    )


    if employee.set_salary(
        new_salary
    ):

        save_employees(
            employees
        )


# ==================================================
# Delete Employee
# ==================================================

def delete_employee(employees):

    print(
        "\n----- Delete Employee -----"
    )


    employee_id = get_positive_integer(
        "Enter Employee ID: "
    )


    employee = find_employee(
        employees,
        employee_id
    )


    if employee is None:

        print(
            "Employee not found."
        )

        return


    print(
        f"Employee Found: "
        f"{employee.name}"
    )


    confirmation = input(
        "Are you sure? (yes/no): "
    ).lower()


    if confirmation == "yes":

        employees.remove(
            employee
        )


        save_employees(
            employees
        )


        print(
            "Employee deleted successfully."
        )

    else:

        print(
            "Employee deletion cancelled."
        )


# ==================================================
# View Departments
# ==================================================

def view_departments(departments):

    print(
        "\n----- Departments -----"
    )


    if not departments:

        print(
            "No departments available."
        )

        return


    for department in departments:

        department.display_department()

        print(
            "------------------------------"
        )


# ==================================================
# Update Department
# ==================================================

def update_department(
    departments,
    employees
):

    print(
        "\n----- Update Department -----"
    )


    department_id = get_positive_integer(
        "Enter Department ID: "
    )


    department = find_department(
        departments,
        department_id
    )


    if department is None:

        print(
            "Department not found."
        )

        return


    old_name = department.department_name


    print(
        f"Current Name: {old_name}"
    )


    new_name = get_name(
        "Enter New Department Name: "
    )


    department.department_name = new_name


    for employee in employees:

        if (
            employee.department.lower()
            ==
            old_name.lower()
        ):

            employee.department = new_name


    save_departments(
        departments
    )

    save_employees(
        employees
    )


    print(
        "Department updated successfully."
    )


# ==================================================
# Delete Department
# ==================================================

def delete_department(
    departments,
    employees
):

    print(
        "\n----- Delete Department -----"
    )


    department_id = get_positive_integer(
        "Enter Department ID: "
    )


    department = find_department(
        departments,
        department_id
    )


    if department is None:

        print(
            "Department not found."
        )

        return


    print(
        f"Department Found: "
        f"{department.department_name}"
    )


    for employee in employees:

        if (
            employee.department.lower()
            ==
            department.department_name.lower()
        ):

            print(
                "Cannot delete department."
            )

            print(
                "Employees are currently "
                "assigned to this department."
            )

            return


    confirmation = input(
        "Are you sure? (yes/no): "
    ).lower()


    if confirmation == "yes":

        departments.remove(
            department
        )


        save_departments(
            departments
        )


        print(
            "Department deleted successfully."
        )

    else:

        print(
            "Department deletion cancelled."
        )


# ==================================================
# View Employees
# ==================================================

def view_employees(employees):

    print(
        "\n----- Employees -----"
    )


    if not employees:

        print(
            "No employees available."
        )

        return


    for employee in employees:

        print(
            f"Employee ID: "
            f"{employee.employee_id}"
        )

        print(
            f"Name: {employee.name}"
        )

        print(
            f"Department: "
            f"{employee.department}"
        )

        print(
            f"Role: "
            f"{employee.__class__.__name__}"
        )

        print(
            f"Salary: "
            f"{employee.get_salary()}"
        )

        print(
            "------------------------------"
        )


# ==================================================
# Employee Work
# ==================================================

def employee_work(employees):

    print(
        "\n----- Employee Work -----"
    )


    employee_id = get_positive_integer(
        "Enter Employee ID: "
    )


    employee = find_employee(
        employees,
        employee_id
    )


    if employee is None:

        print(
            "Employee not found."
        )

        return


    employee.work()


# ==================================================
# Salary Calculation
# ==================================================

def salary_calculation(employees):

    print(
        "\n----- Salary Calculation -----"
    )


    employee_id = get_positive_integer(
        "Enter Employee ID: "
    )


    employee = find_employee(
        employees,
        employee_id
    )


    if employee is None:

        print(
            "Employee not found."
        )

        return


    salary = employee.calculate_salary()


    print(
        f"Calculated Salary: {salary}"
    )


# ==================================================
# Performance Rating
# ==================================================

def performance_rating(employees):

    print(
        "\n----- Performance Rating -----"
    )


    employee_id = get_positive_integer(
        "Enter Employee ID: "
    )


    employee = find_employee(
        employees,
        employee_id
    )


    if employee is None:

        print(
            "Employee not found."
        )

        return


    rating = get_rating(
        f"Enter performance rating "
        f"for {employee.name} (1-5): "
    )


    performance = employee.performance_rating(
        rating
    )



    save_employees(
        employees
    )


    print(
        f"Performance: {performance}"
    )



# ==================================================
# Incentive Calculation
# ==================================================

def incentive_calculation(employees):

    print(
        "\n----- Incentive Calculation -----"
    )


    employee_id = get_positive_integer(
        "Enter Employee ID: "
    )


    employee = find_employee(
        employees,
        employee_id
    )


    if employee is None:

        print(
            "Employee not found."
        )

        return


    employee.calculate_incentive()


    save_employees(
        employees
    )


    print(
        f"Incentive Percentage: "
        f"{employee.incentive_percentage}%"
    )

    print(
        f"Incentive Amount: "
        f"{employee.incentive}"
    )


# ==================================================
# Promotion
# ==================================================

def promotion(employees):

    print(
        "\n----- Promotion -----"
    )

    employee_id = get_positive_integer(
        "Enter Employee ID: "
    )

    employee = find_employee(
        employees,
        employee_id
    )

    if employee is None:

        print(
            "Employee not found."
        )

        return


    if employee.rating is None:

        print(
            "Please enter performance rating first."
        )

        return


    role = employee.__class__.__name__


    # ----------------------------------------------
    # Intern
    # ----------------------------------------------

    if role == "Intern":

        if employee.rating >= 4.0:

            promotion_status = (
                "Selected for Promotion: "
                "Intern -> Developer"
            )

        else:

            promotion_status = (
                "Not Eligible for Promotion"
            )


    # ----------------------------------------------
    # Developer
    # ----------------------------------------------

    elif role == "Developer":

        if employee.rating >= 4.0:

            promotion_status = (
                "Selected for Promotion: "
                "Developer -> Senior Developer"
            )

        else:

            promotion_status = (
                "Not Eligible for Promotion"
            )


    # ----------------------------------------------
    # Senior Developer
    # ----------------------------------------------

    elif role == "SeniorDeveloper":

        if (
            employee.rating >= 4.0
            and employee.experience >= 5
        ):

            promotion_status = (
                "Selected for Promotion: "
                "Senior Developer -> Manager"
            )

        else:

            promotion_status = (
                "Not Eligible for Promotion"
            )


    # ----------------------------------------------
    # Manager
    # ----------------------------------------------

    elif role == "Manager":

        if employee.rating >= 4.5:

            promotion_status = (
                "Selected for Promotion: "
                "Manager -> Senior Manager"
            )

        else:

            promotion_status = (
                "Not Eligible for Promotion"
            )


    else:

        promotion_status = (
            "Role not recognized"
        )


    employee.promotion_status = (
        promotion_status
    )


    save_employees(
        employees
    )


    print(
        f"Promotion: "
        f"{promotion_status}"
    )


# ==================================================
# Employee Reports
# ==================================================

def employee_reports(employees):

    print(
        "\n========== EMPLOYEE REPORTS =========="
    )


    if not employees:

        print(
            "No employees available."
        )

        return


    for employee in employees:

        employee.display_report()


# ==================================================
# Class Method
# ==================================================

def class_method_demo():

    print(
        "\n----- Class Method -----"
    )


    print(
        f"Current Company: "
        f"{Employee.company}"
    )


    new_company = get_name(
        "Enter new company name: "
    )


    Employee.change_company(
        new_company
    )


    print(
        f"Updated Company: "
        f"{Employee.company}"
    )


# ==================================================
# Static Method
# ==================================================

def static_method_demo():

    print(
        "\n----- Static Method -----"
    )


    salary = get_positive_float(
        "Enter Salary to Check: "
    )


    if Employee.check_salary(
        salary
    ):

        print(
            f"{salary} is a valid salary"
        )

    else:

        print(
            f"{salary} is an invalid salary"
        )


# ==================================================
# Main
# ==================================================

def main():

    employee_data = load_employees()

    employees = create_employee_objects(
        employee_data
    )


    department_data = load_departments()

    departments = []


    for data in department_data:

        department = Department(
            data["department_id"],
            data["department_name"]
        )

        departments.append(department)


    while True:

        print(
            "\n========================================"
        )

        print("EMPLOYEE MANAGEMENT SYSTEM")

        print("========================================")

        print("1. Add Department")
        print("2. Add Employee")
        print("3. Search Employee")
        print("4. Update Salary")
        print("5. Delete Employee")
        print("6. View Departments")
        print("7. Update Department")
        print("8. Delete Department")
        print("9. View Employees")
        print("10. Employee Work")
        print("11. Salary Calculation")
        print("12. Performance Rating")
        print("13. Incentive Calculation")
        print("14. Promotion")
        print("15. Employee Reports")
        print("16. Class Method")
        print("17. Static Method")
        print("18. Exit")


        choice = input(
            "\nEnter your choice: "
        )


        if choice == "1":

            add_department(
                departments
            )


        elif choice == "2":

            add_employee(
                employees,
                departments
            )


        elif choice == "3":

            search_employee(
                employees
            )


        elif choice == "4":

            update_salary(
                employees
            )


        elif choice == "5":

            delete_employee(
                employees
            )


        elif choice == "6":

            view_departments(
                departments
            )


        elif choice == "7":

            update_department(
                departments,
                employees
            )


        elif choice == "8":

            delete_department(
                departments,
                employees
            )


        elif choice == "9":

            view_employees(
                employees
            )


        elif choice == "10":

            employee_work(
                employees
            )


        elif choice == "11":

            salary_calculation(
                employees
            )


        elif choice == "12":

            performance_rating(
                employees
            )


        elif choice == "13":

            incentive_calculation(
                employees
            )


        elif choice == "14":

            promotion(
                employees
            )


        elif choice == "15":

            employee_reports(
                employees
            )


        elif choice == "16":

            class_method_demo()


        elif choice == "17":

            static_method_demo()


        elif choice == "18":

            print(
                "Thank you for using "
                "Employee Management System."
            )

            break

        else:

            print(
                "Invalid choice."
            )

if __name__ == "__main__":
    main()