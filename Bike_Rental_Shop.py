class BikeRentalShop:
    def __init__(self,stock):
        self.st=stock
    def DisplayBike(self):
        print(f"Total numbers of bike available are:->{self.st}")
    def RentForBike(self,q):
        if q<=0:
            print(f"Enter the positive value or greater than zero...!!!")
        elif q>self.st:
            print(f"Enter the value (less than stock)")
        else:
            print(f"Total Payable prices:--> Rupees {q*1000}")
            print(f"Total Bikes left :--> {self.st-n}")
while True:
    obj=BikeRentalShop(100)
    uc=int(input('''
    1 Display Stocks
    2 Rent a Bike
    3 Exit
    '''))
    if uc==1:
        obj.DisplayBike()
    elif uc==2:
        n=int(input("Enter the quantity of Bike you need for rent:-->"))
        obj.RentForBike(n)
    else:
        break;
