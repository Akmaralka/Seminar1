import datetime


class Person:

    def __init__(self, name, surname, birthdate, nationality):
        self.name = name
        self.surname = surname
        self.birthdate = birthdate
        self.nationality = nationality

    def age(self):
        print('Age: ', end='')
        today = datetime.date.today()

        age = today.year - self.birthdate.year

        if today < datetime.date(today.year, self.birthdate.month, self.birthdate.day):
            age -= 1

        return age

    def __str__(self):
        return "Name: %s \n" \
               "Surname: %s \n" \
               "Birthdate: %s \n" \
               "Nationality: %s" % (self.name, self.surname, self.birthdate, self.nationality)


class Teacher(Person):
    def __init__(self, name, surname, birthdate, nationality, init_subject):
        Person.__init__(self, name, surname, birthdate, nationality)
        self.subject = init_subject

    def __str__(self):
        return "%s \nSubject: %s" % (Person.__str__(self), self.subject)
