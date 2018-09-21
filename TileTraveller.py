x = 1
y = 1
invalid = False
#directions = [n, s, a, w]
directions = [0,0,0,0]

def move(direction):
    global invalid
    if direction == 'n':
        invalid = False
        return y+1
    elif direction == 's':
        invalid = False
        return y-1
    elif direction == 'e':
        invalid = False
        return x+1
    elif direction == 'w':
        invalid = False
        return x-1

def valid_direction(x, y):
    global directions
    global invalid
    if invalid == False:
        if 1 <= x <= 2 and y == 1: 
            print("You can travel: (N)orth ")
            directions = [1, 0, 0, 0]
        elif x == 1 and y == 2:
            print("You can travel: (N)orth or (E)ast or (S)outh.")
            directions = [1, 1, 1, 0]
        elif x == 1 and y == 3:
            print("You can travel: (E)ast or (S)outh.")
            directions = [0, 1, 1, 0]
        elif x == y and x != 1:
            print("You can travel: (S)outh or (W)est.")
            directions = [0, 1, 0, 1]
        elif x == 2 and y == 3:
            print("You can travel: (E)ast or (W)est.")
            directions = [0, 0, 1, 1]
        elif x == 3 and y == 2:
            print("You can travel: (N)orth or (S)outh.")
            directions = [1, 1, 0, 0]
        elif x == 3 and y == 1:
            print("victory!")
            return "victory"
    else:
        invalid = True
        print("Not a Valid direction!")

def valid_possition(x, y):
    if 1 <= x <= 3 and 1 <= y <= 3:
        return True
    


while valid_possition(x,y):
    position = valid_direction(x, y)
    if(position == "victory"):
        break
    direction = str(input(("Direction: ")))
    direction = direction.lower()
    if direction == 'n' and directions[0] == 1:
        y = move(direction)
    elif direction == 's' and directions[1] == 1:
        y = move(direction)
    elif direction == 'e' and directions[2] == 1:
        x = move(direction)
    elif direction == 'w' and directions[3] == 1:
        x = move(direction)
    else:
        invalid = True



# x = 1
# y = 1
# invalid = False

# while 1 <= x <= 3 and 1 <= y <=3:

#     if 1 <= x <= 2 and y == 1:
#         if invalid == False:
#             print("You can travel: (N)orth.")
#         direction = str(input(("Direction: ")))
#         direction = direction.lower()
#         if direction == 'n':
#             y+=1
#             invalid = False
#         else:
#             invalid = True
#             print("Not a valid direction!")
#     elif x == 1 and y == 2:
#         if invalid == False:
#             print("You can travel: (N)orth or (E)ast or (S)outh.")
#         direction = str(input(("Direction: ")))
#         direction = direction.lower()
#         if direction == 'n':
#             invalid = False
#             y+=1
#         elif direction == 's':
#             invalid = False
#             y-=1
#         elif direction == 'e':
#             invalid = False
#             x+=1
#         else:
#             invalid = True
#             print("Not a valid direction!")
#     elif x == 1 and y == 3:
#         if invalid == False:
#             print("You can travel: (E)ast or (S)outh.")
#         direction = str(input(("Direction: ")))
#         direction = direction.lower()
#         if direction == 's':
#             invalid = False
#             y-=1
#         elif direction == 'e':
#             invalid = False
#             x+=1
#         else:
#             invalid = True
#             print("Not a valid direction!")
#     elif x == y and x != 1:
#         if invalid == False:
#             print("You can travel: (S)outh or (W)est.")
#         direction = str(input(("Direction: ")))
#         direction = direction.lower()
#         if direction == 's':
#             invalid = False
#             y-=1
#         elif direction == 'w':
#             invalid = False
#             x-=1
#         else:
#             invalid = True
#             print("Not a valid direction!")
#     elif x == 2 and y == 3:
#         if invalid == False:
#             print("You can travel: (E)ast or (W)est.")
#         direction = str(input(("Direction: ")))
#         direction = direction.lower()
#         if direction == 'e':
#             invalid = False
#             x+=1
#         elif direction == 'w':
#             invalid = False
#             x-=1
#         else:
#             invalid = True
#             print("Not a valid direction!")
#     elif x == 3 and y == 2:
#         if invalid == False:
#             print("You can travel: (N)orth or (S)outh.")
#         direction = str(input(("Direction: ")))
#         direction = direction.lower()
#         if direction == 'n':
#             invalid = False
#             y+=1
#         elif direction == 's':
#             invalid = False
#             y-=1
#         else:
#             invalid = True
#             print("Not a valid direction!")
#     elif x == 3 and y == 1:
#         break

# print("Victory!")