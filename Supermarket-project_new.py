# 1. Loop to take Product details and quantity of products.
    # defining function to give the product and quantity details.
def enterProducts():
    buyingData = {}
    enterDetails = True
    while enterDetails:
        details = input("Press A to add product and Q to quit: ")
        if details == 'A':
            print("1:Biscuit, 2:Chicken, 3:Egg, 4:Fish, 5:Coke, 6:Bread, 7:Apple, 8:Onion, 9:Milk, 10:Butter")
            product = input("Enter product code number: ")
            quantity = int(input("Enter Quantity: "))
            buyingData.update({product:quantity})
        elif details == 'Q':
            enterDetails = False
        else:
            print("please select a correct option")
    return buyingData

    #definging function to calculate the subtotal of all 
def getPrice(product,quantity):
    priceData = {'1':3, '2':5, '3':1, '4':3, '5':2, '6':2, '7':3, '8':3, '9':2, '10':3}
    
    subtotal = priceData[product]*quantity
    print(product + ':$' + str(priceData[product]) + 'x' + str(quantity) + '=' +
     str(subtotal))
    return subtotal

    #defining function to apply discount as per the consumer membership.
def getDiscount(billAmount, membership):
    discount = 0
    if billAmount >= 25:
        if membership == 'Gold':
            discount = 20
            print(str(discount) + "% off for" + ' ' + membership + ' ' + 'membership on total amount: $' + str(billAmount))
            billAmount = billAmount * 0.80
        elif membership == 'Silver':
            discount = 10
            print(str(discount) + "% off for" + ' ' + membership + ' ' + 'membership on total amount: $' + str(billAmount))
            billAmount = billAmount * 0.90
        elif membership == 'Bronze':
            discount = 5
            print(str(discount) + "% off for" + ' ' + membership + ' ' + 'membership on total amount: $' + str(billAmount))
            billAmount = billAmount * 0.95
    else:
        print('No disount on the amount less than $25')
    return billAmount

    # defining a function to make final billing
def makeBill(buyingData, membership):
    billAmount = 0
    for key, value in buyingData.items():
        billAmount += getPrice(key, value)
    billAmount = getDiscount(billAmount, membership)
    print("The discounted amount is: $" + str(billAmount))

#Writing the code to call above functions and work fo this project.
buyingData = enterProducts()
membership = input('Enter Customer membership:')
print("1:Biscuit, 2:Chicken, 3:Egg, 4:Fish, 5:Coke, 6:Bread, 7:Apple, 8:Onion, 9:Milk, 10:Butter")
makeBill(buyingData, membership)




