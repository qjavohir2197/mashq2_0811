#1-misol
words = ["salom", "dunyo", "python", "map", "lambda"]
lengths = list(map(lambda s: len(s), words))
print(lengths)


#2-misol
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
result = list(map(lambda x: x**2, filter(lambda x: x % 2 != 0, numbers)))
print(result)


#3-misol
numbers = [10, 20, 30, 40]
result = list(map(lambda x: x[0]*x[1], enumerate(numbers)))
print(result)


#4-misol
is_palindrome = lambda s: s == s[::-1]
print(is_palindrome("level"))
print(is_palindrome("python"))


#5-misol
numbers = [1, 3, 5, 7, 9, 11, 15]
result = list(map(lambda x: x*3, filter(lambda x: 5 < x < 10, numbers)))
print(result)
