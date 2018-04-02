print('simple assignment')
shoplist = ['apple', 'mango', 'carrot', 'banana']
mylist = shoplist

del shoplist[0]

print('shoplist is ', shoplist)
print('mylist is ', mylist)

print('copy by makeing a full slice')
# mylist = shoplist[:]

del shoplist[0]

print('shoplist is ', shoplist)
print('mylist is ', mylist)
