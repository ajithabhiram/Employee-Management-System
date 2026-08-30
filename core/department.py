class Department:

    company = "ABC Technologies"


    def __init__(
        self,
        department_id,
        department_name
    ):

        self.department_id = department_id

        self.department_name = department_name


    def display_department(self):

        print(
            f"Department ID: "
            f"{self.department_id}"
        )

        print(
            f"Department Name: "
            f"{self.department_name}"
        )