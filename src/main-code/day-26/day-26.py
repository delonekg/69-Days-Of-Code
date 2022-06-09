names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]
upper_names = [name.upper() for name in names if len(name) > 5]
print(upper_names)


# Exercise 26.1 (Squared Numbers)
def ex_1():
    numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
    squared_numbers = [(num ** 2) for num in numbers]
    print(squared_numbers)


ex_1()


# Exercise 26.2 (Even Numbers)
def ex_2():
    numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
    result = [num for num in numbers if num % 2 == 0]
    print(result)


ex_2()


# Exercise 26.3 (Data Overlap)
def ex_3():
    file1_data = []
    file2_data = []

    with open("file1.txt") as f1:
        data = f1.readlines()
        for num in data:
            file1_data.append(num.replace("\n", ""))

    with open("file2.txt") as f2:
        data = f2.readlines()
        for num in data:
            file2_data.append(num.replace("\n", ""))

    result = [int(num) for num in file1_data if num in file2_data]
    print(result)


ex_3()
