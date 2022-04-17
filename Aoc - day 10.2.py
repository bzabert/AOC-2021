
# Read the file and generate a list with the file
from binascii import Incomplete
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
    line_incorrect= []
    count= -1
    for line in list:
        count+=1
        secuence= []
        for character in line:
            if character == '[' or character == '{' or character == '(' or character == '<':
                secuence.append(character)
            elif character == ']':
                if secuence[-1] == '[':
                    del secuence[-1]
                else:
                    incorrect_character.append(character)
                    line_incorrect.append(count)
                    break
            elif character == ')':
                if secuence[-1] == '(':
                    del secuence[-1]
                else:
                    incorrect_character.append(character)
                    line_incorrect.append(count)
                    break
            elif character == '}':
                if secuence[-1] == '{':
                    del secuence[-1]
                else:
                    incorrect_character.append(character)
                    line_incorrect.append(count)
                    break
            elif character == '}':
                if secuence[-1] == '{':
                    del secuence[-1]
                else:
                    incorrect_character.append(character)
                    line_incorrect.append(count)
                    break
            elif character == '>':
                if secuence[-1] == '<':
                    del secuence[-1]
                else:
                    incorrect_character.append(character)
                    line_incorrect.append(count) 
                    break     
        
    return line_incorrect

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

# Eliminated the incorrect lines
def eliminated_incorrect(list, incorrect):
    for lines in reversed(incorrect):
        del list[lines]
    return list
    

# find the secuence to complete the string 
def complete_sequence(list):
    missing_sequence= []
    for line in list:
        secuence= []
        clossing_char = []
        for character in line:
            if character == '[' or character == '{' or character == '(' or character == '<':
                secuence.append(character)
            elif character == ']':
                if secuence[-1] == '[':
                    del secuence[-1]
            elif character == ')':
                if secuence[-1] == '(':
                    del secuence[-1]
            elif character == '}':
                if secuence[-1] == '{':
                    del secuence[-1]
            elif character == '}':
                if secuence[-1] == '{':
                    del secuence[-1]
            elif character == '>':
                if secuence[-1] == '<':
                    del secuence[-1]  
        secuence.reverse()
        #assing a value of each character
        for character in secuence:
            if character == '<':
                clossing_char.append(4)
            elif character == '(':
                clossing_char.append(1)
            elif character == '[':
                clossing_char.append(2)
            else:
                clossing_char.append(3)
        # Calculated the value of the srting and appended to a list
        score= 0
        for value in clossing_char:
            score = score * 5
            score += value
        missing_sequence.append(score)
    #missing_sequence.sort()
    return missing_sequence

#sort the list scores and select the middle value
def define_score(list):
    list.sort()
    middle_value= int(len(list)/2)
    result= list[middle_value]
    return result

data = read_file('/Users/bzabert/Documents/Python/Adevent of code/Day 10/AoC - day 10 input.txt')
inc_line= find_incorrect(data)
incomplete_lines= eliminated_incorrect(data, inc_line) 
#print(incomplete_lines)
print(define_score(complete_sequence(incomplete_lines)))