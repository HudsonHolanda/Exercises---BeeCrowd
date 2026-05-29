qttLines = int(input())

for _ in range(qttLines):
    wordInput = input()

    if len(wordInput) == 5:
            print("3")
            continue
    
    counter = 0
    testWord1 = False
    testWord2 = False

    for letter in wordInput:
        counter += 1
        if counter == 1:
            if letter == "o":
                testWord1 = True
                continue
            if letter == "t":
                testWord2 = True
                continue

        if counter == 2:
            if letter == "n":
                if testWord1:
                    print("1")
                    break
                testWord1 = True
            if letter == "w":
                if testWord2:
                    print("2")
                    break
                testWord2 = True
        
        if counter == 3:
            if letter == "e":
                if testWord1:
                    print("1")
                    break
                print("Error, none number identified!")
                break
            if letter == "o":
                if testWord2:
                    print("2")
                    break
                print("Error, none number identified!")
                break