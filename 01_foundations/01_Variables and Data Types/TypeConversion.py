# int → float

a = 10
print(float(a))

# float → int

b = 20.88
print(int(b))

# int → str

c = 100
converted = str(c)
print(str(c))
print(type(converted))

# str → int

a = "50"
print(int(a))

# str → float

price = "99.5"
print(float(price))

# int → bool
print(bool(1))
print(bool(100))


# isinstance()
# Professional code me type() se zyada isinstance() use hota hai, kyunki inheritance ko bhi handle karta hai.

age = 20
print(isinstance(age, int))

# id() kisi object ki identity (CPython me aam taur par uska memory address) return karta hai.

x = 100

print(id(x))

a = [1, 2]
b = [1, 2]

print(a == b)
print(a is b)

# == → values compare karta hai.
# is → check karta hai ki dono variables same object ko refer kar rahe hain ya nahi.