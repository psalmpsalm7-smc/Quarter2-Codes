destination=[]
print("Please input your 5 travel destinations:")

for i in range (1,6):
    dest=input(f"Enter place {i}: ")
    destination.append(dest)
print("Original travel itinerary:")

for f in range (0,5):
    print(f+1,".",destination[f])
print("Let's change your 2nd and 5th destinations.")

new_dest2=input("Enter new place for position 2: ")
new_dest5=input("Enter new place for position 5: ")
destination[1]=new_dest2
destination[4]=new_dest5
print("Updated travel itinerary:")
for f in range (0,5):
    print(f+1,".",destination[f])
