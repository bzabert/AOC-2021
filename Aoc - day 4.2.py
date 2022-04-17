from mimetypes import init
import socketserver
from unittest import result
import pandas as pd
import numpy as np

class BingoCard:
    def __init__(self, board) -> None:
        self.grid = np.array(board, dtype= int)

    def print(self):
        print(self.grid)

    def mark_number(self, number):
        for x in range(5):
            for y in range(5):
                if self.grid[x][y] == number:
                    self.grid[x][y] = -1
    
    def check_winer(self):
        for row in self.grid:
            if sum(row) == -5:
                return True
                break
        for x in range(5):
            if (self.grid[0][x]+self.grid[1][x]+self.grid[2][x]+self.grid[3][x]+self.grid[4][x]) == -5:
                return True
                break
        return False
    
    def winer(self):
        count= 0
        for x in range(5):
            for y in range(5):
                if self.grid[x][y] != -1:
                    count += self.grid[x][y]
        return count

        




def read_file(file):
    #Open a File
    with open(file, 'r') as file:
        file= list(file)
        # Create a list for a row, board and for boards. Other list is for the sequence of numbers
        one_board = []
        all_boards = []
        seq= []
        for i in file:
            # Cleans the data without spaces or commas
            line = i.rstrip()
            if len(line) == 289:
            #if len(line) == 20:
                seq= line.split(',')
            elif len(line) == 14:
                one_row = line.split(' ')
                while any(x == '' for x in one_row):
                    one_row.remove('')
                one_board.append(one_row)
                #print(len(one_row))
                if len(one_board)== 5:
                    board= BingoCard(one_board)  
                    all_boards.append(board)
                    #board.print()
                    one_board=[] 
        return seq, all_boards
     
sequence, boards = read_file('/Users/bzabert/Documents/Python/Adevent of code/Day 4/Aoc - day 4 - input.txt')

winers= []

for number in sequence:
    for board in boards:
        board.mark_number(int(number))    
        if board.check_winer() == True:
                if board not in winers:
                    winers.append(board)
        if len(boards)-len(winers) == 1:
            for board in boards:
                if board.check_winer() == False:
                    last_board= board
        if len(boards) == len(winers):
            score=last_board.winer()
            result= int(number) * score
            print(result)
            break
    else:
        continue
    break       
   
        
        