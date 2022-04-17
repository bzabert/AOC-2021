# Read the file and generate a list with the file
def read_file(path):
    with open(path,'r') as file:
        name= []
        file= list(file)
        for line in file:
            name.append(line.rstrip())
        return name

#Iterate through the list and fimd the incorret closing character
def find_incorrect(list):
    incorrect_character= []
    for line in list:
        secuence= []
        for character in line:
            if character == '[' or character == '{' or character == '(' or character == '<':
                secuence.append(character)

            elif character == ']':
                if secuence[-1] == '[':
                    del secuence[-1]
                else:
                    incorrect_character.append(character)
                    break
            elif character == ')':
                if secuence[-1] == '(':
                    del secuence[-1]
                else:
                    incorrect_character.append(character)
                    break
            elif character == '}':
                if secuence[-1] == '{':
                    del secuence[-1]
                else:
                    incorrect_character.append(character)
                    break
            elif character == '}':
                if secuence[-1] == '{':
                    del secuence[-1]
                else:
                    incorrect_character.append(character)
                    break
            elif character == '>':
                if secuence[-1] == '<':
                    del secuence[-1]
                else:
                    incorrect_character.append(character)  
                    break     
        
    return incorrect_character

#Add the charachter to a list and make the sum
def add_numbers(characters):
    result= 0
    one = 0
    two = 0
    three = 0 
    four =0
    for i in characters:
        if i == ')':
            one += 1
        elif i == '}':
            two += 1
        elif i == ']':
            three += 1
        else:
            four +=1
    result = one * 3 + two * 1197 + three * 57 + four *25137 
    return result




data = read_file('/Users/bzabert/Documents/Python/Adevent of code/Day 10/AoC - day 10 input.txt')
print(add_numbers(find_incorrect(data)))
