menu = list()
print(type(menu)) 
print("First menu print", menu)
house_chores= []
print(type(house_chores))

menu.append("Tomatoes")
print("Second menu print", menu)
menu.append("Potatoes")
print("Third menu print", menu)
menu.append("Onions")
print("Fourth menu print", menu)
menu.append("Carrots")
print("Fifth menu print", menu)
menu.append("Cucumbers")
print("Sixth menu print", menu)

names = ["Alice", "Bob", "Charlie", "David"]
print("Names list:", names)

print("Printing the third name", names[1:3])  # This will print names from index 1 to 2 (Bob and Charlie)

class_roster = ["Alice", "Bob", "Charlie", "David"]
test_scores = [85, 90, 78, 92]

print("Class roster:", class_roster)
print("Test scores:", test_scores)

print("Class roster length:", len(class_roster))
print("Test scores length:", len(test_scores))

print("Class roster first name:", class_roster[0])
print("Test scores first score:", test_scores[0])

print("Class roster last name:", class_roster[-1])
print("Test scores last score:", test_scores[-1])

print("Class roster first three names:", class_roster[:3])
print("Test scores last two scores:", test_scores[-2:])

print("Class roster names from index 1 to 3:", class_roster[1:4])
print("Test scores from index 1 to 3:", test_scores[1:4])

print("Class roster names from index 2 to end:", class_roster[2:])

print("Test scores from index 2 to end:", test_scores[2:])

customers = [
    {
        "customer id": 0,
        "first name": "Alice",
        "last name": "Smith",
        "address": "123 Main St, Springfield",
    }
    {
        "customer id": 1,
        "first name": "Bob",
        "last name": "Johnson",
        "address": "456 Elm St, Springfield",
    },
    {
        "customer id": 2,
        "first name": "Charlie",
        "last name": "Brown",
        "address": "789 Oak St, Springfield",
    },
    {
        "customer id": 3,
        "first name": "David",
        "last name": "Williams",
        "address": "101 Pine St, Springfield",
    }
]