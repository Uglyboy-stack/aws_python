def demo(n):
	w = n + 3
	return w
print(demo(7))

n = int(input("Enter a value for n: "))
print(demo(n))
values = [1, 5, 10]

for n in values:
	print(f"demo({n}) = {demo(n)}")
	
def demo():
	n = int(input("Enter a value for n: "))
	w = n + 3
	return w

print(demo())    