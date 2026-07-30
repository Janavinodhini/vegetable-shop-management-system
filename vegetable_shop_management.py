"""
Project: Vegetable Shop Management System

Description:
A Python console application to manage vegetable inventory,
customer billing, discounts, revenue, profit calculation,
and stock availability.

Developed using Python.
"""



vegetables=["tomato","brinjal","onion"]
quantity=[10,12,25]
prices=[20,30,40]
print("-"*30)
print("WELCOME TO VEGETABLE SHOP MANAGEMENT SYSTEM")
print("-"*30)
print("1.Add New Vegetable")
print("2.Update price and quantity")
print("3.Continue Billing")
while True:
    extra=input("Do you want to add another vegetable? (yes/no): ")  
    if extra=="yes":
        itemadd=input("Enter new vegetable")    #add new vegetable
        vegetables.append(itemadd)
        addqua=int(input("Enter quantity"))
        quantity.append(addqua)
        addprice=int(input("addprice"))
        prices.append(addprice)
    else:
        break
print("\nAvailable Vegetables")
for i in zip(vegetables, quantity, prices):
    print(f"{i[0]} --> {i[1]} kg --> {i[2]}/kg")
discounted_revenue=0
revenue_without_discount=0
total_profit=0
print(len(vegetables))
profit_per_item=[]
for i in range(0,len(vegetables)):
    profit_per_item.append(0)
print(profit_per_item)
purchase_cost=0
total_purchase_cost=0
purchase_price=[]
for i in range(0,len(vegetables)):
    originalamountbrought=int(input("Enter Purchase Price"))
    purchase_price.append(originalamountbrought)
for i in range(0,len(vegetables)):
    purchase_cost=quantity[i]*purchase_price[i]
    total_purchase_cost=total_purchase_cost+purchase_cost
print(f"Total Purchase Cost: {total_purchase_cost}")


while True:
    total=0
    customer_items=[]
    customer_quantity=[]
    item_bill=[]
    while True:
        item=input("Enter vegetable name: ")
        customer_items.append(item)
        if item in vegetables:
            print(f"{item} is available. ")
            kg=float(input("Enter quantity (kg): "))
            customer_quantity.append(kg)
            idx=vegetables.index(item)
            if kg<=quantity[idx]:
                quantity[idx]=quantity[idx]-kg
                selling_price=prices[idx]*kg
                item_bill.append(selling_price)
                total=total+(prices[idx]*kg)
                print(kg,"*",prices[idx],"-->","pay for each item",selling_price)
                #purchase_price=[18,27,38]
                buying_price=purchase_price[idx]*kg
                c=selling_price-buying_price
                if buying_price<selling_price:
                    print(f"Profit on this item: {selling_price-buying_price}")
                    profit_per_item[idx]=profit_per_item[idx]+c
            else:
                print(item," is out of stock")
        else:
            print(f"{item} is not available.")
        otheritem=input("you want other item say yes/no")
        if otheritem=="no":
            print("*"*10,"*"*18,"*"*10)
            break
    print(f"Total Amount: {total}")
    print("*"*10,"bill of customer","*"*10)
    for i in zip(customer_items,customer_quantity,item_bill):
        print(i[0],"-->",i[1],"-->",i[2])
    dis=input("enter discount yes/no")
    if dis=="yes":
        discount=int(input("enter discount"))
        print(f"Discount Applied: {discount}%")
        pay=total-((discount/100)*total)
        print("total is",total)
        print(f"Amount to pay: {pay}")
        discounted_revenue=discounted_revenue+pay
    else:
        print(f"No discount applied. Amount to pay: {total}")
        revenue_without_discount=revenue_without_discount+total
    print("*"*10,"end of customer bill","*"*10)
    print("-->"*18,"-->"*11)
    ch=input("you  want to close the shop enter yes/no")
    if ch=="yes":
        revenue=discounted_revenue+revenue_without_discount
        print(f"Total Revenue: {revenue}")
        if purchase_cost<revenue:
            print(f"Total Profit: {revenue-purchase_cost}")    #Caculate Profit
        else:
            for i in range(0,len(profit_per_item)):
                total_profit=total_profit+profit_per_item[i]
            print(total_profit)
            if total_profit>0:
                print("your profit is",total_profit)
            else:
                print("there is  no profit")
        for it in zip(vegetables,quantity):
            print(f"{it[0]}-->{it[1]}kg")
        print("="*50)
        print("SHOP CLOSED SUCCESSFULLY")
        print("THANK YOU FOR USING VEGETABLE SHOP MANAGEMENT SYSTEM")
        print('='*50)
        for i in zip(vegetables,profit_per_item,):
            print(i[0],"-->",i[1])
        for i in range(0,len(quantity)):
            if quantity[i]<=0 and profit_per_item[i]>=0:
                print("you can bring more",vegetables[i],"because its quantity is 0 and profit is ",profit_per_item[i])
        break
    else:
        Another_customer=input("Is there another customer? (yes/no): ")
        customer_count=int(input("enter no of customer"))
        if Another_customer == "yes":
            print("No of customers:", customer_count)
        else:
            print("No other customer")
      
            
      
    
   
    
            
        
