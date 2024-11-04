def display_square(side_length,symbol,filled):
    for i in range(side_length):
        if filled:
            print(symbol*side_length)
        else:
            if i == 0 or i == side_length - 1:
                print(symbol*side_length)
            else:
                print(symbol + " "*(side_length-2) + symbol)
print("Filled square:")
display_square(5,"*",True)
print("Hollow square:")
display_square(5,"*",False)