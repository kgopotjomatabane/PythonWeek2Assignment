
#Create an empty my_list
my_list = []

#Append elements 
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)

#Insert 15 at the second position
my_list.insert(1, 15)

#Extend list
my_list.extend([50, 60, 70])

#Remove the last element
my_list.pop()

#sort list in ascending order
my_list.sort()

#Find and print the index of the value 30 in my_list
index_of_30 = my_list.index(30)
print("Index of 30:" , index_of_30)

#print the final list
print("Final list:", my_list)

