#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp


with open("Day 024/Mail Merge Project Start/Input/Names/invited_names.txt", mode ="r") as lines:
    names = lines.readlines()


with open("Day 024/Mail Merge Project Start/Input/Letters/starting_letter.txt", mode ="r") as letter:
    original_letter = letter.read()

for name in names:
    txt = name.strip("\n")
    path = f"Day 024/Mail Merge Project Start/Output/ReadyToSend/{txt}.txt"
    with open(path, mode ="w") as text:
        text.write(original_letter)
    with open(path, mode ="r") as text:
        new_text = text.read()   
    new_text.replace("[name]", txt)
    with open(path, mode ="w") as text:
        text.write(new_text)
