import numpy as np

#Create a Data Frame from the input
def read_file(path):
    clean_data= []
    with open(path,'r') as file:
        raw_data= list(file)
        for line in raw_data:
            character_data = []
            line=line.rstrip()
            for number in line:
                character_data.append(int(number))
            clean_data.append(character_data)
        df_input= np.array(clean_data)
    return df_input

# Create a Step. Fisrt add one to every number. Search the points that are bigger than 10
# and add 1 to point adjacents. Reset to 0 the points that flash and count the number of flashes
def steps(data, number_of_steps):
    
    count= 0
    print(data)
    for step in range(number_of_steps):
        # Add 1 to every step
        print(step)
        data +=1
        bool = np.any(data >= 10)
        while bool == True:
            for x in range(10):
                for y in range(10):
                # Add 1 to adjancent point
                # For the middle values
                    if data[x][y] >= 10:
                        count +=1
                        data[x][y] = 0
                        try: #TOP-RIGHT
                            if data [x-1][y+1] != 0 and x != 0 and y !=9:
                                data[x-1][y+1] += 1
                        except:
                            pass
                        try: #RIGHT
                            if data[x][y+1] != 0 and y !=9 :
                                data[x][y+1] += 1
                        except:
                            pass
                        try: #BOTTOM-RIGHT
                            if data[x+1][y+1] != 0 and x != 9 and y !=9 :
                                data[x+1][y+1] += 1
                        except:
                            pass
                        try: #BOTTOM
                            if data[x+1][y] != 0 and x != 9 :
                                data[x+1][y] += 1
                        except:
                            pass
                        try: #BOTTOM LEFT
                            if data[x+1][y-1] != 0 and x != 9 and y !=0:
                                data[x+1][y-1] += 1
                        except:
                            pass
                        try: #LEFT
                            if data[x][y-1] != 0 and y !=0:
                                data[x][y-1] += 1
                        except:
                            pass
                        try: #TOP LEFT
                            if data[x-1][y-1] != 0 and x != 0 and y !=0:
                                data[x-1][y-1] += 1
                        except:
                            pass
                        try: #TOP
                            if data[x-1][y] != 0 and x != 0 :
                                data[x-1][y] += 1
                        except:
                            pass
            bool = np.any(data >= 10)
            #print(data)
        print('next step')
        print(data)     
    return count

#print(read_file('/Users/bzabert/Documents/Python/Adevent of code/Day 11/Aoc - day 11- input.txt'))
df_data=read_file('/Users/bzabert/Documents/Python/Adevent of code/Day 11/Aoc - day 11- input.txt')
#print(df_data)
print(steps(df_data, 100))