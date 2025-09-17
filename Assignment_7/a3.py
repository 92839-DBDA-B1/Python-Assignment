# 3.
# Create a class Student with the following features:

# Initializer (__init__)

# Data members: roll_no, name, math, physics, chemistry.

# Setters (mutators):

# set_name(name) → update student’s name.

# set_math(m), set_physics(p), set_chemistry(c) → update subject marks.

# Getters (accessors):

# get_roll_no()

# get_name()

# get_math(), get_physics(), get_chemistry()

# Facilitator methods:

# calculate_total() → returns total marks.

# calculate_percentage() → returns percentage (out of 300).

# has_passed() → returns True if percentage ≥ 40, else False.

class Student:
    def __init__(self, roll_no, name, math, physics, chemistry):
        self.roll_no = roll_no
        self.name = name
        self.math = math
        self.physics = physics
        self.chemistry = chemistry

    def set_name(self, name):
        self.name = name

    def set_roll_no(self, roll_no):
        self.roll_no = roll_no

    def set_math(self, math):
        self.math = math

    def set_physics(self, physics):
        self.physics = physics

    def set_chemistry(self, chemistry):
        self.chemistry = chemistry

    def get_name(self):
        return self.name

    def get_roll_no(self):
        return self.roll_no

    def get_math(self):
        return self.math

    def get_physics(self):
        return self.physics

    def get_chemistry(self):
        return self.chemistry

    def calculate_total(self):
        return self.math + self.physics + self.chemistry

    def calculate_percentage(self):
        return (self.calculate_total() / 300) * 100

    def has_passed(self):
        return self.calculate_percentage() >= 40


student1 = Student(101, "Neha", 80, 70, 60)
print("Name:", student1.get_name())
print("Roll No:", student1.get_roll_no())
print("Total Marks:", student1.calculate_total())
print("Percentage:", student1.calculate_percentage())
print("Has Passed:", student1.has_passed())
