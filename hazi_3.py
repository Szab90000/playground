def CanYouDraw(A, B, C):
    if(
    A + B > C and 
    B + C > A and
    C + A > B):
        print(f"A {A}, {B} és {C} oldalú háromszög szerkeszthető")
    else:
       print(f"A {A}, {B} és {C} oldalú háromszög NEM szerkeszthető")     


print("Adja meg a háromszög 3 oldalát cm-ben:")

side1 = int(input("a oldal (cm): "))
side2 = int(input("b oldal (cm): "))
side3 = int(input("c oldal (cm): "))

CanYouDraw(side1, side2, side3)