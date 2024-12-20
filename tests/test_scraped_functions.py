# Scratch file for me to test different functions to learn/test
# Here I write blocks of code for practice, or it may be code I scraped and decided not to use.

# I decided to make most things a def() function and just not call it


def using_greater_lesser_signs():
    a = '\u2265 = greater than or equal to'
    b = '\u2264 = less than or equal to'
    print(a)
    print(b)


# 8/31/2024 - Can I nest a while loop in an except? I don't want to end it while user keeps entering ValueError.
def test_nested_try_except():
    c = input('Enter integer: ')
    print('')
    try:
        c = int(c)
    except ValueError:
        print('Please enter an integer')
        c = input('Enter integer again: ')
        print('')
        while type(c) is not int:
            print('Please enter an integer')
            c = input('Enter integer again: ')
            print('')
            try:
                c = int(c)
            except ValueError:
                pass
    finally:
        print(f"The number as an integer type is {c}")


# 9/1/2024 - Changed how user enter's infant/neonate age entry
def old_pt_age():
    print('Enter the Patient\'s Age.\n\n'
          'If the patient is \u2264 1-Year\'s-old: \n'
          'Type the letter "I" for Infant (Aged 1 month - 12 months) or '
          '"N" for Neonate (0 - 1 month old) respectively. \n\n')


def returning_specific_parameter_for_function():
    # What if I have a function that returns two parameters.
    # Of those two parameters, how do I call the second argument?

    # There are two ways to go about this:

    # The first way is to unpack the returned values:

    def function_1():
        x = 5
        y = 10
        return x, y

    # Unpack the returned values
    a, b = function_1()  # The two arguments are returned are set to equal the two new arguments 'a' and 'b'
    # Now 'b' is the second value (y)
    print(b)  # Output: 10

    # The second way is to index the return tuple, and call the argument you want:
    def function_2():
        x = 5
        y = 10
        return x, y

    # Accessing the second value (y) using index 1
    result = function_2()  # Two arguments --> Result // type(result) is a tuple
    print(result[1])  # Output: 10


# 11/15/2024
def class_ship_function():  # Practice using classes and how they work
    class Ship:  # Creates the class "Ship" so we can now create instances of "Ship"

        def __init__(self, name, capacity):
            # ^^^^ Anytime we make an instance of "Ship" and "__init__" is used, the function is auto executed.
            self.name = name
            self.capacity = capacity
            self.cargo = 0
            # ^^^^^ The parameters name and capacity are applied to the object BECAUSE we used "self.[parameter]"

        # sail function that only executes after a call
        def sail(self, location):
            self.location = location
            return "The {} has sailed for {}".format(self.name, self.location)

    black_pearl = Ship("Black Pearl", 800)
    black_pearl.sail(input())
    print(black_pearl.location)


def more_class_practice():
    class Patient:
        def __init__(self, name=None, age=None):
            self.name = name
            self.age = age
            # Setting vitals and labs to groups make it easier to read and understand
            self.vitals = {'pulse': None, 'blood_pressure': None, 'temperature': None}
            self.labs = {'blood_glucose': None, 'cholesterol': None}
