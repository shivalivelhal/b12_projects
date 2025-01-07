# # List
##--------------------------------------------------
# # Example-1
# list1 = [10,20,30,12.11,35.1,'apple',[1,2,3,4]]

# print(list1.__dir__())
# 'clear', 'copy', 'append', 'insert', 'extend', 'pop', 'remove', 'index', 'count', 'reverse', 'sort'

# print(list1)
# list1.append("10+1j")
# print(list1)           # o/p : [10, 20, 30, 12.11, 35.1, 'apple', [1, 2, 3, 4], '10+1j']

# list1.extend([202,203,204,202])  
# print(list1)           # o/p : [10, 20, 30, 12.11, 35.1, 'apple', [1, 2, 3, 4], '10+1j', 202, 203, 204,202]

# print(list1.count(202)) # o/p : 2

# list = list1.copy()
# print("New List = ",list)  # o/p : New List =  [10, 20, 30, 12.11, 35.1, 'apple', [1, 2, 3, 4], '10+1j', 202, 203, 204, 202]

# print(list1.index('apple')) # 5

# list1.insert(0,"abc")
# print(list1)   # o/p :['abc', 10, 20, 30, 12.11, 35.1, 'apple', [1, 2, 3, 4], '10+1j', 202, 203, 204, 202]

# sort_list = [12.22,-1.2,0,65,78.88,78.70,-3]
# sort_list.sort()
# print(sort_list)  # o/p : [-3, -1.2, 0, 12.22, 65, 78.7, 78.88]

# list1.reverse()  
# print(list1)      #o/p : [202, 204, 203, 202, '10+1j', [1, 2, 3, 4], 'apple', 35.1, 12.11, 30, 20, 10, 'abc']

# list1.remove('apple')
# print(list1)  #o/p :['abc', 10, 20, 30, 12.11, 35.1, [1, 2, 3, 4], '10+1j', 202, 203, 204, 202]

# list1.pop()
# list1.pop()
# list1.pop()
# print(list1)      # o/p : ['abc', 10, 20, 30, 12.11, 35.1, 'apple', [1, 2, 3, 4], '10+1j', 202]

# list1.clear()
# print(list1)      # o/p : []

# #Example-2

# student_data = ["roshni","mahutkar",23,{"address":"kolhapur","phone_num" : 1234567456},10j+12]
# print(student_data)
# print(student_data[3])   # prints the Dict
# student_data.append("CSE")
# print(student_data)

# student_data.extend(["DSA","C","C++","DBMS","CN"])
# print(student_data)

# print(student_data.count("roshni"))

# print(student_data.index({"address":"kolhapur","phone_num" : 1234567456}))

# student_data.insert(5,[98,87,98,76,65])
# print(student_data)

# sublist = student_data[5]
# print("SubList of student = ",sublist)
# sublist.sort()
# print(sublist)      #  [65, 76, 87, 98, 98]

# student_data1 = student_data.copy()
# print(student_data1)

# student_data1.remove({"address":"kolhapur","phone_num" : 1234567456})
# print(student_data1)

# student_data1.reverse()
# print(student_data1)

# student_data1.pop()
# student_data1.pop()
# print(student_data1)

# student_data1.clear()
# print(student_data1)

# #Example-3

# Emp_data = [{"name":"roshni","id": 2345678,"phone_num":9876543210},{"name":"Shivali","id": 132334,"phone_num":9876543210},{"name":"Shreya","id":6543678,"phone_num":9876543210}]
# print(Emp_data)

# Emp_data.append({"name":"Tejas","id": 2345678,"phone_num":9876543210})
# print(Emp_data)

# Emp_data.extend([10,10,20,30,40,50])
# print(Emp_data)

# print(Emp_data.count(10))

# Emp_data.insert(0,"SoftTech")
# print(Emp_data)

# copy_data = Emp_data.copy()
# print(copy_data)

# print(Emp_data.index("SoftTech"))

# Emp_data.remove(10)
# print(Emp_data)

# Emp_data.reverse()
# print(Emp_data)

# Emp_data.pop()
# Emp_data.pop()
# Emp_data.pop()
# print(Emp_data)

# Emp_data.clear()
# print(Emp_data)

#Example-4
# food_data = [
#     {  
#         "name": "Butter Chicken",
#         "price": 550,
#         "ingredients": {"Chicken", "Butter", "Tomato","Onion", "Spices"},  
#         "veg": False,  
#     },
#     {
#         "name": "Paneer Tikka",
#         "price": 250.10, 
#         "ingredients": {"Paneer", "Yogurt", "Spices", "Capsicum", "Onion"}, 
#         "veg": True,  
#     },
#     {
#         "name": "Chicken Biryani",
#         "price": 350, 
#         "ingredients": {"Rice", "Chicken", "Spices", "Yogurt", "Fried Onion"},
#         "veg": False,
#     },
   
# ]


# print(food_data)

# food_data.append({"name": "Chicken Fry","price": 350, "ingredients": {"Rice", "Chicken", "Spices", "Yogurt", "Fried Onion"},"veg": False,})
# print(food_data)

# food_data.extend([450,550,665,879,988])
# print(food_data)

# print(food_data.count(45))

# food_data.insert(0,"Food Data")
# print(food_data)

# copy_data = food_data.copy()
# print(copy_data)

# print(food_data.index(450))

# food_data.remove(988)
# print(food_data)

# food_data.reverse()
# print(food_data)

# food_data.pop()
# food_data.pop()
# food_data.pop()
# print(food_data)

# food_data.clear()
# print(food_data)

# Example - 5

# list = [23,63.3,('a','b','c'),{"even_num":[2,4,6,8],"odd_num":[1,3,5,7]},[12,43,4,2,1,3,4]]

# list.append("abcd")
# print(list)

# list.extend('apple')
# print(list)

# list1 = list.copy()
# print(list1)

# list.insert(2,222)
# print(list)

# print(list.index(63.3))

# print(list.count(222))

# num = list[5]
# print(num)

# num.sort()
# print(num)

# num.reverse()
# print(num)

# num.pop()
# num.pop()
# print(num)

# num.clear()
# print(num)
# print(list)

# list.remove(63.3)
# print(list)

##---------------------------------------------------------------
# Tuple
##---------------------------------------------------------------
## Example - 1
# tuple = (42,42, "hello", 3.14, [1, 2, 3])

# print(tuple.__dir__())
# 'index', 'count'

# print(tuple.count(42))
# print(tuple.index([1,2,3]))

## Example - 2
# tuple1 = ("a","b",2.34,[1,22,33],True,1)

# print(tuple1.count("a"))
# print(tuple1.index(True))

## Example - 3
# num = (1, 2, 3, 2, 2, 4)

# print(num.count(2))
# print(num.index(2,2,5))

# # Example - 4
# Emp = ("Roshni",101,55000.75,["Python", "SQL"],{"role": "Manager", "dept": "HR"},(3, 5, 7))

# print(Emp.count(55000.75))
# print(Emp.index({"role": "Manager", "dept": "HR"}))

#Example - 5

# fruit_data = ("Apple", 3, 9.81, {"Fruit": True, "Quantity": 10}, [1, 2, 3, 4], {7, 8, 9}, None)
# print(fruit_data.count([1, 2, 3, 4]))
# print(fruit_data.index(None))

##---------------------------------------------------------------
## Set
## 'add', 'clear', 'copy', 'difference', 'discard', 'intersection','pop', 'remove','union'
##---------------------------------------------------------------

# # Example 1
# fruit_set = {1, "apple", 3.5, "banana", True, (1, 2)}

# fruit_set.add("grape")
# print(fruit_set)

# set_copy = fruit_set.copy() 
# print(set_copy)

# diff_set = fruit_set.difference({3.5, "banana", (1, 2)})
# print(diff_set)

# fruit_set.discard("apple")  
# print(fruit_set)

# intersection_set = fruit_set.intersection({"banana", 1, (1, 2)}) 
# print(intersection_set)

# popped_element = fruit_set.pop()  
# print(popped_element)

# print(fruit_set)
# fruit_set.remove(3.5)  
# print(fruit_set)

# union_set = fruit_set.union({"kiwi", "orange"}) 
# print(union_set)

# fruit_set.clear()  
# print(fruit_set)

# # Example 2
# animal_set = {True, "dog", 7.8, (1, 1), 3.5, "cat"}

# animal_set.add("lion") 
# print(animal_set)

# my_copy = animal_set.copy()  
# print(my_copy)

# diff_set = animal_set.difference({"dog", (1, 1), "lion"})  
# print(diff_set)

# animal_set.discard(7.8)  
# print(animal_set)

# intersection_set = animal_set.intersection({"lion", "cat", 3.5}) 
# print(intersection_set)

# popped_element = animal_set.pop()  
# print(popped_element)
# print(animal_set)

# animal_set.remove("cat")  
# print(animal_set)

# union_set = animal_set.union({1, "elephant"}) 
# print(union_set)

# animal_set.clear()  
# print(animal_set)

# # Example 3

# color1 = {"red","blue","yellow","black","brown"}
# color2 = {"red","yellow","green","blue"}
# color1.add("purple")
# print(color1)

# color2.clear()
# print(color2) 

# color1.remove("blue")
# print(color1) 

# color_copy = color1.copy()
# print(color_copy)

# color1.discard("brown")
# print(color1) 
# color1.discard("green")  
# print(color1)

# result = color1.intersection(color2)
# print(result)

# result = color1.union(color2)
# print(result)

# result = color1.difference(color2)
# print(result)

# removed_item = color1.pop()
# print("Removed item: ",removed_item)
# print(color1)

# # Example 4: 

# student_set = {"rosh",23,(1,2,3,4)}

# student_set.add("CSE")  
# print(student_set)

# my_copy = student_set.copy()  
# print(my_copy)

# diff_set = student_set.difference((1,2,3,4))  
# print(diff_set)

# student_set.discard(23) 
# print(student_set)

# popped_element = student_set.pop()  
# print(popped_element)

# print(student_set)
# student_set.remove("CSE") 
# print(student_set)


#Dict


student_data = {
    "name": "Rosh",
    "age": 23,
    "grades": {"Math": 85, "English": 92, "Science": 88},
    "subjects": ["Math", "English", "Science"],
    "is_graduated": True
}

print(student_data)
print(student_data.get("name"))

print(student_data.pop("is_graduated"))
print(student_data)

print(student_data.popitem())
print(student_data)

new_dict = dict.fromkeys(["Address", "city"], "kop")
print(new_dict)

print(student_data.setdefault("is_graduated",True))
print(student_data)

student_data.clear()
print(student_data)

product_data = {
    "product_name": "Laptop",
    "price": 1000,
    "brand": "Dell",
    "stock": 50
}

print(product_data)
print(product_data.get("price"))

print(product_data.pop("brand"))
print(product_data)

print(product_data.popitem())
print(product_data)

new_product_dict = dict.fromkeys(["color", "warranty"], "unknown")
print(new_product_dict)

print(product_data.setdefault("stock", 100))
print(product_data)

product_data.clear()
print(product_data)

car_info = {
    "make": "Tesla",
    "model": "Model 3",
    "year": 2022,
    "color": "red"
}

print(car_info)
print(car_info.get("model"))

print(car_info.pop("color"))
print(car_info)

print(car_info.popitem())
print(car_info)

new_car_dict = dict.fromkeys(["owner", "license_plate"], "unknown")
print(new_car_dict)

print(car_info.setdefault("price", 50000))
print(car_info)

car_info.clear()
print(car_info)


order_info = {
    "order_id": 12345,
    "product": "Smartphone",
    "quantity": 2,
    "status": "Shipped"
}

print(order_info)
print(order_info.get("product"))

print(order_info.pop("status"))
print(order_info)

print(order_info.popitem())
print(order_info)

new_order_dict = dict.fromkeys(["shipping_address", "payment_method"], "pending")
print(new_order_dict)

print(order_info.setdefault("delivery_date", "2025-01-15"))
print(order_info)

order_info.clear()
print(order_info)


employee_info = {
    "employee_id": 456,
    "name": "Roshni",
    "department": "Development",
    "salary": 60000
}

print(employee_info)
print(employee_info.get("name"))

print(employee_info.pop("department"))
print(employee_info)

print(employee_info.popitem())
print(employee_info)

new_employee_dict = dict.fromkeys(["email", "phone"], "N/A")
print(new_employee_dict)

print(employee_info.setdefault("hire_date", "2024-07-15"))
print(employee_info)

employee_info.clear()
print(employee_info)



# String

text = "  an apple a day keeps a doctor away  "

print(text.strip())
print(text.lstrip())
print(text.rstrip())
print(text.split())
print(text.capitalize())
print(text.lower())
print(text.upper())
print(text.title())
print(text.swapcase())
print(text.isalnum())
print(text.isnumeric())
print(text.isupper())
print(text.count("a"))
print(text[3:10])
print(text.startswith("  "))
print(text.index("apple"))
print(text.find("doctor"))
print(text.replace("apple", "orange"))


text = "  welcome to python programming  "

print(text.strip())
print(text.lstrip())
print(text.rstrip())
print(text.split())
print(text.capitalize())
print(text.lower())
print(text.upper())
print(text.title())
print(text.swapcase())
print(text.isalnum())
print(text.isnumeric())
print(text.isupper())
print(text.count("o"))
print(text[2:15])
print(text.startswith("  "))
print(text.index("python"))
print(text.find("programming"))
print(text.replace("python", "Java"))


text = "  Learning Python is fun and rewarding  "

print(text.strip())
print(text.lstrip())
print(text.rstrip())
print(text.split())
print(text.capitalize())
print(text.lower())
print(text.upper())
print(text.title())
print(text.swapcase())
print(text.isalnum())
print(text.isnumeric())
print(text.isupper())
print(text.count("n"))
print(text[2:15])
print(text.startswith("  "))
print(text.index("Python"))
print(text.find("fun"))
print(text.replace("fun", "exciting"))


text = "  Success depends on hard work and perseverance  "

print(text.strip())
print(text.lstrip())
print(text.rstrip())
print(text.split())
print(text.capitalize())
print(text.lower())
print(text.upper())
print(text.title())
print(text.swapcase())
print(text.isalnum())
print(text.isnumeric())
print(text.isupper())
print(text.count("e"))
print(text[3:18])
print(text.startswith("  "))
print(text.index("hard"))
print(text.find("work"))
print(text.replace("perseverance", "work"))


text = "  Data Science is transforming the world  "

print(text.strip())
print(text.lstrip())
print(text.rstrip())
print(text.split())
print(text.capitalize())
print(text.lower())
print(text.upper())
print(text.title())
print(text.swapcase())
print(text.isalnum())
print(text.isnumeric())
print(text.isupper())
print(text.count("s"))
print(text[5:15])
print(text.startswith("  "))
print(text.index("transforming"))
print(text.find("the"))
print(text.replace("Science", "Engineering"))
