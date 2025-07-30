buy_score = 0

donut_condition = "stale"  # Options: fresh, stale

donut_filling = "chocolate"  # Options: chocolate, vanilla, strawberry

donut_price = "unreasonable"  # Options: reasonable, expensive

if donut_condition == "fresh":
    buy_score += 10
    
if donut_filling == "chocolate":
    buy_score += 5
    
if donut_price == "reasonable":
        buy_score += 7
        
print("Buy score:", buy_score)        


first_names = ["John", "Jane", "Doe", "Alice", "Bob"]
last_names = ["Smith", "Doe", "Johnson", "Brown", "Davis"]
full_names = []

for a_first_name in first_names:
    for a_last_name in last_names:
        full_names.append(a_first_name + " " + a_last_name)
        
print(full_names)        
