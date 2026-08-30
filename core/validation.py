def get_integer(message):

    while True:

        try:
            return int(input(message))

        except ValueError:
            print("Please enter a valid integer.")


def get_positive_integer(message):

    while True:

        value = get_integer(message)

        if value > 0:
            return value

        print("Value must be greater than 0.")


def get_age(message):

    while True:

        age = get_integer(message)

        if 18 <= age <= 60:
            return age

        print("Age must be between 18 and 60.")


def get_float(message):

    while True:

        try:
            return float(input(message))

        except ValueError:
            print("Please enter a valid number.")


def get_positive_float(message):

    while True:

        value = get_float(message)

        if value > 0:
            return value

        print("Value must be greater than 0.")


def get_name(message):

    while True:

        name = input(message).strip()

        if name:
            return name

        print("Name cannot be empty.")


def get_rating(message):

    while True:

        try:

            rating = float(input(message))

            if 1 <= rating <= 5:
                return rating

            print("Rating must be between 1 and 5.")

        except ValueError:

            print("Please enter a valid number.")


def get_experience(message):

    while True:

        experience = get_integer(message)

        if experience >= 0:
            return experience

        print("Experience cannot be negative.")