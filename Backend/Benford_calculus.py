def benford_calculus(x):

    return the_law(x)

def the_law(num):
    numbers = {"1": 0, "2": 0, "3": 0, "4": 0, "5": 0, "6": 0, "7": 0, "8": 0, "9": 0}
    number = int(num)

    while number > 9:
        numbers[str(number)[0]] += int(str(number)[1:]) + 1
        number -= int(str(number)[1:]) + 1

    for i in range(number):
        numbers[str(number)] += 1
        number -= 1
    return numbers
