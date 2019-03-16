from myclass import Person, Teacher
import datetime

Person = Person

Julian = Person('Julian', 'Almeida',
                datetime.date(1976, 2, 15),
                'portugal')

print('** Julian **\n', Julian)

Mark = Teacher('Mark', 'Hitton',
              datetime.date(1980, 12, 1),
              'american', 'English')

print('** Mark **\n', Mark)
