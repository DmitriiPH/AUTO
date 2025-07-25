#asd = int(input('Input msg'))

#if asd == 1:
#    print('one')
#elif asd == 2:
#    print('two')
#else:
#    print('efwefwfwefwef')



#arr = ['one', 'two', 'ttre', 'for']

#for num in arr:
    #if 'o' in num :
        #print(num)


#obj = {'k1': 123, 'k2':33333, 'k3':135}
#for ooo in obj:
    #print(ooo)
    #print(obj[ooo])


#obj = {'k1': 123, 'k2':33333, 'k3':135}
#for ooo in obj.values():
   
#    print(ooo)

#obj = {'k1': 123, 'k2':33333, 'k3':135}           печать как вб 
#for ooo in obj:
   
#    print(f'{ooo}: {obj[ooo]}')


#obj = {'k1': 123, 'k2':33333, 'k3':135}       как кортеж
#for ooo in obj.items():
    
#    print(ooo)


#obj = {'k1': 123, 'k2':33333, 'k3':135}     как в бд
#for ooo in obj.items():
#    name, num = ooo
#    print(f'{name} : {num}')


#obj = {'k1': 123, 'k2':33333, 'k3':135}     как в бд оптимизация
#for name, num in obj.items():    
#    print(f'{name} : {num}')

text = 'one o sdlsdg  oohhj lmnfp'

words = text.split()
fin = []
for zzz in words:
    if 'o' not in zzz:
        fin.append(zzz)
print(fin)