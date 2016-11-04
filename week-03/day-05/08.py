# Create a new class called `Person` that has a first_name and a last_name (takes it in it's constructor)
# It should have a `greet` method that prints it's full name

# Create a `Student` class that is the child class of `Person`
# it should have a method to add grades
# it should have a `salute` method that prints it's full name and the average of it's grades as well

class Person:

    def greet(self, firstname,lastname):
        greetings = ""
        greetings = firstname + " " +lastname
        return greetings




class Student(Person):
    grade = []

    def add_grade(self, grade):
        if 1 <= grade and 5 >= grade:
            self.grade.append(grade)
            return grade

    def average(self):
        summa = 0
        for i in range(len(self.grade)):
            summa += self.grade[i]
            average = summa / len(self.grade)

        return  average

#greet left
    def solute(self):
        return self.average()




magic = Student()
magic.greet("Vladimir","Putin")
magic.add_grade(3)
magic.add_grade(4)
magic.add_grade(4)


print(magic.greet("Vladimir","Putin"))
print(magic.solute())
