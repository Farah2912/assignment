numbers = [12, 75, 150, 180, 145, 525, 50]
results = []

for item in numbers:
    if item > 500:
        break

    if item > 150:
        continue

    if item % 5 == 0 :
        results.append(item)

print(results)



for i in range(5):
    print(i)
print("Done!")



number = 76542
number_reversed = str(number)[::-1]
print(number_reversed)

key = ["Ten", "Twenty", "Thirty"]
values = [10, 20, 30]
dictionary = dict(zip(key, values))
print(dictionary)
dict = {"Ten":10 ,
        "Twenty":20 ,
        "Thirty": 30
        }
print(dict)






sample_dict = {
    "name" : "kelly" ,
    "age" : 25 ,
    "salary" : 8000 ,
    "city" : "New york"
}
sample_dict.pop("name" )
sample_dict.pop("salary")
print(sample_dict)


sample_set = {"yellow", "orange", "Black"}
sample_list = ["Blue", "Green", "Red"]
sample_set.update(sample_list)
sample = sample_set.union(sample_list)
print(sample_set)
print(sample)



set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}
print(set1.intersection(set2))



tuble1 = [10, 20, 30, 40, 50]
tuble1.reverse()
print(tuble1)



tublle1 = ["orange" , [10, 20, 30],(5, 15, 25)]
result = tublle1[1]
print(result[1])


tuple11 = [10, 20, 30 ,40]
your_code = input("enter your code:")
if your_code == "a":
    print(10)
elif your_code == "b" :
    print(20)
elif your_code == "c" :
    print(30)
elif your_code == "d" :
    print(40)

