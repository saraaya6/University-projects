
area = input("Choose an area: (Cairo), (Alexandria), or (Tanta): ").lower()

if area == "cairo" or area == "alexandria" or area == "tanta":
    print(f"{area} is on our list!")
else:
    print(f"Sorry, {area()} is not on our list!")
