import random

# Find the squares of numbers from 1 to 10
lst1 = [*range(1, 11, 1)]

i = 0

while i < len(lst1):
    print(f"{i+1}^2 = {lst1[i] ** 2}")
    i += 1

# Find the squares of numbers from 10 to 1
lst1 = [*range(1, 11, 1)]

i = len(lst1) - 1

while 0 <= i <= len(lst1):
    print(f"{i+1}^2 = {lst1[i] ** 2}")
    i -= 1

# Find the maximum number in the list, but not more than 100
rnd_lst = random.sample(range(0, 300), 25)

print(rnd_lst)

max_num = 0

i = 0

while i < len(rnd_lst):
    if max_num < rnd_lst[i] < 100:
        max_num = rnd_lst[i]
    i += 1

print(f"Maximum number: {max_num}")

# Find the sum of all numbers in the list divided by 3
rnd_lst = random.sample(range(1, 100), 40)

print(rnd_lst)

lst2 = []

i = 0

while i < len(rnd_lst):
    if rnd_lst[i] % 3 == 0:
        lst2.append(rnd_lst[i])
    i += 1

print(lst2)

print("The sum of the second list =", sum(lst2))

# Find the squares of numbers from 10 to 30
lst1 = [*range(10, 31, 1)]

i = 0

while i < len(lst1):
    q = lst1[i] ** 2
    print(f"{lst1[i]}^2 = {q}")
    i += 1

# In a list of words, find the word with the highest number of letters.
random_words = ["ready", "ball", "spell", "envious", "functional", "soup", "unadvised", "roasted", "drop",
                "border", "embarrass", "polite"]

letters_number = 0

word = ()

i = 0

while i < len(random_words):
    if len(random_words[i]) > letters_number:
        letters_number = len(random_words[i])
        word = random_words[i]
    i += 1

print(f"The longest word - {word}")

# Calculate and display separately the sum of paired and unpaired numbers in the list
rnd_lst = random.sample(range(0, 81), 30)

print(rnd_lst)

paired = []

unpaired = []

i = 0

while i < len(rnd_lst):
    if rnd_lst[i] % 2 == 0:
        paired.append(i)
    else:
        unpaired.append(i)
    i += 1

print("Sum of paired number =", sum(paired))

print("Sum of unpaired number =", sum(unpaired))

# Create a function that accepts an array and returns the sum of its elements
lst = random.sample(range(1, 100), 35)

print(lst)


def adr(x):
    return sum(x)


print("The sum of array:", adr(lst))

# Create a function that accepts two arguments: the first list and the second number k.
# Find the largest number in the list whose index is smaller than k.
# If the list has fewer elements than number k, return 0.
lst1 = random.sample(range(1, 100), 30)

print(lst1)

numb = int(input("Enter a number:"))


def largest(arr, k):
    if k > len(arr) or k <= 0:
        return 0
    else:
        x = 0
        lar = arr[x]
        while x < k:
            if arr[x] > lar:
                arr[x] = lar
            x += 1
        return lar


print(largest(lst1, numb))
