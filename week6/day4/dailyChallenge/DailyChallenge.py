# Daily Challenge: Happy Birthday
from datetime import date
from datetime import datetime
usr_bd = input(
    'Please indicate your birthday date in the following format DD/MM/YYYY: ')
birthday = datetime.strptime(f'{usr_bd}', "%d/%m/%Y")

today = date.today()
age = today.year - birthday.year - \
    ((today.month, today.day) < (birthday.month, birthday.day))


if str(age)[1] == '1':
    cake = """
         _i_________
        |:H:a:p:p:y:|
      __|___________|__
     |^^^^^^^^^^^^^^^^^|
     |:B:i:r:t:h:d:a:y:|
     |                 |
     ~~~~~~~~~~~~~~~~~~~

       """

elif str(age)[1] == '2':
    cake = """
         _ii________
        |:H:a:p:p:y:|
      __|___________|__
     |^^^^^^^^^^^^^^^^^|
     |:B:i:r:t:h:d:a:y:|
     |                 |
     ~~~~~~~~~~~~~~~~~~~
    
       """

elif str(age)[1] == '3':
    cake = """
         _iii_______
        |:H:a:p:p:y:|
      __|___________|__
     |^^^^^^^^^^^^^^^^^|
     |:B:i:r:t:h:d:a:y:|
     |                 |
     ~~~~~~~~~~~~~~~~~~~

       """
elif str(age)[1] == '4':
    cake = """
         _iiii______
        |:H:a:p:p:y:|
      __|___________|__
     |^^^^^^^^^^^^^^^^^|
     |:B:i:r:t:h:d:a:y:|
     |                 |
     ~~~~~~~~~~~~~~~~~~~
    
       """
elif str(age)[1] == '5':
    cake = """
     _iiiii_____
    |:H:a:p:p:y:|
  __|___________|__
 |^^^^^^^^^^^^^^^^^|
 |:B:i:r:t:h:d:a:y:|
 |                 |
 ~~~~~~~~~~~~~~~~~~~

   """
elif str(age)[1] == '6':
    cake = """
     _iiiiii____
    |:H:a:p:p:y:|
  __|___________|__
 |^^^^^^^^^^^^^^^^^|
 |:B:i:r:t:h:d:a:y:|
 |                 |
 ~~~~~~~~~~~~~~~~~~~

   """
elif str(age)[1] == '7':
    cake = """
     _iiiiiii___
    |:H:a:p:p:y:|
  __|___________|__
 |^^^^^^^^^^^^^^^^^|
 |:B:i:r:t:h:d:a:y:|
 |                 |
 ~~~~~~~~~~~~~~~~~~~

   """
elif str(age)[1] == '8':
    cake = """
     _iiiiiiii__
    |:H:a:p:p:y:|
  __|___________|__
 |^^^^^^^^^^^^^^^^^|
 |:B:i:r:t:h:d:a:y:|
 |                 |
 ~~~~~~~~~~~~~~~~~~~

   """
elif str(age)[1] == '9':
    cake = """
     _iiiiiiiii_
    |:H:a:p:p:y:|
  __|___________|__
 |^^^^^^^^^^^^^^^^^|
 |:B:i:r:t:h:d:a:y:|
 |                 |
 ~~~~~~~~~~~~~~~~~~~

   """
elif str(age)[1] == '0':
    cake = """
     iiiiiiiiii_
    |:H:a:p:p:y:|
  __|___________|__
 |^^^^^^^^^^^^^^^^^|
 |:B:i:r:t:h:d:a:y:|
 |                 |
 ~~~~~~~~~~~~~~~~~~~

   """
# checking for a leap year
if (birthday.year % 400 == 0) and (birthday.year % 100 == 0):
    print(cake * 2)

elif (birthday.year % 4 == 0) and (birthday.year % 100 != 0):
    print(cake * 2)

else:
    print(cake)
