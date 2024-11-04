def display_even_numbers(start, end):
    for number in range(start, end + 1):
        if number % 2 == 0:
            print(number, end=" ")

display_even_numbers(2, 20)
