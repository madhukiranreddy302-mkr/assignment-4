try:
    with open("sample.txt", "r") as file:
        print("File contents:")
        for line in file:
            print(line.strip())
except FileNotFoundError:
    print("Error: The file 'sample.txt' does not exist.")

