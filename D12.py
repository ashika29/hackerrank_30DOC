# Question link: https://www.hackerrank.com/challenges/30-inheritance/problem
# Code section:


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
    def __init__(self, firstName, lastName, id, scores):
        self.score = scores
        return super(Student, self).__init__(firstName, lastName, id)   
    #   Function Name: calculate
    #   Return: A character denoting the grade.
    #
    # Write your function here
    def calculate(self):
        sm = 0
        for value in self.score:
            sm += int(value)
        sm =int(sm / len(self.score))
        if sm < 40:
            self.grade = 'T'
        elif sm > 39 and sm < 55:
            self.grade = 'D'
        elif sm > 54 and sm < 70:
            self.grade = 'P'
        elif sm > 69 and sm < 80:
            self.grade = 'A'
        elif sm > 79 and sm < 90:
            self.grade = 'E'
        elif sm > 89 and sm < 101:
            self.grade = 'O'
        else:
            pass
        return self.grade
        

