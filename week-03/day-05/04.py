# Create a student Class
# that has a method `add_grade`, that takes a grade from 1 to 5
# an other method `get_average`, that returns the average of the
# grades

class Student:
    grade = []

    def add_grade(self, grade):
        if 1 <= grade and 5 >= grade:
            self.grade.append(grade)

    def average(self):
        summa = 0
        for i in range(len(self.grade)):
            summa += self.grade[i]
            average = summa / len(self.grade)
        return average



act = Student()

act.add_grade(3)
act.add_grade(6)
act.add_grade(4)
act.add_grade(74)


print(act.grade)
print(act.average())
