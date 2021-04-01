#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp


lines = open("Day 024/Mail Merge Project Start/Input/Names/invited_names.txt", mode ="r")
names = lines.readlines()
print(names)


letter = open("Day 024/Mail Merge Project Start/Input/Letters/starting_letter.txt", mode ="r")
original_letter = letter.read()

for name in names:
    txt = name.strip("\n")
    anterior_name = "[name]"
    path = f"Day 024/Mail Merge Project Start/Output/ReadyToSend/{txt}.txt"
    with open(path, mode ="w") as text:
        text.write(original_letter.replace(anterior_name, txt))
        anterior_name = txt

letter.close()
lines.close()