# 1.
# Create a class named Mobile with attributes ModelName,Company,Price and with
# methods:set_attributes, print_details and can_afford

class Mobile:
    def __init__(self,ModelName, Company, Price):
        self.Modelname=ModelName
        self.Company=Company
        self.Price=int(Price)

    def __del__(self):
        pass

    def set_attribute(self,Modelname,Company,Price):
        self.Modelname=Modelname
        self.Company= Company
        self.Price=int(Price)


    def print_details(self):
        print(f"Model name={self.Modelname}")
        print(f"Company name:{self.Company}")
        print(f"Price:{self.Price}")
        
    def can_afford(self,ammount):
        if ammount>=self.Price:
            print("You can afford")
        else:
            print("You can not afford")
        
mobile1=Mobile("OnePluse nord CE3","OnePluse","22000")
mobile1.print_details()
mobile1.can_afford(30000)
mobile1.can_afford(10000)

        
