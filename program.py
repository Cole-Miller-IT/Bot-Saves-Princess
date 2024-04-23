#!/usr/bin/python

#https://www.hackerrank.com/challenges/saveprincess/problem using python 3

#Sample input from the user (each on a newline)
#3                  Dimensions of the grid(n). n x n grid size
#---                First Row
#-m-                Second Row
#p--                Third Row
#                   etc... if n is higher


#Goes from the middle of the grid to the top left corner then goes clockewise around to the other corners check for the princess
#once it reaches a new corner. Assumes the bot can see the whole grid.
def displayPathtoPrincess(n,grid):
    cornersChecked = 4
             #top left, top right, bot right, bot left
    corners = [0,           0,          0,      0]
    princessFound = False
    currentRow = n // 2
    currentCol = n // 2
    
    while(princessFound == False):
        if cornersChecked == 4:
            #At the start, go to the top left most corner
            #Go all the way to the left
            while(currentCol > 0):
                print("LEFT")
                currentCol = currentCol - 1
                
            #Go all the way up
            while(currentRow > 0):
                print("UP")
                currentRow = currentRow - 1
            
        else:
            #print("elseses")
            if corners[1] == 0:
                #print("one")
                #Move to the top right corner
                while(currentCol < (n - 1)):
                    print("RIGHT")
                    currentCol = currentCol + 1
            elif corners[2] == 0:
                #print("two")
                #Move to the bot right corner
                while(currentRow < (n - 1)):
                    print("DOWN")
                    currentRow = currentRow + 1
            else:
                #Move to the bot left corner
                #print("problem")
                while(currentCol > 0):
                    print("LEFT")
                    currentCol = currentCol - 1
         
        
        #Check if the princess is in this corner
        #print(currentRow)
        #print(currentCol)
        if (grid[currentRow][currentCol] == 'p'):
            #print("Princess found")
            princessFound = True
            break
        else:
            #print("Princess not found")
            cornersChecked = cornersChecked - 1
            
            if (currentRow == 0 and currentCol == 0):
                #print("top left")
                corners[0] = 1
            elif (currentRow == 0 and currentCol == (n - 1)):
                #print("top right")
                corners[1] = 1
            elif (currentRow == (n - 1) and currentCol == (n - 1)):
                #print("bot right")
                corners[2] = 1
            else:
                #print("bot left")
                corners[3] = 1
            
    

m = int(input())
grid = [] 
for i in range(0, m): 
    grid.append(input().strip())

displayPathtoPrincess(m, grid)