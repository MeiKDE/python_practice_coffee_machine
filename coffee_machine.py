#Global variables of machine resources: 
machine_resources={
"water": 300,
"milk": 200,
"coffee": 100,
"money": 0
}

# to restock machine resources
def restock(drink, quantity):
    global machine_resources
    machine_resources[drink] = quantity

def coffee_selection(choice):
    coffee_selection=[
        {"espresso": {"water": 50, "coffee":18}},
        {"latte": {"water": 200, "coffee":24, "milk": 150}},
        {"cappuccino": {"water": 250, "coffee":24, "milk": 100}}        
    ]

def cost(drink):
    expresso_cost=2.95
    latte_cost=5.65
    cappuccino_cost=5.85
    
    if drink.lower()=="expresso":
        print(f"{drink} costs ${expresso_cost} dollars")
        return expresso_cost
    elif drink.lower()=="latte":
        print(f"{drink} costs ${latte_cost} dollars")
        return latte_cost
    elif drink.lower()=="cappuccino":
        print(f"{drink} costs ${cappuccino_cost} dollars")
        return cappuccino_cost
    else:
        return 0.00


# check if resources are sufficient
def check_resources(drink):
    #expresso requires 50ml water and 18g coffee
    if drink=="expresso":
        if machine_resources["water"]>=50 and machine_resources["coffee"]>=18:
            #print report() status after purchase
            #print (f'Report: {machine_resources["water"]}')
            #print (f'Report: {machine_resources["coffee"]}')
            return True
        else:
            print("Sorry, there is not enough resources")
            #print water and coffee status
            print(f'Water remaining: {machine_resources["water"]} ml')
            print(f'Coffee remaining: {machine_resources["coffee"]} g')
            
            
            print("Restocking resources...")
            if machine_resources["water"]<50:
                #restock water 
                restock(drink="water", quantity=300) #refill 300ml water to machine_resources
            if machine_resources["coffee"]<18:
                #restock coffee
                restock(drink="coffee", quantity=100) #refill 100g coffee to machine_resources
            return False
        

    # latte requiress 200ml water, milk or coffee
    if drink=="latte":
        if machine_resources["water"]>=200 and (machine_resources["coffee"]>=24 and machine_resources["milk"]>=150):
            #print machine_resources status after purchase
            #print(f'Report: water {machine_resources["water"]} ml')
            #print(f'Report: coffee {machine_resources["coffee"]} g')
            #print(f'Report: milk {machine_resources["milk"]} ml')
            return True
        else:
            print("Sorry, there is not enough resources")
            #print water, coffee, and milk status
            print(f'Water remaining: {machine_resources["water"]} ml')
            print(f'Coffee remaining: {machine_resources["coffee"]} g')
            print(f'Milk remaining: {machine_resources["milk"]} ml')
            
            
            print("Restocking resources...")
            if machine_resources["water"]<200:
                #restock water 
                restock(drink="water", quantity=300) #refill 300ml water to machine_resources
            if machine_resources["coffee"]<24:
                #restock coffee
                restock(drink="coffee", quantity=100) #refill 100g coffee to machine_resources
            if machine_resources["milk"]<150:
                #restock coffee
                restock(drink="coffee", quantity=200) #refill 100g coffee to machine_resources    
                
            return False
            
    # cappuccino requires 250ml water, milk or coffee
    if drink=="cappuccino":
        if machine_resources["water"]>=250 and (machine_resources["coffee"]>=24 and machine_resources["milk"]>=100):
            #print report() status after purchase
            #print(f'Report: water {machine_resources["water"]} ml')
            #print(f'Report: coffee {machine_resources["coffee"]} g')
            #print(f'Report: milk {machine_resources["milk"]} ml')   
            return True
        else:
            print("Sorry, there is not enough resources")
            #print water, coffee, and milk status
            print(f'Water remaining: {machine_resources["water"]} ml')
            print(f'Coffee remaining: {machine_resources["coffee"]} g')
            print(f'Milk remaining: {machine_resources["milk"]} ml') 
            
            
            
            print("Restocking resources...")
            if machine_resources["water"]<250:
                #restock water 
                restock(drink="water", quantity=300) #refill 300ml water to machine_resources
            if machine_resources["coffee"]<24:
                #restock coffee
                restock(drink="coffee", quantity=100) #refill 100g coffee to machine_resources
            if machine_resources["milk"]<100:
                #restock coffee
                restock(drink="milk", quantity=200) #refill 100g coffee to machine_resources    
            
            
            
            return False
            
# deduct resources if resource is sufficient
def deduct_resources(drink):
    
    print(f"{drink.lower()} is being made.")
    #expresso requires 50ml water and 18g coffee
    if drink.lower()=="expresso":
        machine_resources["water"]-=50 #descrease water by 50ml
        machine_resources["coffee"]-=18 #descrease coffee by 18g

        #print water and coffee status
        print(f'Water remaining: {machine_resources["water"]} ml')
        print(f'Coffee remaining: {machine_resources["coffee"]} g')
    

    # latte requiress 200ml water, milk or coffee
    if drink.lower()=="latte":
        machine_resources["water"]-=200 #descrease water by 200ml
        machine_resources["coffee"]-=24 #descrease coffee by 24g
        machine_resources["milk"]-=150 #descrease milk by 150ml

        #print water, coffee, and milk status
        print(f'Water remaining: {machine_resources["water"]} ml')
        print(f'Coffee remaining: {machine_resources["coffee"]} g')
        print(f'Milk remaining: {machine_resources["milk"]} ml')
            
    # cappuccino requires 250ml water, milk or coffee
    if drink.lower()=="cappuccino":
        machine_resources["water"]-=250 #descrease water by 250ml
        machine_resources["coffee"]-=24 #descrease coffee by 24g
        machine_resources["milk"]-=100 #descrease milk by 100ml

        #print water, coffee, and milk status
        print(f'Water remaining: {machine_resources["water"]} ml')
        print(f'Coffee remaining: {machine_resources["coffee"]} g')
        print(f'Milk remaining: {machine_resources["milk"]} ml') 

def purchase(drink):
    if check_resources(drink)==True:
        #payment process
        # calculate quarters = $0.25, dimes = $0.10, nickles = $0.05, pennies = $0.01
        print("Please insert coins. ")
        print("How many quarters? ")
        quarters=int(input())
        print("\n")
        print("How many dimes? ")
        dimes=int(input())
        print("\n")
        print("How many nickles? ")
        nickles=int(input())
        print("\n")
        print("How many pennies? ")
        pennies=int(input())
        print("\n")

        # calculate total value of coins
        total_value=(quarters*0.25 + dimes*0.10 + nickles*0.05 + pennies*0.01).__round__(2)
        
        print(f"Total value of coins: $ {total_value}")
        
        drink_cost=cost(drink).__round__(2)
        
        if total_value>=drink_cost:
            
            print("\n")
            #deduct cost from money
            deduct_resources(drink)
            print("\n")
            
            #print(f"check deduct_resource function: {machine_resources}")
            
            machine_resources["money"]+=drink_cost
            
            #print(f"check deduct_resource function again and see if money is added: {machine_resources}")
            
            print(f"Here is your change: {(total_value-drink_cost).__round__(2)} and {drink} ☕. Enjoy!")
        else:
            print(f"Sorry, you do not have enough money. You are short by: $ {drink_cost-total_value}")
     
        
# choose drink from menu
def report(machine_resources):
    print("\n")
    print("report: ")
    for key, value in machine_resources.items(): #print machine_resources status
        print(key + ": " + str(value))  
    print("\n")
    
    
#main program
while True:
    drink=""
    request=input("Would you like? (Expresso/Latte/Cappuccino): ").lower()
    if request=="expresso":
        drink="expresso"
    elif request=="latte":
        drink="latte"
    elif request=="cappuccino":
        drink="cappuccino"
    else:
        print("Invalid input. Please try again.")

    report(machine_resources)
    print("\n")
    print("Here is the cost for the following drink: ")
    cost(drink)
    print("\n")
    purchase(drink)
    print("\n")

    report(machine_resources) #print machine_resources status after purchase
    print("\n")
    
    continue_program=input(f"Would you like to continue? (y/n): ")
    if continue_program.lower()=="n":
        break

    








        











