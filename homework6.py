my_dict = {"name": "Maksim",
           "age": 23,
           "city": "Rostov-on-don"}
print(my_dict)
print(my_dict["name"])
print(my_dict.get("country", "Набор ключей не существует "))
my_dict["district"] = "Nakhicheva"
my_dict["street"] = "Selmashskaya"
removed_value = my_dict.pop("age")
print(removed_value)
print(my_dict)

my_set = {1, 2.5, "hello", True, 1, 2.5}
print(my_set)
my_set.add(3)
my_set.add("world")
my_set.remove(1)
print(my_set)