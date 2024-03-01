#Michael Basazinew
#mbasazin
#Project: Car Dealership
#References: class homeworks, labs, and textbook

import carsPackage.dealership as info

class cust_info:
    def __init__(self,credit,budget):
        self.credit = credit
        self.budget = budget        

    #determine if credit score is eligible
    def credit_score(self):
        if self.credit >= 600:
            return print('\nBased on your credit score, you are eligible to finance a car')
        elif self.credit < 600:
            return print('\nBased on your credit score, you are not eligible to finance a car')
        else:
            return print('\nYou did not enter a valid number')

    #determine if user's budget fits car prices
    def car_budget(self):
        if self.budget <= 7000:
            return print('Your budget is lower than our most cars available but here are the cars...')
        elif self.budget > 7000:
            return print('We have cars that fit your budget...')
        else:
            return print('You did not enter a valid number, but here is our list...')

        
class repair:
    def __init__(self, insurance, damage):
        self.insurance = insurance
        self.damage = damage        

    #determine if customer is eligible for car insurance savings
    def car_insurance(self):
        if self.insurance == 'state farm' or self.insurance == 'gieco' or self.insurance == 'all state':
            save = self.damage * .35
            discount = self.damage - save
            return print('Since you have {} insurance, you save 35%.\nYour total cost is now ${}'.format(self.insurance,discount))
        return print('You do not have a valid insurance associate with us')
    

def pick():
    d = {}
    temp = open('cars.txt','r')
    display = temp.readlines()

    #converts cars.txt into dictionary
    for x in display:
        car,make,year,price = x.strip('\n').split(',')
        d[car] = [make,year,price]
    return d    


def main():
    d = pick() #displays all cars
    cart = {} #empty cart for items to be added into wishlist
    print("\nWelcome to Mike's Shop!\nWe sell, rent and repair cars!")

    while True:
        option = int(input('\nAre you looking to 1)Buy 2)Rent 3)Repair 4)Exit\nEnter a number: '))

        if option == 1 or option == 2:
            credit = int(input('What is your credit score? '))
            budget = int(input('What is your budget? '))
            customer = cust_info(credit,budget) #calls cust_info class
            customer.credit_score()
            customer.car_budget()

            info.options(d)
            choice = input("which car number are you interested in? ")
            returned = info.find(choice,d,cart)

            #add car to cart
            if returned == False:
                print('{} not found. Returning to main menu...'.format(choice))                 
            else:
                info.display_car(cart)
        
        elif option == 3:
            insurance = input(str('whats your insurance? State Farm? Gieco? All State? or none? ' )).lower()
            damage = int(input('What was the total damage cost quote? ' ))
            x = repair(insurance,damage) #calls repair class
            x.car_insurance()

        #exits while loop
        elif option == 4:
            print("\nThank you for visiting us. See you soon!")
            break
        
        else:
            print("\nPlease choose from the following menu")
        
 
main()


    
