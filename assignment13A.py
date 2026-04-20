"""
-----------------------------------------------------------------------
ASSIGNMENT 13A: Object practice
-----------------------------------------------------------------------
[ ] 1. Header Docstring included.
[ ] 2. Define a class for a part of your project using PascalCase.
[ ] 3. Use __init__ to set private attributes (__variable).
[ ] 4. Write Setters and Getters for the attributes.
[ ] 5. Write a summary function that returns a formatted description.
[ ] 6. Instantiate two distinct objects and print their summaries.
-----------------------------------------------------------------------
"""

class Employee:
    def __init__(self, first_name, last_name, employee_id, position, hourly_pay):
        # Private attributes
        self.__first_name = first_name
        self.__last_name = last_name
        self.__employee_id = employee_id
        self.__position = position
        self.__hourly_pay = hourly_pay

    # Getters
    def get_first_name(self):
        return self.__first_name

    def get_last_name(self):
        return self.__last_name

    def get_employee_id(self):
        return self.__employee_id

    def get_position(self):
        return self.__position

    def get_hourly_pay(self):
        return self.__hourly_pay

    # Setters
    def set_first_name(self, first_name):
        self.__first_name = first_name

    def set_last_name(self, last_name):
        self.__last_name = last_name

    def set_employee_id(self, employee_id):
        self.__employee_id = employee_id

    def set_position(self, position):
        self.__position = position

    def set_hourly_pay(self, hourly_pay):
        if hourly_pay >= 0:
            self.__hourly_pay = hourly_pay

    # Summary method
    def get_summary(self):
        return (f"Employee Summary: {self.__first_name} {self.__last_name}, "
                f"ID: {self.__employee_id}, Position: {self.__position}, "
                f"Hourly Pay: ${self.__hourly_pay:.2f}")


# Instantiate two distinct objects
employee1 = Employee("John", "Smith", "E101", "Barista", 15.50)
employee2 = Employee("Maria", "Lopez", "E102", "Manager", 22.75)

# Print summaries
print(employee1.get_summary())
print(employee2.get_summary())