greet = "hello World"
extened_grt = "Hello World, " + "this is a long string"


name = "John"

intrupution = f"Hello {name}"

greet_format = "Hello {}"

formatted = greet_format.format(name)

print(intrupution, formatted)
print(formatted.replace("John", "Adam"))

quantity = 3
itemno = 567
price = 49
myorder = f"I want {quantity} pieces of item number {itemno} for {price:.2f} dollars."
print(myorder)
