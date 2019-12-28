import sys
import math

# Don't let the machines win. You are humanity's last hope...

def searchX(x,i,j,w):
    for k in range(w-j):
        if j+k+1 == w:
            r = "-1 -1"
        elif(x[i][j+k+1]=='0'):
            r = "{} {}".format(j+k+1,i)
            break
    return r

def searchY(x,i,j,h):
    for k in range(h-i):
        if i+k+1 == h:
            b = "-1 -1"
        elif(x[i+k+1][j]=='0'):
            b = "{} {}".format(j,i+k+1)
            break
    return b
    

width = int(input())  # the number of cells on the X axis
height = int(input())  # the number of cells on the Y axis
x = ["" for x in range(height)]
r=""
b=""
print("width = {}, height = {}, x = {}".format(width,height,x), file=sys.stderr)

for i in range(height):
    x[i]= [x for x in input()]  # width characters, each either 0 or .

print("x = {}".format(x), file=sys.stderr)

for i in range(height):
    for j in range(width):
        r = searchX(x,i,j,width)
        b= searchY(x,i,j,height)
        if(x[i][j]=='.'):
            continue
        else:
            print("{} {} {} {}".format(j,i,r,b))
        
# Write an action using print
# To debug: print("Debug messages...", file=sys.stderr)


# Three coordinates: a node, its right neighbor, its bottom neighbor
