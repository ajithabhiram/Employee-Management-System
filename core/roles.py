from employee import Employee


# ==================================================
# Developer
# ==================================================

class Developer(Employee):

    def work(self):

        print(
            f"{self.name} is developing software."
        )


    def calculate_salary(self):

        allowance = 10000

        return (
            self.get_salary()
            +
            allowance
        )


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


    def work(self):

        print(
            f"{self.name} is leading "
            f"the development team."
        )


    def calculate_salary(self):

        allowance = 20000

        return (
            self.get_salary()
            +
            allowance
        )


    def promotion(self):

        if self.rating is None:

            self.promotion_status = (
                "Performance Not Rated"
            )

        elif (
            self.rating >= 4.5
            and
            self.experience >= 5
        ):

            self.promotion_status = (
                "Selected for Promotion - Manager"
            )

        elif self.rating >= 4:

            self.promotion_status = (
                "Getting Close to Promotion - "
                "Keep Learning"
            )

        elif self.rating >= 3:

            self.promotion_status = (
                "Needs More Improvement "
                "for Promotion"
            )

        else:

            self.promotion_status = (
                "Not Ready for Promotion"
            )

        return self.promotion_status


# ==================================================
# Manager
# ==================================================

class Manager(Employee):

    def work(self):

        print(
            f"{self.name} is managing the team."
        )


    def calculate_salary(self):

        allowance = 15000

        return (
            self.get_salary()
            +
            allowance
        )


    def promotion(self):

        if self.rating is None:

            self.promotion_status = (
                "Performance Not Rated"
            )

        elif self.rating >= 4.5:

            self.promotion_status = (
                "Selected for Promotion - "
                "Senior Manager"
            )

        elif self.rating >= 4:

            self.promotion_status = (
                "Getting Close to Promotion - "
                "Keep Learning"
            )

        elif self.rating >= 3:

            self.promotion_status = (
                "Needs More Improvement "
                "for Promotion"
            )

        else:

            self.promotion_status = (
                "Not Ready for Promotion"
            )

        return self.promotion_status


# ==================================================
# Intern
# ==================================================

class Intern(Employee):

    def work(self):

        print(
            f"{self.name} is learning "
            f"and assisting the team."
        )


    def calculate_salary(self):

        return self.get_salary()


    def promotion(self):

        if self.rating is None:

            self.promotion_status = (
                "Performance Not Rated"
            )

        elif self.rating >= 4.5:

            self.promotion_status = (
                "Selected for Promotion - "
                "Developer"
            )

        elif self.rating >= 4:

            self.promotion_status = (
                "Getting Close to Promotion - "
                "Keep Learning"
            )

        elif self.rating >= 3:

            self.promotion_status = (
                "Needs More Improvement "
                "for Promotion"
            )

        else:

            self.promotion_status = (
                "Not Ready for Promotion"
            )

        return self.promotion_status