print("here is my diary: \n")
f1 = open("functions/files/diary.txt", "r")
print(f1.read())
f1.close()

print( "\nNow lets create another diary!")
f2 = open("functions/files/diary.txt", "w")
f2.write("Writing in my diary file.\n")
f2.close()