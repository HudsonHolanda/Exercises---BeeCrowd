n = int(input())
position = input()

for _ in range(n):
    movement = int(input())

    if movement == 1:
        if position == "A":
            position = "B"
        elif position == "B":
            position = "A"
    
    elif movement == 2:
        if position == "B":
            position = "C"
        elif position == "C":
            position = "B"

    elif movement == 3:
        if position == "A":
            position = "C"
        elif position == "C":
            position = "A"

    else:
        break

print(position)