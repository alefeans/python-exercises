import sys
from person import Person


class Student(Person):
    #   Class Constructor
    #
    #   Parameters:
    #   firstName - A string denoting the Person's first name.
    #   lastName - A string denoting the Person's last name.
    #   id - An integer denoting the Person's ID number.
    #   scores - An array of integers denoting the Person's test scores.
    #
    # Write your constructor here
    def __init__(self, firstName, lastName, idNum, scores):
        super().__init__(firstName, lastName, idNum)
        self.scores = scores
        if (len(self.firstName) < 1) and (len(self.firstName) > 10):
            sys.exit(1)
        elif (len(self.lastName) < 1) and (len(self.lastName) > 10):
            sys.exit(1)
        elif (len(self.scores) < 0) and (len(self.scores) > 100):
            sys.exit(1)

    #   Function Name: calculate
    #   Return: A character denoting the grade.
    #
    # Write your function here
    def calculate(self):
        result = sum(self.scores) / len(self.scores)
        letter = ""
        if (result > 89) and (result < 101):
            letter = "O"
        elif (result > 79) and (result < 90):
            letter = "E"
        elif (result > 69) and (result < 80):
            letter = "A"
        elif (result > 54) and (result < 70):
            letter = "P"
        elif (result > 39) and (result < 55):
            letter = "D"
        else:
            letter = "T"
        return letter
