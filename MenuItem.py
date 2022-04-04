class MenuItem:
    def __init__(self,name,cost,water,milk,coffe):
        self.name=name
        self.cost=cost
        self.ingredients={
            "water": water,
            "milk": milk,
            "coffe": coffe
        }

class Menu:
    def __init__(self):
        self.menu=[
            MenuItem(name="latte",cost=2.5,water=200,milk=150,coffe=24),
            MenuItem(name="espresso",cost=1.5,water=50,milk=0,coffe=18),
            MenuItem(name="cappuccino",cost=3.0,water=250,milk=50,coffe=24)
        ]
    def get_items(self):
        options=""
        for item in self.menu:
            options+=f"{item.name}, {item.cost}/"
        options+="report/off"
        return options
    def find_drink(self,order_name):
        for item in self.menu:
            if order_name==item.name:
                return item
        return 0

class CoffeMaker:
    def __init__(self):
        self.ingredients={
            "water":200,
            "milk":300,
            "coffe":100
        }
    def report(self):
        print(f"Water: {self.ingredients['water']} ml")
        print(f"Milk: {self.ingredients['milk']} ml")
        print(f"Coffe: {self.ingredients['milk']} ml")
    def is_resource_sufficient(self,drink):
        can_make=True
        for item in drink.ingredients:
            if drink.ingredients[item]>self.ingredients[item]:
                print(f"Sorry there is not enough {item}")
                can_make=False
        return can_make
    def make_coffe(self,order):
        for item in order.ingredients:
            self.ingredients[item]-=order.ingredients[item]
        print(f"You can take your {order.name}!")

class MoneyMachine:
    Currency="Lei"
    coin_values={
        "50 de bani": 0.5,
        "1 leu": 1.0,
        "5 lei": 5.0
    }
    def __init__(self):
        self.Value=0
        self.profit=0
    def machine_money(self):
        self.Value+=float(input(f"How many coins(50 de bani)?"))*self.coin_values['50 de bani']
        self.Value += float(input(f"How many bucks(1 leu)?")) * self.coin_values['1 leu']
        self.Value += float(input(f"How many bucks(5 lei)?")) * self.coin_values['5 lei']
    def check_payment(self,drink):
        check=True
        if self.Value<drink.cost:
            check=False
            print(f"Sorry, not enough money.The {drink.name} cost {drink.cost}.Money refunded.")
        else:
            self.Value-=drink.cost
            print(f"Here is your change {self.Value}")
            self.profit=drink.cost
            return check
    def money_raport(self):
        print(f"Machine profit: {self.profit}")