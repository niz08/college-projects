#Smart Bill Generator Project [CIT Project]

print("*"*50)
print("\t Welcome to Byte Brew Cafe!")
print("*"*50)

total=0
d={}
newtotal=0

##getting item input:

while True:
    item_name=input("\nEnter Item Name:")
    item_quantity=int(input("\nEnter Quantity:"))
    item_price=float(input("\nEnter Price:"))
    final_price=item_quantity*item_price
    d[item_name]=[item_quantity,final_price]
    ch=input("\nAdd More? [Y/N]")
    if ch.lower() in "n":
        break
print("-"*50)

##printing each item:

print("Total Items:")
for i in d:
    print(f"\nItem:{i}\nQuantity:{d[i][0]}\nPrice:{d[i][1]}")
    total+=d[i][1]
print("-"*50)

#applying discount:

dis=input("\nEnter Discount? [Y/N]")
if dis.lower() in "y":
    discount=int(input("Enter Discount Amount:"))
    newtotal=total-total*discount/100

##adding tax:
    
tax=int(input("\nEnter Tax Amount:"))
newtotal=newtotal+newtotal*tax/100
print("-"*50)

##final bill:

print("\nFinal Bill")
print(f"\nSubtotal:{total}")
print(f"Discount Applied:{dis}")
print(f"Tax Applied:{tax}")
print(f"Final Total:{newtotal}")
print("-"*50)

