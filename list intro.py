my_list = ['1','2','3']
a_list = ['4','5','6']
print( my_list + a_list)
print(my_list)

#merging lists
new_list = my_list + a_list
print( new_list)
print(new_list[:4])

#changing any elements
new_list[0]= "ALL caps"
print(new_list[0])
print(new_list)

#just for fun 
type(new_list)
len(new_list)

#to add new elements on list
new_list.append('7')
print(new_list) 

#to remove elements on list
new_list.pop()
print(new_list)

#to remove element on 1 list and add in another list
popped_ele = new_list.pop()
print(new_list)

#to .pop on specific elements
new_list.pop(2) # '3' is removed
print(new_list)
      
 #to sort the elements into order
num_list = ['3','4','8','1','99','69','420']
num_list.sort()
print(num_list)

#dictionary
prices =  {'apple':150,"orange":75,"kiwi":200}
print(prices['apple'])
print(prices['kiwi'])

# 1 number dictionaries in one single dictionary
no_prices = {'biryani':210, 'khuska':150,'naan':{'parotta':45,'butter_naan':50}}
print(no_prices['naan']['parotta'])

#many dictionaries in one main dictionary
menu_prices = {'fruits':{'apple':49.99,'orange':29.99,'banana':15.99},'veges':{'onion':19.99,'cucumber':9.99,'carrot':29.99},'meat':{'mutton':699,'chicken':199,'fish':449}}
print(menu_prices['meat']['mutton'])
