def main_function():

    mainList = []
    evenList = []
    oddList = []

    while True:
        number = input("Please enter positive integers only - Enter quit when you're done: ")
        if number == "quit":
            break
        elif int(number) < 0:
            print("This is a negative number. Please enter positive integers only!")
        else:
            mainList.append(int(number))
            if (int(number) % 2) == 0:
                evenList.append(int(number))
            else:
                oddList.append(int(number))

    return mainList, evenList, oddList

lists = main_function()
main_list = lists[0]
even_list = lists[1]
odd_list = lists[2]
print("Main List:", main_list)
print("Even List:", even_list)
print("Odd List:", odd_list)

print ("Minimum Value in Main List:", min(main_list))
print ("Minimum Value in Even List:", min(even_list))
print ("Minimum Value in Odd List:", min(odd_list))

print ("Maximum Value in Main List:", max(main_list))
print ("Maximum Value in Even List:", max(even_list))
print ("Maximum Value in Odd List:", max(odd_list))




