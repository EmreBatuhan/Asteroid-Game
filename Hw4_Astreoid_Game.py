
x = int(input())
y = int(input())
g = int(input())

# DO_NOT_EDIT_ANYTHING_ABOVE_THIS_LINE
time = 0
position = (y+1)//2
meteors=[]
for i in range(1,x*y+1):
    meteors.append(i)
while True:
    if len(meteors)== 0:
        print("YOU WON!")
        for i in range(1,y*(x+g)+1):
            print(" ",end="")
            if i%y == 0:
                print()
        print(" "*(position-1)+"@"+" "*(y-position))
        print("-"*72)
        print("YOUR SCORE:",x*y)
        break
    if time % 5 == 0 and time > 0 :
        if meteors[-1]>y*(x+g-1):
            print("GAME OVER")
            for i in range(1, y * (x + g) + 1):
                if i in meteors:
                    print("*", end="")
                else:
                    print(" ", end="")
                if i % y == 0:
                    print()
            print(" " * (position - 1) + "@" + " "*(y - position))
            print("-" * 72)
            print("YOUR SCORE:",x*y-len(meteors))
            break
        else:
            new_meteors=[]
            for i in meteors:
                new_meteors.append(i+y)
            meteors = new_meteors
    for i in range(1,y*(x+g)+1):
        if i in meteors:
            print("*",end="")
        else:
            print(" ",end="")
        if i%y == 0:
            print()
    print(" " * (position - 1) + "@" + " "*(y-position))
    print("-" * 72)
    print("Choose your action!")
    command = input()
    if command.lower() == "exit":
        for i in range(1, y * (x + g) + 1):
            if i in meteors:
                print("*", end="")
            else:
                print(" ", end="")
            if i % y == 0:
                print()
        print(" " * (position - 1) + "@" + " "*(y - position))
        print("-" * 72)
        print("YOUR SCORE:", x * y - len(meteors))
        break
    if command.lower() == "left" and position > 1:
        position -= 1
    elif command.lower() == "right" and position < y:
        position += 1
    elif command.lower() == "fire":
        bullet = y*(x+g-1)+position
        while (bullet not in meteors) and bullet > 0:
            for i in range(1, y * (x + g) + 1):
                if i in meteors:
                    print("*", end="")
                elif i == bullet:
                    print("|",end="")
                else:
                    print(" ", end="")
                if i % y == 0:
                    print()
            print(" " * (position - 1) + "@" + " "*(y - position))
            print("-" * 72)
            bullet -= y
        if bullet>0:
            meteors.remove(bullet)
    time += 1

# DO_NOT_EDIT_ANYTHING_BELOW_THIS_LINE