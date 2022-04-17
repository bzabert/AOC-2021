from audioop import reverse
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
        x_len= len(line)-1
    #print(x_len)
    y_len=len(raw_data)
    #print(y_len)
    

    df_data = np.array(data)
    low_point= []
    coord= []

    for x in range(x_len-1):
        for y in range(y_len-1):
            if x == 0:
                if y == 0 :
                    if df_data[x][y] <= df_data[x+1][y] and df_data[x][y] <= df_data[x][y+1]:
                        low_point.append(df_data[x][y])
                        coord.append([x,y])
                elif y == 99:
                    if df_data[x][y] <= df_data[x+1][y] and df_data[x][y] <= df_data[x][y-1]:
                        low_point.append(df_data[x][y])
                        coord.append([x,y])
                else:
                    if df_data[x][y] <= df_data[x+1][y] and df_data[x][y] <= df_data[x][y-1] and df_data[x][y] <= df_data[x][y+1]:
                        low_point.append(df_data[x][y])
                        coord.append([x,y])
            elif x == 99:
                if y == 0 :
                    if df_data[x][y] <= df_data[x-1][y] and df_data[x][y] <= df_data[x][y+1]:
                        low_point.append(df_data[x][y])
                        coord.append([x,y])
                elif y == 99:
                    if df_data[x][y] <= df_data[x-1][y] and df_data[x][y] <= df_data[x][y-1]:
                        low_point.append(df_data[x][y])
                        coord.append([x,y])
                else:
                    if df_data[x][y] <= df_data[x-1][y] and df_data[x][y] <= df_data[x][y-1] and df_data[x][y] <= df_data[x][y+1]:
                        low_point.append(df_data[x][y])
                        coord.append([x,y])
            else:
                if df_data[x][y] <= df_data[x+1][y] and df_data[x][y] < df_data[x-1][y] and df_data[x][y] < df_data[x][y-1] and df_data[x][y] < df_data[x][y+1]:
                        low_point.append(df_data[x][y])
                        coord.append([x,y])
    
    #print(low_point)

    risk = 0
    for lpoint in low_point:
        risk += int(lpoint) +1
    
    #print(risk)
    #print(coord)

    def basin(matrix, x, y, x_end, y_end, cell_analised):
        if x < 0 or y < 0 or x > x_end or y > y_end \
                or int(matrix[x][y]) == 9 \
                or (x, y) in cell_analised:
            return

        cell_analised.append((x, y))

        basin(matrix, x, y + 1, x_end, y_end, cell_analised)
        basin(matrix, x, y - 1, x_end, y_end, cell_analised)
        basin(matrix, x + 1, y, x_end, y_end, cell_analised)
        basin(matrix, x - 1, y, x_end, y_end, cell_analised)
        
    

    
    len_basis= []
    for lpoint in coord:
        #print(lpoint) 
        x,y = lpoint
        cells= []
        basin(raw_data, x, y, x_len-1, y_len-1, cells)
        len_basis.append(len(cells))
        #print(cells)
    len_basis.sort()
    result=len_basis[-1]*len_basis[-2]*len_basis[-3]
    print(result)    


        

    
