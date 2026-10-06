# 1st challenge
bill = 50
tip= 0.2*50
tips= print("tip =") 
print(tip)
total=tip+50
print("total=")
print(total)
# 4th challenge
score = 82
r=82
if r>=90:
    print("A")
elif r>=80:
    print("B")
elif r>=70:
    print("C")
elif r>60:
    print("D")
elif r>=50:
    print("F")
    # 8th challenge
first = "Ada"
last = "Lovelace"
school = "CSAEA"

print(f"Hello,my name is {first} {last} from {school}")
# 7th challenge
height = 50
age = 8
has_adult = True
if height<50: 
    print("sorry, you can't ride")
elif age<8:
    print("sorry you cant ride")
elif has_adult== False:
    print("sorry you can't ride")
elif height>=50:
    print("You can ride!")
elif age>=8:
    print("You can ride!")
elif has_adult==True:
    print("You can ride")

# challenge #5
password = "csaea2026"
attempt = "csaea2026"
 
# <Your Code Here>

if attempt=="CSAEA2026":
    print("Access denied")
elif attempt=="csaea2026":
    print("Access granted")
elif attempt!="csaea2026":
    print("Access denied")

#challenge #6
plate = 2242
 
if plate%2==0:
    print("park on east side")
else:
    print("park on west side")
#Example output:
#Park on the west side

# 9th challenge
cart = [12, 5, 30, 8]
print(f"List:{cart}")
print(f" Items= {(len(cart))}")
#total=sum(cart)

total=0
for j in range(0,len(cart)):
    total=total+cart[j]
print(f"Total=${total}")
#challenge 3
fahrenheit = 212
x=fahrenheit-32
c=x/1.8
print(c)
#challenge 10
groceries = ["milk", "eggs", "bread"]
print(groceries)
groceries.insert(0, "apples")
groceries.append("cheese")
groceries.append("lettuce")
print(groceries)
#challenge 20
speed_limit = 55
speed = 71
if speed>speed_limit:
    print("Fine:100$")
else:
    print("Speed limit: okay")