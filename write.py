user_input = input("Enter some data: ")

with open("output.txt", "w") as file:
    file.write(user_input + "\n")

print("Data written to output.txt successfully.")
append_data = input("Enter additional data to append: ")

with open("output.txt", "a") as file:
    file.write(append_data + "\n")

print("Additional data appended successfully.")
print("\nFinal content of output.txt:")
with open("output.txt", "r") as file:
    for line in file:
        print(line.strip())
