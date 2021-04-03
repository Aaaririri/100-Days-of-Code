with open("Day 026/file/file1.txt") as file:
    file1 = file.readlines()
file1 = [item.strip("\n") for item in file1]

with open("Day 026/file/file2.txt") as file:
    file2 = file.readlines()
file2 = [item.strip("\n") for item in file2]

result = [int(item) for item in file1 if item in file2]
print(result)