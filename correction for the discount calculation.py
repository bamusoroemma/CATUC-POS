print('welcome of CATUC POS')
num_items = int(input('please enter how many items purchased\n'))
items_cost= []
total_quantity=0

for item in range(1,num_items +1):
      item_name=input('please enter the item name\n')
      item_quantity=int(input(f'please enter the quantity of {item_name }\n'))
      unit_price= int(input(f" please enter unit price of '{item_name}'\n"))
      total_price=unit_price * item_quantity
      print( f' the total price of {item_name} is = {total_price}\n')    
      items_cost.append(total_price)
items_cost_total = sum(items_cost)
if items_cost_total >= 10000 :
    discount = (0.30 * items_cost_total)
    print(f' the items_cost_total is = {items_cost_total} ')
    print(f' your discount is = {discount} ')
    total_cost = items_cost_total - discount
    print(f' tatal purchase = { total_cost} frs\n thanks for your patronage')
elif (len(items_cost) > 5) and (items_cost_total > 4000) :
    discount = 0.15 * items_cost_total
    print(f' the items_cost_total is = {items_cost_total} \n')
    print(f' your discount is = {discount} \n')
    total_cost = items_cost_total - discount
    print(f' total purchase = {total_cost} frs\nthanks for your patronage')
else :
    total_cost = items_cost_total
    print(f'total purchase = {total_cost} frs\n thanks for your patronage')
