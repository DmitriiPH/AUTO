
#symbol = 20
#symbol *=20
#print(symbol)

#text = 'wdwad ergerg tutu'
#print('tutu' in text)


#abc = int(input('something write?'))
#abc = bool(input('something write?'))
#abc = str(input('something write?'))
#print('hi',type(abc),'!')


#arr = [1,2,3,4,5,6,'wergreg',None]

#print(arr)
#print(arr[6])
#print(arr[-1])

#arr[2] = 'str'
#print(arr)


# МАссивы это списки    . апенд - добавить, поп- удалить,
# arr_name = list() - объявление
#arr2 = [1,'2',3,4]
#arr2.append(42)
#arr2.append('123')
#print(len(arr2))
#print(arr2.index('2'))
#arr2.pop(2)
#print(arr2)
#print(4 in arr2)




# Кортежи - нельзя в них что-то добавлять или изменять
# tuple_name = tuple() - объявление
#  отличие не [] а ()

#kor = (1,2,3,4)
#kor[4] = 42
#print(kor) - 'это не верно'

#kor = (1) выведет число
#kor = (1,) выведет кортеж



# SET - множества. В нем только не повторяющиеся элементы. Нет порядка эл-ов. Мможно работать как и с массивом

#my_set = {1,2,3,4,5,"str",False,2.55}
#print(my_set)
#my_set.add(42) +
#my_set.add(5) - так как уже есть


#arr = [1,1,2,3,4,4,4,4,4]
#arr = set(arr)
#print(arr)

#obj = {}  - 'это словарь'
#set = set()   - " Это правильный пустой словарь"



#Словари - они же объекты

obj = {'key': 2}
print(obj)
print(len(obj))
obj['key2'] = 'dva'
print(obj)
print(obj.keys())
print(obj.values())
print(obj.items())