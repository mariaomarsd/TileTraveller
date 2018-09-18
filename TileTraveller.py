x = 1
y = 1
invalid = False

while 1 <= x <= 3 and 1 <= y <=3:

    if 1 <= x <= 2 and y == 1:
        if invalid == False:
            print("You can travel: (N)orth.")
        direction = str(input(("Direction: ")))
        direction = direction.lower()
        if direction == 'n':
            y+=1
            invalid = False
        else:
            invalid = True
            print("Not a valid direction!")
    elif x == 1 and y == 2:
        if invalid == False:
            print("You can travel: (N)orth or (E)ast or (S)outh.")
        direction = str(input(("Direction: ")))
        direction = direction.lower()
        if direction == 'n':
            invalid = False
            y+=1
        elif direction == 's':
            invalid = False
            y-=1
        elif direction == 'e':
            invalid = False
            x+=1
        else:
            invalid = True
            print("Not a valid direction!")
    elif x == 1 and y == 3:
        if invalid == False:
            print("You can travel: (E)ast or (S)outh.")
        direction = str(input(("Direction: ")))
        direction = direction.lower()
        if direction == 's':
            invalid = False
            y-=1
        elif direction == 'e':
            invalid = False
            x+=1
        else:
            invalid = True
            print("Not a valid direction!")
    elif x == y and x != 1:
        if invalid == False:
            print("You can travel: (S)outh or (W)est.")
        direction = str(input(("Direction: ")))
        direction = direction.lower()
        if direction == 's':
            invalid = False
            y-=1
        elif direction == 'w':
            invalid = False
            x-=1
        else:
            invalid = True
            print("Not a valid direction!")
    elif x == 2 and y == 3:
        if invalid == False:
            print("You can travel: (E)ast or (W)est.")
        direction = str(input(("Direction: ")))
        direction = direction.lower()
        if direction == 'e':
            invalid = False
            x+=1
        elif direction == 'w':
            invalid = False
            x-=1
        else:
            invalid = True
            print("Not a valid direction!")
    elif x == 3 and y == 2:
        if invalid == False:
            print("You can travel: (N)orth or (S)outh.")
        direction = str(input(("Direction: ")))
        direction = direction.lower()
        if direction == 'n':
            invalid = False
            y+=1
        elif direction == 's':
            invalid = False
            y-=1
        else:
            invalid = True
            print("Not a valid direction!")
    elif x == 3 and y == 1:
        break

print("Victory!")