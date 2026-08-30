from abc import ABC, abstractmethod


# ==================================================
# Employee Base Class
# ==================================================

class Employee(ABC):

    company = "ABC Technologies"

    def __init__(
        self,
        employee_id,
        name,
        age,
        department,
        salary
    ):

        self.employee_id = employee_id
        self.name = name
        self.age = age
        self.department = department
        self._salary = salary

        self.rating = None
        self.performance = "Not Rated"
        self.incentive = 0
        self.incentive_percentage = 0
        self.promotion_status = "Not Available"

    # ==================================================
    # Display Details
    # ==================================================

    def display_details(self):

        print(
            f"Employee ID: {self.employee_id}"
        )

        print(
            f"Name: {self.name}"
        )

        print(
            f"Age: {self.age}"
        )

        print(
            f"Department: {self.department}"
        )

        print(
            f"Salary: {self.get_salary()}"
        )

    # ==================================================
    # Getter
    # ==================================================

    def get_salary(self):

        return self._salary

    # ==================================================
    # Setter
    # ==================================================

    def set_salary(self, new_salary):

        if new_salary <= 0:

            print(
                "Salary must be greater than 0"
            )

        else:

            self._salary = new_salary

            print(
                f"Salary updated to {self._salary}"
            )

    # ==================================================
    # Work
    # ==================================================

    def work(self):

        print(
            f"{self.name} is working"
        )

    # ==================================================
    # Abstract Method
    # ==================================================

    @abstractmethod
    def calculate_salary(self):

        pass

    # ==================================================
    # Class Method
    # ==================================================

    @classmethod
    def change_company(
        cls,
        company_name
    ):

        cls.company = company_name

    # ==================================================
    # Static Method
    # ==================================================

    @staticmethod
    def check_salary(salary):

        return salary > 0

    # ==================================================
    # Performance Rating
    # ==================================================

    def performance_rating(self, rating):

        if rating >= 4.5:

            self.performance = "Excellent"

        elif rating >= 3.5:

            self.performance = "Very Good"

        elif rating >= 2.5:

            self.performance = "Good"

        elif rating >= 1.5:

            self.performance = "Needs Improvement"

        else:

            self.performance = "Poor"

        self.rating = rating

        return self.performance

    # ==================================================
    # Incentive Calculation
    # ==================================================

    def calculate_incentive(self):

        if self.rating is None:

            print(
                "Please enter performance rating first."
            )

            return 0

        if self.rating >= 4.5:

            self.incentive_percentage = 20

        elif self.rating >= 3.5:

            self.incentive_percentage = 15

        elif self.rating >= 2.5:

            self.incentive_percentage = 10

        elif self.rating >= 1.5:

            self.incentive_percentage = 5

        else:

            self.incentive_percentage = 0

        self.incentive = (
            self.get_salary()
            * self.incentive_percentage
            / 100
        )

        return self.incentive

# ==================================================
# Promotion
# ==================================================

def promotion(self):

    if self.rating is None:

        self.promotion_status = (
            "Performance rating required"
        )

        return self.promotion_status


    role = self.__class__.__name__


    # ----------------------------------------------
    # Intern -> Developer
    # ----------------------------------------------

    if role == "Intern":

        if self.rating >= 4.0:

            self.promotion_status = (
                "Selected for Promotion: "
                "Intern -> Developer"
            )

        else:

            self.promotion_status = (
                "Not Eligible for Promotion"
            )


    # ----------------------------------------------
    # Developer -> Senior Developer
    # ----------------------------------------------

    elif role == "Developer":

        if self.rating >= 4.0:

            self.promotion_status = (
                "Selected for Promotion: "
                "Developer -> Senior Developer"
            )

        else:

            self.promotion_status = (
                "Not Eligible for Promotion"
            )


    # ----------------------------------------------
    # Senior Developer -> Manager
    # ----------------------------------------------

    elif role == "SeniorDeveloper":

        if (
            self.rating >= 4.0
            and self.experience >= 5
        ):

            self.promotion_status = (
                "Selected for Promotion: "
                "Senior Developer -> Manager"
            )

        else:

            self.promotion_status = (
                "Not Eligible for Promotion"
            )


    # ----------------------------------------------
    # Manager -> Senior Manager
    # ----------------------------------------------

    elif role == "Manager":

        if self.rating >= 4.5:

            self.promotion_status = (
                "Selected for Promotion: "
                "Manager -> Senior Manager"
            )

        else:

            self.promotion_status = (
                "Not Eligible for Promotion"
            )


    else:

        self.promotion_status = (
            "Not Eligible for Promotion"
        )


    return self.promotion_status

    # ==================================================
    # Employee Report
    # ==================================================

    def display_report(self):

        print(
            "\n------------------------------"
        )

        print(
            "       EMPLOYEE REPORT"
        )

        print(
            "------------------------------"
        )

        print(
            f"Employee ID: {self.employee_id}"
        )

        print(
            f"Name: {self.name}"
        )

        print(
            f"Age: {self.age}"
        )

        print(
            f"Department: {self.department}"
        )

        print(
            f"Salary: {self.get_salary()}"
        )

        if isinstance(
            self,
            SeniorDeveloper
        ):

            print(
                "Role: Senior Developer"
            )

            print(
                f"Experience: "
                f"{self.experience} years"
            )

        elif isinstance(
            self,
            Developer
        ):

            print(
                "Role: Developer"
            )

        elif isinstance(
            self,
            Manager
        ):

            print(
                "Role: Manager"
            )

        elif isinstance(
            self,
            Intern
        ):

            print(
                "Role: Intern"
            )

        else:

            print(
                "Role: Employee"
            )

        if self.rating is not None:

            print(
                f"Performance Rating: "
                f"{self.rating}"
            )

            print(
                f"Performance: "
                f"{self.performance}"
            )

        print(
            f"Incentive Percentage: "
            f"{self.incentive_percentage}%"
        )

        print(
            f"Incentive: "
            f"{self.incentive}"
        )

        print(
            f"Promotion: "
            f"{self.promotion_status}"
        )

        print(
            "------------------------------"
        )


# ==================================================
# Developer
# ==================================================

class Developer(Employee):

    def developer_work(self):

        print(
            f"{self.name} works on "
            f"software development"
        )

    # Method Overriding

    def work(self):

        print(
            f"{self.name} is developing software"
        )

    # Method Overriding

    def calculate_salary(self):

        allowance = 10000

        total_salary = (
            self.get_salary()
            + allowance
        )

        return total_salary


# ==================================================
# Senior Developer
# ==================================================

class SeniorDeveloper(Developer):

    def __init__(
        self,
        employee_id,
        name,
        age,
        department,
        salary,
        experience
    ):

        super().__init__(
            employee_id,
            name,
            age,
            department,
            salary
        )

        self.experience = experience

    def display_senior_details(self):

        print(
            f"Experience: "
            f"{self.experience} years"
        )

    # Method Overriding

    def work(self):

        print(
            f"{self.name} is leading "
            f"the development team"
        )

    # Method Overriding

    def calculate_salary(self):

        allowance = 20000

        total_salary = (
            self.get_salary()
            + allowance
        )

        return total_salary


# ==================================================
# Manager
# ==================================================

class Manager(Employee):

    def manager_work(self):

        print(
            f"{self.name} manages the team"
        )

    # Method Overriding

    def work(self):

        print(
            f"{self.name} is managing the team"
        )

    # Method Overriding

    def calculate_salary(self):

        allowance = 15000

        total_salary = (
            self.get_salary()
            + allowance
        )

        return total_salary


# ==================================================
# Intern
# ==================================================

class Intern(Employee):

    def intern_work(self):

        print(
            f"{self.name} is working as an intern"
        )

    # Method Overriding

    def work(self):

        print(
            f"{self.name} is learning "
            f"and assisting the team"
        )

    # Method Overriding

    def calculate_salary(self):

        return self.get_salary()