import random
print('Hi we have here a shopping list. Take a look.')
shopping_list = ['cucumber', 'tomato', 'grapes', 'wine', 'water', 'carrot', 'juice']
for i in range(len(shopping_list)):
    print(shopping_list[i])

print('================================================')
shopping_list[0] = 'banana'
print(shopping_list, ' change before the ID')

added_list = ['Coca-cola', 'Pepsi', 'Fanta']
shopping_list[1:3] = added_list
print(shopping_list)

shopping_list.append('bitchez be crazy')
print(shopping_list)

shopping_list.reverse()
print(shopping_list)

shopping_list.remove('bitchez be crazy')
print(shopping_list)
