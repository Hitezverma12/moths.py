def SquaredValues(beg, end):
    lst = [] 

    for i in range(beg, end):
        lst.append(i**2)  # square each value and add to the list

    lst_even = []
    lst_odd = []

    for i in lst:
        if i % 2 == 0:
            lst_even.append(i)
        else:
            lst_odd.append(i)

    print("Here's a list of even squares within the specified range:", lst_even) 
    print("Here's a list of odd squares within the specified range:", lst_odd) 

# Take user input
beg = int(input("Enter starting range: "))
end = int(input("Enter end range: "))

SquaredValues(beg, end)

        