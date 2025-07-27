#i=0 
#while i < 5:
#    print('*')
#    i+=1


#while True:
#    asd = input('dre')
#    if asd == 'exit':
#        print('yes')
#        break
#    elif asd == 'www':
#        print("continue")
#        continue
#    else:
#        print('try again')

#print('bye')


#a=1
#b=2
#c=3
#d=4

#main = 33

#def calc(num):
#    num + main
#    print()

def price (**kwargs):
    for title, price in kwargs.items():
        print(f'Product {title} price is {price}')

price(a=111,b=222,c=333)