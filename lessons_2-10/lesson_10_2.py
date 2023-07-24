str1 = input("Enter your text: ")
str2 = input("Enter your text: ")
str3 = input("Enter your text: ")
str4 = input("Enter your text: ")

file = open("new.txt", "w")
for elem in (str1, str2):
    file.write(f"{elem}\n")
file.close()

file = open("new.txt", "a")
for elem in (str3, str4):
    file.write(f"{elem}\n")
