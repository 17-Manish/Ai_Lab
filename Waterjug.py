import math
a=int(input("enter jug A capacity: "))
b=int(input("enter jug B capacity: "))
ai=int(input("initial water in jug A : "))
bi=int(input("initial water in jug B : "))
af=int(input("final state of jug A : "))
bf=int(input("final state of jug B : "))

if a<=0 or b<=0:
    print("jug capacities must be positive.")
    exit(1)
if ai<0 or bi<0 or af<0 or bf<0:
    print("negative values are not allowed.")
    exit(1)
#define the water
def wjug(a,b,ai,bi,af,bf):
        print("list of operation you can Do:\n")
        print("1. fill jug A completely")
        print("2. fill jug B completely")
        print("3. empty jug A completely")
        print("4. empty jug B completely")
        print("5. pour from jug A till jug B is full or A becomes empty")
        print("6. pour from jug B till jug A is full or B becomes empty")
        print("7. pour all from jug B to jug A")
        print("8. pour all from jug A to jug B")

        while (ai !=af or bi !=bf):
            op = int(input("enter the operation(1-8): "))

            if op ==1:
                ai=a
            elif op ==2:
                bi =b
            elif op ==3:
              ai = 0
            elif op == 4:
                bi = 0
            elif op == 5:
                pour_amount = min(ai,b - bi)
                ai -= pour_amount
                bi += pour_amount
            elif op == 6:
                pour_amount = min(bi,a - ai)
                bi -= pour_amount
                ai += pour_amount
            elif op == 7:
                pour_amount = min(ai,b - bi)
                ai += pour_amount
                bi -= pour_amount
            elif op == 8:
                pour_amount = min(bi,a - ai)
                bi += pour_amount
                ai -= pour_amount
            else:
                print("invalid operation. please choose a number between 1-8")
                continue
            print(f"jug A: {ai}, jug B: {bi}")
            if ai == af and bi == bf:
                print("final state reached: jug A=",ai,",jug B =",bi)
                return

            print("final state reached : jug A = ", ai,",jug B =",bi)
gcb = math.gcd(a,b)
if (af <= a and bf <= b) and (af % gcb == bf % gcb ==0):
    wjug(a,b,ai,bi,af,bf)
else:
    print("the final state is not achievable with the given capacities.")
    exit(1)
                



                
