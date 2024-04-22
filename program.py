#print("Hello World!")
#!/usr/bin/python

def displayPathtoPrincess(n,grid):
    #print all the moves here
    print(n)    #NxN grid
    
    for row in range(n):
        print(grid[row])
        
    cornersChecked = 4
    princessFound = False
    while(princessFound == False):
        if cornersChecked == 4:
            #At the start, go to a random corner
        else:
        #if the princess is found, 
            #end
        #else 
            #determine what corner you are in
            #go to one of the other corners taking all of the same moves to reach it (treat the player as a Rook from                   Chess)
            #Go back and check if the princess is found
    

m = int(input())
grid = [] 
for i in range(0, m): 
    grid.append(input().strip())

displayPathtoPrincess(m,grid)