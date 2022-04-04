from MenuItem import Menu,MenuItem,CoffeMaker,MoneyMachine
menu=Menu()
money_machine=MoneyMachine()
coffe_maker=CoffeMaker()
is_on=True
while is_on:
    options = menu.get_items()
    choice=input(f"What would you like to drink? ({options}): ")
    if(choice=="report"):
        coffe_maker.report()
        money_machine.money_raport()
    elif choice=="off":
        is_on=False
    else:
        drink=menu.find_drink(choice)
        if(drink==0):
            print("Unavailable item")
        else:
            print(f"You selected: {choice}")
            money_machine.machine_money()
            if(coffe_maker.is_resource_sufficient(drink) and money_machine.check_payment(drink)):
                coffe_maker.make_coffe(drink)

