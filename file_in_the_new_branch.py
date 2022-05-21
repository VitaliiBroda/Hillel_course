import random

# Create a function that takes the radius and returns the length and square of circumference.
# Determine the cases when the radius is not a number.


def length_of_circumference(n):
    pi = 3.14
    try:
        long = 2 * pi * int(n)
        square = pi * int(n)**2
        return print(f"The length of the circle: {long}\n"
                     f"The square of the circle: {square}")
    except ValueError:
        print("You entered float number or not integer")


length_of_circumference(input("Enter the radius:"))

# The function accepts a number, returns whether the number is a palindrome or not.


def palindrome(n):
    number = n
    reverse = 0
    while n:
        digit = n % 10
        reverse = reverse * 10 + digit
        n = n // 10
    if number == reverse:
        return print("The number is a palindrome!")
    else:
        return print("The number isn't a palindrome!")


palindrome(int(input("Enter the number:")))

# The function accepts a number n greater than 0. By using recursion,
# display all the numbers less than n but greater than 0.


def recursion(i):
    if i == 1:
        return print(i)
    else:
        recursion(i - 1)
        return print(i)


recursion(int(input("Enter a number:")))

# Create a lambda function that accepts x i y and returns x^2 + y^2.
number_1, number_2 = int(input("Enter X:")), int(input("Enter Y:"))

sum_of_sqr = lambda x, y: (x ** 2) + (y ** 2)

print(sum_of_sqr(number_1, number_2))

# Create a lambda function that accepts the word and returns its length.
len_of_word = lambda word: len(word)

print(len_of_word(input("Enter the word:")))

# Create a map that converts all the numbers in the list to a string.
numbers = random.sample(range(1, 50), 12)

print(f"Integers but string: {list(map(str, numbers))}")

# Create a filter that leaves only numbers more than 10 in the list.
numbers = random.sample(range(1, 20), 15)

print(f"All numbers: {numbers}")


def scales(i):
    return i > 10


numbers_over_10 = list(filter(scales, numbers))

print(f"List with numbers > 10: {numbers_over_10}")

# There is a list of words with the help of the map remove all the letters "a" from each word.


def replacer(word):
    new_word = word.replace("a", "")
    return new_word


random_words = ["fan", "jam", "day", "fair", "rain", "pain", "bake", "cake", "part", "coat"]

mod_words = list(map(lambda word: word.replace("a", ""), random_words))  # first approach

print(mod_words)

print(list(map(replacer, random_words)))  # second approach

# There is a list of words, using the filter to fill in only those words with a number of letters greater than 4.
random_words = ["constellation", "choke", "day", "fair", "gesture", "pain", "pastel", "concern", "public", "coat"]


def len_word(word):     # first approach
    return len(word) > 4


print(list(filter(len_word, random_words)))

new_lst = list(filter((lambda word: len(word) > 4), random_words))  # second approach

print(f"{random_words}\n"
      f"{new_lst}")