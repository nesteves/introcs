__author__ = 'nunoe'

import datetime


class Person(object):

    def __init__(self, name):
        self.name = name
        self.birthday = None
        self.last_name = name.split(' ')[-1]

    def set_birthday(self, year, month, day):
        """ Sets the birthday of the person
        :param year: int
        :param month: int
        :param day: int
        :return: nothing
        """
        self.birthday = datetime.date(year, month, day)

    def get_age(self):
        """ Returns the age of the person
        :return: int, the age of the Person's instance
        """
        if self.birthday is None:
            raise(ValueError('Birthday is not set.'))
        return (datetime.date.today() - self.birthday).days

    def __str__(self):
        return self.name

    def __lt__(self, other):
        """ Implements the less than method for this class
        :param other: another instance of Person
        :return: boolean, the result of comparing self and other lexicographically (self < other)
        """
        if self.last_name == other.last_name:
            return self.name < other.name
        return self.last_name < other.last_name


class MITPerson(Person):

    id = 0

    def __init__(self, name):
        super(MITPerson, self).__init__(name)
        self.id = MITPerson.id
        MITPerson.id += 1

    def __lt__(self, other):
        """ Overrides the less than method from Person to compare elements
            based on their ID numbers
        :param other: another instance of MITPerson
        :return: boolean, the result of comparing self and other by ID number
        """
        return self.id < other.id


class Student(MITPerson):
    pass


class UG(Student):

    def __init__(self, name, class_year):
        super(UG, self).__init__(name)
        self.year = class_year

    def get_class(self):
        return self.year


class Grad(Student):
    pass


class TransferStudent(Student):
    pass


def is_student(obj):
    return isinstance(Student, obj)


class Grades(object):
    """ Class that maps students to a set of grades """
    def __init__(self):
        """ Builds the empty grade book """
        self.students = []
        self.grades = {}
        self.is_sorted = True

    def add_student(self, student):
        """ Adds a student to the list of students creates its entry for the grade book
        :param student: Student, the student to be added to the list
        """
        if student in self.students:
            raise ValueError('Duplicate Student.')
        self.students.append(student)
        self.grades[student.id] = []
        self.is_sorted = False

    def add_grade(self, student, grade):
        """ Adds a grade to the grade book of a particular student
        :param student: Student
        :param grade: the grade obtained
        """
        try:
            self.grades[student.id].append(grade)
        except KeyError:
            raise ValueError('Student not in Grade Book.')

    def get_grades(self, student):
        """ Returns all the grades from a particular student
        :param student: Student, from which to get the grades
        :return: list, all the grades from the student's grade book
        """
        try:
            return self.grades[student.id][:] # notice that a copy is returned
        except KeyError:
            raise ValueError('Student not in Grade Book.')

    def get_students(self):
        """  Returns all the students in the grade book
            Notice that this is a generator method and will return one student at a time
        :return: student
        """
        if not self.is_sorted:
            self.students.sort()
            self.is_sorted = True
        for s in self.students:
            yield s


def grade_report(course):
    """ Returns a report on the grade book given
    :param course: Grades, the grade book to be reported
    :return: str, a report on the grade book
    """
    report = []
    for st in course.get_students():
        try:
            average = sum(course.get_grades(st)) / len(course.get_grades(st))
            report.append(str(st) + '\'s mean grade is: ' + str(average) + '.')
        except ZeroDivisionError:
            report.append(str(st) + ' has no grades.')
    return '\n'.join(report)

if __name__ == '__main__':
    # Test Person Lists
    a = Person("Roger Rabbit")
    b = Person("Alec Baldwin")
    normalList = [a, b]
    print [str(e) for e in normalList]
    normalList.sort()
    print [str(e) for e in normalList]

    # Test MIT Person Lists
    a = MITPerson("Roger Rabbit")
    b = MITPerson("Alec Baldwin")
    mitList = [a, b]
    print [str(e) for e in mitList]
    mitList.sort()
    print [str(e) for e in mitList]

    # Test Grades class
    a = Student('Nuno')
    b = Student('Neuza')
    c = Student('Antonio')

    cs600 = Grades()
    cs600.add_student(c)
    cs600.add_grade(c, 20)
    cs600.add_grade(c, 13)
    cs600.add_grade(c, 6)
    cs600.add_student(b)
    cs600.add_grade(b, 12)
    cs600.add_grade(b, 13)
    cs600.add_grade(b, 15)
    cs600.add_student(a)
    cs600.add_grade(a, 5)
    cs600.add_grade(a, 3)
    cs600.add_grade(a, 15)

    print grade_report(cs600)