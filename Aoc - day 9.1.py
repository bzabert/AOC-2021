import numpy as np
import pandas as pd 

with open('/Users/bzabert/Documents/Python/Adevent of code/Day 9/AoC - day 9 input.txt', 'r') as file:
    raw_data=list(file)
    #print(raw_data)
    order= 0
    data= []
    
    for line in raw_data: 
        data.append(line.rstrip())
        #print(len(line.rstrip()))

    df_data = np.array(data)
    low_point= []

    for x in range(99):
        for y in range(99):
            if x == 0:
                if y == 0 :
                    if df_data[x][y] <= df_data[x+1][y] and df_data[x][y] <= df_data[x][y+1]:
                        low_point.append(df_data[x][y])
                elif y == 99:
                    if df_data[x][y] <= df_data[x+1][y] and df_data[x][y] <= df_data[x][y-1]:
                        low_point.append(df_data[x][y])
                else:
                    if df_data[x][y] <= df_data[x+1][y] and df_data[x][y] <= df_data[x][y-1] and df_data[x][y] <= df_data[x][y+1]:
                        low_point.append(df_data[x][y])
            elif x == 99:
                if y == 0 :
                    if df_data[x][y] <= df_data[x-1][y] and df_data[x][y] <= df_data[x][y+1]:
                        low_point.append(df_data[x][y])
                elif y == 99:
                    if df_data[x][y] <= df_data[x-1][y] and df_data[x][y] <= df_data[x][y-1]:
                        low_point.append(df_data[x][y])
                else:
                    if df_data[x][y] <= df_data[x-1][y] and df_data[x][y] <= df_data[x][y-1] and df_data[x][y] <= df_data[x][y+1]:
                        low_point.append(df_data[x][y])
            else:
                if df_data[x][y] <= df_data[x+1][y] and df_data[x][y] < df_data[x-1][y] and df_data[x][y] < df_data[x][y-1] and df_data[x][y] < df_data[x][y+1]:
                        low_point.append(df_data[x][y])
    
    #print(low_point)

    risk = 0
    for lpoin in low_point:
        risk += int(lpoin) +1
    
    print(risk)
