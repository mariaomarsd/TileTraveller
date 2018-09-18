x = 1
y = 1

while 1 <= x <= 3 and 1 <= y <=3:
    direction = str(input(("Direction:")))
    direction.lower()

    if 1 <= x <= 3 and y == 1:
        print("You can travel: (N)orth")
        if direction == 'n':
            y+=1
        else:
            print("Not a valid direction!")
    elif x == 1 and y == 2:
        print("You can travel: (N)orth or (E)ast or (S)outh.")
        if direction == 'n':
            y+=1
        elif direction == 's':
            y-=1
        elif direction == 'e':
            x+=1
        else:
            print("Not a valid direction")
    elif x == 1 and y == 3:
        print("You can travel: (E)ast or (S)outh.")
        if direction == 's':
            y-=1
        elif direction == 'e':
            x+=1
        else:
            print("Not a valid direction!")
    elif 2 <= x <= 3 and 2 <= y <= 3:
        print("You can travel: (S)outh or (W)est.")
        if direction == 's':
            y-=1
        elif direction == 'w':
            x-=1
        else:
            print("Not a valid direction!")
    elif x == 2 and y == 3:
        print("You can travel: (E)ast or (W)est.")
        if direction == 'e':
            x+=1
        elif direction == 'w':
            x-=1
        else:
            print("Not a valid direction!")
    elif x == 3 and y == 2:
        print("You can travel: (N)ourth or (S)outh.")
        if direction == 'n':
            y+=1
        elif direction == 's':
            y-=1
        else:
            print("Not a valid direction!")
    else:
        ("Not a valid direction!!!!")

        
print("Victory!")