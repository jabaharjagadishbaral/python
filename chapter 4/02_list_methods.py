list=["apple","kanha",23,3.8,"jjb","bbb"]
print(list[0])
list.append("Jabahar")
print(list)

l1=[1,92,23,44,5]
#l1.sort()
#l1.reverse()
#l1.insert(3, 999999) # Insert 999999 such that its index in the list is 3
#print(l1.pop(3))
#value = l1.pop(3)
#print(value)
l1.remove(23)
print(l1)


numbers = [10, 20, 30]

numbers.append(40)
print(numbers)          # [10, 20, 30, 40]

numbers.extend([50, 60])
print(numbers)          # [10, 20, 30, 40, 50, 60]

numbers.insert(1, 15)
print(numbers)          # [10, 15, 20, 30, 40, 50, 60]

numbers.remove(30)
print(numbers)          # [10, 15, 20, 40, 50, 60]

numbers.pop()
print(numbers)          # [10, 15, 20, 40, 50]

print(numbers.index(40))   # 3
print(numbers.count(10))   # 1

numbers.sort()
print(numbers)          # [10, 15, 20, 40, 50]

numbers.reverse()
print(numbers)          # [50, 40, 20, 15, 10]

copy_list = numbers.copy()
print(copy_list)        # [50, 40, 20, 15, 10]

numbers.clear()
print(numbers)          # []