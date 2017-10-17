"""
Read in list to dictionary
Return aggregate price
"""
def main():
    foods = {}
    total = 0
    try:
        print("This program keeps a running total of your shopping list.\nUse 'EXIT' to exit.")
        with open("shoppinglist.txt") as f:
            foodList = f.readlines()
        foodList = [x.strip("\n") for x in foodList]
        del foodList[0]
        foods = {foodList[i]: foodList[i+1] for i in range(0, len(foodList), 2)}
        
        getPrice = input("Enter an item: ")
        while getPrice != 'EXIT':
            try:
                total += float(foods[getPrice])
                print("Your current total is $" + "{:.2f}".format(total))
                getPrice = input("\nEnter an item: ")
            except KeyError:
                print("That is not a valid item.")
                getPrice = input("\nEnter an item: ")
        print("Your final total is $" + "{:.2f}".format(total))
    
    except FileNotFoundError:
        quit

main()
    
