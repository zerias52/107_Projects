print("hello from python")
# similar to console.log("hello from python")

# let variable = 1;
variable = 1
variable = True
variable = "hello"

array = [1, 2, 3, 4, 5]
print(array[4])
array.append(6)
print(array)
print(array.pop())
print(array)


dict = {
    "name":"Brett",
    "last_name":"Byrd",
}

print(dict)
print(dict["name"])

# for(i=0; i<array.length; i++){
# let temp = array[i]
# console.log(temp)}

for numbers in array:
    print(numbers)

for i in dict:
    print(dict[i])

def hello():
    print("hello from python function")

def goodbye(name):
    print("Goodbye " + name)

hello()
goodbye("Brett")