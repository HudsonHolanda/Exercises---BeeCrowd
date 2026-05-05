A, B, C = map(int, input().split())
Humor = ":("
if(A > B and B <= C):
    Humor = ":)"
elif(A < B and B >= C):
    Humor = ":("
elif(A < B and B < C):
    if((B - A) > (C - B)):
        Humor = ":("
    else:
        Humor = ":)"
elif(A > B and B > C):
    if((A - B) > (B - C)):
        Humor = ":)"
    else:
        Humor = ":("
elif(A == B and B < C):
    Humor = ":)"
elif(A == B and B > C):
    Humor = ":("

print(Humor)