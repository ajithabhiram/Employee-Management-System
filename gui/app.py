import sys
import os
import io
from contextlib import redirect_stdout


# ==================================================
# CORE PATH
# ==================================================

project_root = os.path.dirname(
    os.path.dirname(
        os.path.abspath(__file__)
    )
)

core_folder = os.path.join(
    project_root,
    "core"
)

for module_path in (project_root, core_folder):
    if module_path not in sys.path:
        sys.path.insert(0, module_path)


# ==================================================
# IMPORTS
# ==================================================

import streamlit as st

from core.employee import Employee
from core.department import Department

from core.roles import (
    Developer,
    SeniorDeveloper,
    Manager,
    Intern
)

from core.data_manager import (
    load_employees,
    load_departments,
    save_employees,
    save_departments,
    create_employee_objects
)


# ==================================================
# PAGE SETTINGS
# ==================================================

st.set_page_config(
    page_title="Employee Management System",
    page_icon="🏢",
    layout="wide"
)


# ==================================================
# TITLE
# ==================================================

st.title("🏢 Employee Management System")

st.write(
    "Employee management system using Python OOP "
    "and Streamlit."
)


# ==================================================
# DATA FUNCTIONS
# ==================================================

def get_employees():

    employee_data = load_employees()

    employees = create_employee_objects(
        employee_data
    )

    return employees


def get_departments():

    department_data = load_departments()

    departments = []

    for data in department_data:

        department = Department(
            data["department_id"],
            data["department_name"]
        )

        departments.append(
            department
        )

    return departments


def find_employee(
    employees,
    employee_id
):

    for employee in employees:

        if employee.employee_id == employee_id:
            return employee

    return None


def find_department(
    departments,
    department_id
):

    for department in departments:

        if department.department_id == department_id:
            return department

    return None


def get_role_name(employee):

    if isinstance(employee, SeniorDeveloper):

        return "Senior Developer"

    elif isinstance(employee, Developer):

        return "Developer"

    elif isinstance(employee, Manager):

        return "Manager"

    elif isinstance(employee, Intern):

        return "Intern"

    return "Employee"


# ==================================================
# SIDEBAR
# ==================================================

st.sidebar.title("📌 Navigation")

page = st.sidebar.radio(
    "Select Module",
    [
        "🏠 Dashboard",
        "👤 Employee Registration",
        "🏢 Department Management",
        "🔍 Search Employee",
        "💰 Salary Calculation",
        "⭐ Performance Rating",
        "🎁 Incentive Calculation",
        "📈 Promotion",
        "📋 Employee Reports",
        "🛠️ OOP Concepts"
    ]
)


# ==================================================
# DASHBOARD
# ==================================================

if page == "🏠 Dashboard":

    st.header("🏠 Dashboard")

    employees = get_employees()
    departments = get_departments()

    col1, col2, col3 = st.columns(3)

    with col1:

        st.metric(
            "Total Employees",
            len(employees)
        )

    with col2:

        st.metric(
            "Total Departments",
            len(departments)
        )

    with col3:

        developers = 0

        for employee in employees:

            if isinstance(
                employee,
                Developer
            ):

                developers += 1

        st.metric(
            "Developers",
            developers
        )


    st.divider()

    st.subheader("System Features")

    col1, col2 = st.columns(2)

    with col1:

        st.write("👤 Employee Registration")
        st.write("🏢 Department Management")
        st.write("🔍 Employee Search")
        st.write("💰 Salary Management")
        st.write("⭐ Performance Rating")

    with col2:

        st.write("🎁 Incentive Calculation")
        st.write("📈 Promotion")
        st.write("📋 Employee Reports")
        st.write("🛠️ OOP Concepts")


# ==================================================
# EMPLOYEE REGISTRATION
# ==================================================

elif page == "👤 Employee Registration":

    st.header("👤 Employee Registration")

    departments = get_departments()
    employees = get_employees()


    if not departments:

        st.warning(
            "Please add a department before "
            "registering an employee."
        )

    else:

        st.write(
            "Enter employee details below."
        )


        employee_id = st.number_input(
            "Employee ID",
            min_value=1,
            step=1
        )


        name = st.text_input(
            "Employee Name"
        )


        age = st.number_input(
            "Age",
            min_value=18,
            max_value=60,
            step=1
        )


        department_names = []

        for department in departments:

            department_names.append(
                department.department_name
            )


        selected_department = st.selectbox(
            "Department",
            department_names
        )


        salary = st.number_input(
            "Salary",
            min_value=1.0,
            step=1000.0
        )


        role = st.selectbox(
            "Employee Role",
            [
                "Developer",
                "Senior Developer",
                "Manager",
                "Intern"
            ]
        )


        experience = 0

        if role == "Senior Developer":

            experience = st.number_input(
                "Experience in Years",
                min_value=0,
                step=1
            )


        if st.button(
            "➕ Register Employee",
            use_container_width=True
        ):

            if not name.strip():

                st.error(
                    "Employee name cannot be empty."
                )

            elif find_employee(
                employees,
                int(employee_id)
            ):

                st.error(
                    "Employee ID already exists."
                )

            elif not Employee.check_salary(
                salary
            ):

                st.error(
                    "Salary must be greater than 0."
                )

            else:

                if role == "Developer":

                    employee = Developer(
                        int(employee_id),
                        name,
                        int(age),
                        selected_department,
                        salary
                    )


                elif role == "Senior Developer":

                    employee = SeniorDeveloper(
                        int(employee_id),
                        name,
                        int(age),
                        selected_department,
                        salary,
                        int(experience)
                    )


                elif role == "Manager":

                    employee = Manager(
                        int(employee_id),
                        name,
                        int(age),
                        selected_department,
                        salary
                    )


                else:

                    employee = Intern(
                        int(employee_id),
                        name,
                        int(age),
                        selected_department,
                        salary
                    )


                employees.append(
                    employee
                )



                save_employees(
                    employees
                )

                st.success(
                    "Employee registered successfully."
                )


# ==================================================
# DEPARTMENT MANAGEMENT
# ==================================================

elif page == "🏢 Department Management":

    st.header("🏢 Department Management")

    departments = get_departments()
    employees = get_employees()


    # ------------------------------------------------
    # ADD DEPARTMENT
    # ------------------------------------------------

    st.subheader("➕ Add Department")

    department_id = st.number_input(
        "Department ID",
        min_value=1,
        step=1,
        key="add_department_id"
    )


    department_name = st.text_input(
        "Department Name",
        key="add_department_name"
    )


    if st.button(
        "Add Department",
        use_container_width=True
    ):

        if find_department(
            departments,
            int(department_id)
        ):

            st.error(
                "Department ID already exists."
            )

        elif not department_name.strip():

            st.error(
                "Department name cannot be empty."
            )

        else:

            department = Department(
                int(department_id),
                department_name
            )

            departments.append(
                department
            )

            save_departments(
                departments
            )

            st.success(
                "Department added successfully."
            )


    st.divider()


    # ------------------------------------------------
    # VIEW DEPARTMENTS
    # ------------------------------------------------

    st.subheader("📋 Departments")


    if not departments:

        st.info(
            "No departments available."
        )

    else:

        for department in departments:

            st.write(
                f"**ID:** {department.department_id}"
            )

            st.write(
                f"**Name:** "
                f"{department.department_name}"
            )

            st.divider()


    # ------------------------------------------------
    # UPDATE DEPARTMENT
    # ------------------------------------------------

    st.subheader("✏️ Update Department")


    if departments:

        update_options = {}

        for department in departments:

            update_options[
                f"{department.department_id} - "
                f"{department.department_name}"
            ] = department.department_id


        selected_update = st.selectbox(
            "Select Department",
            list(update_options.keys()),
            key="update_department_select"
        )


        new_department_name = st.text_input(
            "New Department Name"
        )


        if st.button(
            "Update Department"
        ):

            selected_id = update_options[
                selected_update
            ]

            department = find_department(
                departments,
                selected_id
            )


            if not new_department_name.strip():

                st.error(
                    "Department name cannot be empty."
                )

            else:

                old_name = (
                    department.department_name
                )

                department.department_name = (
                    new_department_name
                )


                for employee in employees:

                    if (
                        employee.department.lower()
                        ==
                        old_name.lower()
                    ):

                        employee.department = (
                            new_department_name
                        )


                save_departments(
                    departments
                )

                save_employees(
                    employees
                )

                st.success(
                    "Department updated successfully."
                )


    st.divider()


    # ------------------------------------------------
    # DELETE DEPARTMENT
    # ------------------------------------------------

    st.subheader("🗑️ Delete Department")


    if departments:

        delete_options = {}

        for department in departments:

            delete_options[
                f"{department.department_id} - "
                f"{department.department_name}"
            ] = department.department_id


        selected_delete = st.selectbox(
            "Select Department",
            list(delete_options.keys()),
            key="delete_department_select"
        )


        if st.button(
            "Delete Department"
        ):

            selected_id = delete_options[
                selected_delete
            ]

            department = find_department(
                departments,
                selected_id
            )


            employee_found = False


            for employee in employees:

                if (
                    employee.department.lower()
                    ==
                    department.department_name.lower()
                ):

                    employee_found = True
                    break


            if employee_found:

                st.error(
                    "Cannot delete department."
                )

                st.warning(
                    "Employees are currently "
                    "assigned to this department."
                )

            else:

                departments.remove(
                    department
                )

                save_departments(
                    departments
                )

                st.success(
                    "Department deleted successfully."
                )


# ==================================================
# SEARCH EMPLOYEE
# ==================================================

elif page == "🔍 Search Employee":

    st.header("🔍 Search Employee")

    employees = get_employees()


    employee_id = st.number_input(
        "Enter Employee ID",
        min_value=1,
        step=1
    )


    if st.button(
        "Search Employee",
        use_container_width=True
    ):

        employee = find_employee(
            employees,
            int(employee_id)
        )


        if employee is None:

            st.error(
                "Employee not found."
            )

        else:

            st.success(
                "Employee found."
            )


            st.write(
                f"**Employee ID:** "
                f"{employee.employee_id}"
            )

            st.write(
                f"**Name:** {employee.name}"
            )

            st.write(
                f"**Age:** {employee.age}"
            )

            st.write(
                f"**Department:** "
                f"{employee.department}"
            )

            st.write(
                f"**Salary:** "
                f"{employee.get_salary()}"
            )

            st.write(
                f"**Role:** "
                f"{get_role_name(employee)}"
            )

            if isinstance(
                employee,
                SeniorDeveloper
            ):

                st.write(
                    f"**Experience:** "
                    f"{employee.experience} years"
                )


# ==================================================
# SALARY CALCULATION
# ==================================================

elif page == "💰 Salary Calculation":

    st.header("💰 Salary Calculation")

    employees = get_employees()


    if not employees:

        st.info(
            "No employees available."
        )

    else:

        employee_options = {}

        for employee in employees:

            employee_options[
                f"{employee.employee_id} - "
                f"{employee.name}"
            ] = employee.employee_id


        selected = st.selectbox(
            "Select Employee",
            list(employee_options.keys())
        )


        if st.button(
            "Calculate Salary",
            use_container_width=True
        ):

            employee_id = employee_options[
                selected
            ]

            employee = find_employee(
                employees,
                employee_id
            )


            output = io.StringIO()


            with redirect_stdout(output):

                result = employee.calculate_salary()


            printed_output = output.getvalue()


            st.write(
                f"**Employee:** "
                f"{employee.name}"
            )

            st.write(
                f"**Role:** "
                f"{get_role_name(employee)}"
            )

            st.write(
                f"**Basic Salary:** "
                f"₹{employee.get_salary():,.2f}"
            )


            if result is not None:

                st.success(
                    f"Calculated Salary: "
                    f"₹{result:,.2f}"
                )

            elif printed_output:

                st.success(
                    printed_output.strip()
                )

            else:

                st.info(
                    "Salary calculation completed."
                )


# ==================================================
# PERFORMANCE RATING
# ==================================================

elif page == "⭐ Performance Rating":

    st.header("⭐ Performance Rating")

    employees = get_employees()

    if not employees:

        st.info(
            "No employees available."
        )

    else:

        employee_options = {}

        for employee in employees:

            employee_options[
                f"{employee.employee_id} - "
                f"{employee.name}"
            ] = employee.employee_id

        selected = st.selectbox(
            "Select Employee",
            list(employee_options.keys())
        )

        rating = st.number_input(
            "Enter Performance Rating (1-5)",
            min_value=1.0,
            max_value=5.0,
            value=3.0,
            step=0.1
        )

        st.caption(
            "3+ = Needs More Improvement | "
            "4+ = Getting Close | "
            "4.5+ = Selected"
        )

        if st.button(
            "⭐ Save Rating",
            use_container_width=True
        ):

            employee_id = employee_options[
                selected
            ]

            employee = find_employee(
                employees,
                employee_id
            )

            employee.performance_rating(
                rating
            )

            save_employees(
                employees
            )

            st.success(
                f"Performance: "
                f"{employee.performance}"
            )


# ==================================================
# INCENTIVE CALCULATION
# ==================================================

elif page == "🎁 Incentive Calculation":

    st.header("🎁 Incentive Calculation")

    employees = get_employees()


    if not employees:

        st.info(
            "No employees available."
        )

    else:

        employee_options = {}

        for employee in employees:

            employee_options[
                f"{employee.employee_id} - "
                f"{employee.name}"
            ] = employee.employee_id


        selected = st.selectbox(
            "Select Employee",
            list(employee_options.keys())
        )


        if st.button(
            "Calculate Incentive",
            use_container_width=True
        ):

            employee_id = employee_options[
                selected
            ]

            employee = find_employee(
                employees,
                employee_id
            )


            if employee.rating is None:

                st.warning(
                    "Please enter a performance "
                    "rating first."
                )

            else:

                employee.calculate_incentive()


                save_employees(
                    employees
                )


                st.success(
                    f"Incentive Percentage: "
                    f"{employee.incentive_percentage}%"
                )


                st.write(
                    f"**Salary:** "
                    f"₹{employee.get_salary():,.2f}"
                )

                st.write(
                    f"**Incentive:** "
                    f"₹{employee.incentive:,.2f}"
                )


# ==================================================
# PROMOTION
# ==================================================

elif page == "📈 Promotion":

    st.header("📈 Promotion")

    employee_data = load_employees()

    employees = create_employee_objects(
        employee_data
    )

    if not employee_data:

        st.info(
            "No employees available."
        )

    else:

        employee_options = {}

        for data in employee_data:

            employee_options[
                f"{data['employee_id']} - "
                f"{data['name']}"
            ] = data["employee_id"]


        selected = st.selectbox(
            "Select Employee",
            list(employee_options.keys())
        )


        if st.button(
            "Check Promotion",
            use_container_width=True
        ):

            employee_id = employee_options[
                selected
            ]


            # ------------------------------------------
            # Find employee data
            # ------------------------------------------

            selected_data = None

            for data in employee_data:

                if (
                    data["employee_id"]
                    == employee_id
                ):

                    selected_data = data
                    break


            if selected_data is None:

                st.error(
                    "Employee not found."
                )

            else:

                name = selected_data[
                    "name"
                ]

                role = selected_data.get(
                    "role",
                    "Employee"
                )

                rating = selected_data.get(
                    "rating"
                )


                # ------------------------------------------
                # Promotion Result
                # ------------------------------------------

                st.subheader(
                    "Promotion Result"
                )

                st.write(
                    f"**Employee:** {name}"
                )


                # ==========================================
                # DEVELOPER
                # ==========================================

                if role == "Developer":

                    current_role = (
                        "Developer"
                    )

                    promotion_path = (
                        "Developer → "
                        "Senior Developer"
                    )

                    required = (
                        "Performance Rating ≥ 4.0"
                    )


                    st.write(
                        f"**Current Role:** "
                        f"{current_role}"
                    )

                    if rating is None:

                        st.warning(
                            "Please enter a performance "
                            "rating first."
                        )

                    else:

                        st.write(
                            f"**Performance Rating:** "
                            f"{rating}"
                        )

                        st.write(
                            f"**Promotion Path:** "
                            f"{promotion_path}"
                        )

                        st.write(
                            f"**Required:** "
                            f"{required}"
                        )


                        if rating >= 4.0:

                            promotion_status = (
                                "Selected for Promotion: "
                                "Developer → "
                                "Senior Developer"
                            )

                            st.success(
                                f"✅ {promotion_status}"
                            )

                        else:

                            promotion_status = (
                                "Not Eligible for Promotion"
                            )

                            st.warning(
                                f"❌ {promotion_status}"
                            )


                # ==========================================
                # SENIOR DEVELOPER
                # ==========================================

                elif role == "SeniorDeveloper":

                    current_role = (
                        "Senior Developer"
                    )

                    promotion_path = (
                        "Senior Developer → Manager"
                    )

                    required = (
                        "Performance Rating ≥ 4.0 "
                        "and Experience ≥ 5 years"
                    )


                    st.write(
                        f"**Current Role:** "
                        f"{current_role}"
                    )


                    if rating is None:

                        st.warning(
                            "Please enter a performance "
                            "rating first."
                        )

                    else:

                        experience = selected_data.get(
                            "experience",
                            0
                        )


                        st.write(
                            f"**Performance Rating:** "
                            f"{rating}"
                        )

                        st.write(
                            f"**Experience:** "
                            f"{experience} years"
                        )

                        st.write(
                            f"**Promotion Path:** "
                            f"{promotion_path}"
                        )

                        st.write(
                            f"**Required:** "
                            f"{required}"
                        )


                        if (
                            rating >= 4.0
                            and experience >= 5
                        ):

                            promotion_status = (
                                "Selected for Promotion: "
                                "Senior Developer → Manager"
                            )

                            st.success(
                                f"✅ {promotion_status}"
                            )

                        else:

                            promotion_status = (
                                "Not Eligible for Promotion"
                            )

                            st.warning(
                                f"❌ {promotion_status}"
                            )


                # ==========================================
                # MANAGER
                # ==========================================

                elif role == "Manager":

                    current_role = (
                        "Manager"
                    )

                    promotion_path = (
                        "Manager → Senior Manager"
                    )

                    required = (
                        "Performance Rating ≥ 4.5"
                    )


                    st.write(
                        f"**Current Role:** "
                        f"{current_role}"
                    )


                    if rating is None:

                        st.warning(
                            "Please enter a performance "
                            "rating first."
                        )

                    else:

                        st.write(
                            f"**Performance Rating:** "
                            f"{rating}"
                        )

                        st.write(
                            f"**Promotion Path:** "
                            f"{promotion_path}"
                        )

                        st.write(
                            f"**Required:** "
                            f"{required}"
                        )


                        if rating >= 4.5:

                            promotion_status = (
                                "Selected for Promotion: "
                                "Manager → "
                                "Senior Manager"
                            )

                            st.success(
                                f"✅ {promotion_status}"
                            )

                        else:

                            promotion_status = (
                                "Not Eligible for Promotion"
                            )

                            st.warning(
                                f"❌ {promotion_status}"
                            )


                # ==========================================
                # INTERN
                # ==========================================

                elif role == "Intern":

                    current_role = (
                        "Intern"
                    )

                    promotion_path = (
                        "Intern → Developer"
                    )

                    required = (
                        "Performance Rating ≥ 4.0"
                    )


                    st.write(
                        f"**Current Role:** "
                        f"{current_role}"
                    )


                    if rating is None:

                        st.warning(
                            "Please enter a performance "
                            "rating first."
                        )

                    else:

                        st.write(
                            f"**Performance Rating:** "
                            f"{rating}"
                        )

                        st.write(
                            f"**Promotion Path:** "
                            f"{promotion_path}"
                        )

                        st.write(
                            f"**Required:** "
                            f"{required}"
                        )


                        if rating >= 4.0:

                            promotion_status = (
                                "Selected for Promotion: "
                                "Intern → Developer"
                            )

                            st.success(
                                f"✅ {promotion_status}"
                            )

                        else:

                            promotion_status = (
                                "Not Eligible for Promotion"
                            )

                            st.warning(
                                f"❌ {promotion_status}"
                            )


                # ==========================================
                # UNKNOWN ROLE
                # ==========================================

                else:

                    st.error(
                        f"Unknown employee role: {role}"
                    )

# ==================================================
# EMPLOYEE REPORTS
# ==================================================

elif page == "📋 Employee Reports":

    st.header("📋 Employee Reports")

    employee_data = load_employees()


    if not employee_data:

        st.info(
            "No employees available."
        )

    else:

        for data in employee_data:

            employee_id = data.get(
                "employee_id"
            )

            name = data.get(
                "name",
                "Unknown"
            )

            age = data.get(
                "age",
                "N/A"
            )

            department = data.get(
                "department",
                "N/A"
            )

            salary = data.get(
                "salary",
                0
            )

            role = data.get(
                "role",
                "Employee"
            )

            rating = data.get(
                "rating"
            )

            performance = data.get(
                "performance",
                "Not Rated"
            )

            incentive_percentage = data.get(
                "incentive_percentage",
                0
            )

            incentive = data.get(
                "incentive",
                0
            )

            promotion_status = data.get(
                "promotion_status",
                "Not Available"
            )


            # ------------------------------------------
            # Convert role name for display
            # ------------------------------------------

            if role == "SeniorDeveloper":

                display_role = (
                    "Senior Developer"
                )

            elif role == "Developer":

                display_role = "Developer"

            elif role == "Manager":

                display_role = "Manager"

            elif role == "Intern":

                display_role = "Intern"

            else:

                display_role = role


            # ------------------------------------------
            # Employee Report
            # ------------------------------------------

            with st.expander(
                f"{employee_id} - {name}"
            ):

                st.write(
                    f"**Employee ID:** "
                    f"{employee_id}"
                )

                st.write(
                    f"**Name:** "
                    f"{name}"
                )

                st.write(
                    f"**Age:** "
                    f"{age}"
                )

                st.write(
                    f"**Department:** "
                    f"{department}"
                )

                st.write(
                    f"**Salary:** "
                    f"₹{salary:,.2f}"
                )

                st.write(
                    f"**Role:** "
                    f"{display_role}"
                )


                # ------------------------------------------
                # Experience
                # ------------------------------------------

                if role == "SeniorDeveloper":

                    experience = data.get(
                        "experience",
                        0
                    )

                    st.write(
                        f"**Experience:** "
                        f"{experience} years"
                    )


                # ------------------------------------------
                # Performance
                # ------------------------------------------

                if rating is not None:

                    st.write(
                        f"**Performance Rating:** "
                        f"{rating}"
                    )

                    st.write(
                        f"**Performance:** "
                        f"{performance}"
                    )


                # ------------------------------------------
                # Incentive
                # ------------------------------------------

                st.write(
                    f"**Incentive Percentage:** "
                    f"{incentive_percentage}%"
                )

                st.write(
                    f"**Incentive:** "
                    f"₹{incentive:,.2f}"
                )


                # ------------------------------------------
                # Promotion
                # ------------------------------------------



        st.divider()


        # ------------------------------------------------
        # DELETE EMPLOYEE
        # ------------------------------------------------

        st.subheader("🗑️ Delete Employee")

        # Reload employee objects for the delete operation.
        # Employee Reports uses employee_data, so this section
        # must create its own employees list.
        employees = create_employee_objects(
            load_employees()
        )

        employee_options = {}

        for employee in employees:

            employee_options[
                f"{employee.employee_id} - "
                f"{employee.name}"
            ] = employee.employee_id


        selected_delete = st.selectbox(
            "Select Employee to Delete",
            list(employee_options.keys()),
            key="delete_employee_select"
        )


        if st.button(
            "Delete Employee",
            use_container_width=True
        ):

            employee_id = employee_options[
                selected_delete
            ]

            employee = find_employee(
                employees,
                employee_id
            )


            if employee:

                employees.remove(
                    employee
                )

                save_employees(
                    employees
                )

                st.success(
                    "Employee deleted successfully."
                )


# ==================================================
# OOP CONCEPTS
# ==================================================

elif page == "🛠️ OOP Concepts":

    st.header("🛠️ OOP Concepts Demonstration")

    st.write(
        "This section demonstrates the OOP concepts "
        "used in the Employee Management System."
    )


    # ==================================================
    # CLASS METHOD
    # ==================================================

    st.subheader("1️⃣ Class Method")

    st.write(
        "Used to change the company name for "
        "the Employee class."
    )


    st.write(
        f"**Current Company:** "
        f"{Employee.company}"
    )


    new_company = st.text_input(
        "Enter New Company Name",
        key="company_name"
    )


    if st.button(
        "Change Company",
        use_container_width=True
    ):

        if new_company.strip():

            Employee.change_company(
                new_company
            )

            st.success(
                f"Updated Company: "
                f"{Employee.company}"
            )

        else:

            st.error(
                "Company name cannot be empty."
            )


    st.divider()


    # ==================================================
    # STATIC METHOD
    # ==================================================

    st.subheader("2️⃣ Static Method")

    st.write(
        "Used to validate whether a salary "
        "is greater than zero."
    )


    test_salary = st.number_input(
        "Enter Salary to Validate",
        min_value=0.0,
        step=1000.0,
        key="static_salary"
    )


    if st.button(
        "Check Salary",
        use_container_width=True
    ):

        if Employee.check_salary(
            test_salary
        ):

            st.success(
                f"{test_salary} is a valid salary"
            )

        else:

            st.error(
                f"{test_salary} is an invalid salary"
            )


    st.divider()


    # ==================================================
    # INHERITANCE
    # ==================================================

    st.subheader("3️⃣ Inheritance")

    st.write(
        "Employee is the base class. "
        "Developer, Manager and Intern inherit "
        "from Employee."
    )


    # ==================================================
    # MULTILEVEL INHERITANCE
    # ==================================================

    st.subheader("4️⃣ Multilevel Inheritance")

    st.write(
        "SeniorDeveloper inherits from Developer, "
        "and Developer inherits from Employee."
    )


    st.code(
        "Employee\n"
        "   ↓\n"
        "Developer\n"
        "   ↓\n"
        "SeniorDeveloper"
    )


    # ==================================================
    # HIERARCHICAL INHERITANCE
    # ==================================================

    st.subheader("5️⃣ Hierarchical Inheritance")

    st.write(
        "Developer, Manager and Intern inherit "
        "from the Employee base class."
    )


    st.code(
        "              Employee\n"
        "             /    |    \\\n"
        "            /     |     \\\n"
        "     Developer  Manager  Intern"
    )


    # ==================================================
    # ABSTRACTION
    # ==================================================

    st.subheader("6️⃣ Abstraction")

    st.write(
        "Employee contains the abstract "
        "calculate_salary() method."
    )


    st.code(
        "@abstractmethod\n"
        "def calculate_salary(self):\n"
        "    pass"
    )


    # ==================================================
    # METHOD OVERRIDING
    # ==================================================

    st.subheader("7️⃣ Method Overriding")

    st.write(
        "Each role provides its own implementation "
        "of work() and calculate_salary()."
    )


    # ==================================================
    # POLYMORPHISM
    # ==================================================

    st.subheader("8️⃣ Polymorphism")

    st.write(
        "The same method name such as work() "
        "behaves differently depending on the "
        "employee object."
    )


    employees = get_employees()


    if employees:

        if st.button(
            "Demonstrate Polymorphism"
        ):

            for employee in employees:

                output = io.StringIO()

                with redirect_stdout(output):

                    employee.work()

                result = output.getvalue()


                if result:

                    st.write(
                        f"**{get_role_name(employee)}:** "
                        f"{result.strip()}"
                    )