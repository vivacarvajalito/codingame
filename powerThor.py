import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.
# ---
# Hint: You can use the debug stream to print initialTX and initialTY, if Thor seems not follow your orders.

# light_x: the X position of the light of power
# light_y: the Y position of the light of power
# initial_tx: Thor's starting X position
# initial_ty: Thor's starting Y position
light_x, light_y, initial_tx, initial_ty = [int(i) for i in input().split()]
tx = initial_tx
ty = initial_ty
# game loop
while True:
    remaining_turns = int(input())  # The remaining amount of turns Thor can move. Do not remove this line.

    # Write an action using print
    # To debug: print("Debug messages...", file=sys.stderr)
    if(tx > light_x):
        if(ty>light_y):
            print('NW')
            tx -=1
            ty -=1
        if(ty<light_y):
            print('SW')
            tx -=1
            ty +=1
        if(ty==light_y):
            print('W')
            tx -=1
    if(tx < light_x):
        if(ty>light_y):
            print('NE')
            tx +=1
            ty -=1
        if(ty<light_y):
            print('SE')
            tx +=1
            ty +=1
        if(ty==light_y):
            print('E')
            tx +=1
    if(tx == light_x):
        if(ty>light_y):
            print('N')
            ty-=1
        if(ty<light_y):
            print('S')
            ty+=1

    # A single line providing the move to be made: N NE E SE S SW W or NW