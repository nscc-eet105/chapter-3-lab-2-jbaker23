#My name is Jacob Baker and this is Chapter 3 Lab 2 which I made on June 22
print ("Jane's Stuff Store")#This prints out the name of the store
print ("                  ")#space
user_input1=int(input("How many items would you like to purchase?"))#This calculates number of items

if user_input1 < 0:
    print("This can not be an answer.")#error prevention
else:
    total = 0
    for num in range(1,user_input1+1):
        user_input2=float(input(f"How much does item {num} cost:$ "))#this calculates the cost of each item
        if user_input2 < 0:
            print("Answer is not valid")#error prevention
        else:
            total += user_input2
    print(f"The total cost is ${total:.2f}.")#provides the running total of all the items at the end
    average_cost = total/user_input1
    print(f"The average cost is ${average_cost:.2f} per item.")#does division to get the average
        
    
    

