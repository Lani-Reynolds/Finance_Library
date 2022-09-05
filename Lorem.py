from dataclasses import dataclass


NEWLINE = "\n"
    
def Get_Assets(PO:object) -> list:
    order = PO.order
    assets:list = [(item.name, item.flat_price) for item in order]
    return assets

def Cost_Of_Goods(order:list):
    return sum([round((item.flat_price * item.quantity), 2) for item in order])

def Expenses_Receipt(order:list):
    receipt = ""
    total_expense = 0
    for item in order:
        sale_expense = round((item.flat_price * item.quantity), 2)
        total_expense += sale_expense
        receipt += "{} | {}{}".format(item.name, sale_expense, "\n")
    receipt += "Total Expenses: " + str(total_expense)
    return receipt

def Retail_Revenue(order:list):
    return sum([round((round(item.flat_price + (item.flat_price * item.cost_plus_percentage), 2) * item.quantity), 2) for item in order])

def Revenue_Receipt(order:list):
    receipt = ""
    total_revenue = 0
    for item in order:
        sale_reveue = round((round(item.flat_price + (item.flat_price * item.cost_plus_percentage), 2) * item.quantity), 2)
        total_revenue += sale_reveue
        receipt += "{} | {}{}".format(item.name, sale_reveue, "\n")
    receipt += "Total Revenue: " + str(total_revenue)
    return receipt

def Income(order:list):
    return Retail_Revenue(order) - Cost_Of_Goods(order)

def Financial_Statement(order:list):
    return 0

if __name__ == '__main__':
    
    admin_user = User("Jerry", [])

    production_order1 = Production_Order([
        Item("Apple", 0.12, 5000),
        Item("Banana", 0.15, 5000),
        Item("Peaches", 0.16, 5000),
    ])
    production_order2 = Production_Order([
        Item("Pears", 0.12, 5000),
        Item("Mangos", 0.15, 5000),
        Item("Strawberries", 0.16, 5000),
    ])
    
    admin_user.total_assets.append(Get_Assets(production_order1))
    admin_user.total_assets.append(Get_Assets(production_order2))
    print(admin_user.total_assets)

    order1 = [
        Item("Apple", 0.12, 2500),
        Item("Banana", 0.15, 2500),
        Item("Peaches", 0.16, 2500),
    ]
    
    order2 = [
        Item("Mango", 0.13, 2500),
        Item("Strawberry", 0.05, 2500),
        Item("Pineapple", 0.20, 2500),
        Item("Kiwi", 0.10, 2500),
        Item("Orange", 0.11, 25000),
        Item("Pear", 0.15, 2500),
    ]
    
    with open("datalog.txt", "w+") as DataLog:
        DataLog.write(str(Get_Assets(production_order1)) + "\n" * 2)
        DataLog.write(str(Cost_Of_Goods(order1)) + "\n" * 2)
        DataLog.write(str(Cost_Of_Goods(order2)) + "\n" * 2)
        DataLog.write(str(Expenses_Receipt(order1)) + "\n" * 2)
        DataLog.write(str(Expenses_Receipt(order2)) + "\n" * 2)
        DataLog.write(str(Retail_Revenue(order1)) + "\n" * 2)
        DataLog.write(str(Retail_Revenue(order2)) + "\n" * 2)
        DataLog.write(str(Revenue_Receipt(order1)) + "\n" * 2)
        DataLog.write(str(Revenue_Receipt(order2)) + "\n" * 2)
        DataLog.write(str(Income(order1)) + "\n" * 2)
        DataLog.write(str(Income(order2)) + "\n" * 2)
        
        for asset_group in admin_user.total_assets:
            for item in asset_group:
                DataLog.write(str(item) + "\n")
            DataLog.write("\n" * 2)