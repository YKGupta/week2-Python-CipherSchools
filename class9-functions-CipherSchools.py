def sayHemlo():
    for _ in range(3):
        print("Hemlo")

print("Good morning, this program")
sayHemlo()
print("..., uhum uhum..., sorry for th—")
sayHemlo()
print("....")
sayHemlo()
print("Shuttt itt!")
sayHemlo()
print(":-|")

def sayHemlo(name):
    for _ in range(3):
        print("Hemlo", name)

sayHemlo("Yash")

def sayHemlo(name, times = 3):
    for _ in range(times):
        print("Hemlo", name)

sayHemlo("Yash", 100)