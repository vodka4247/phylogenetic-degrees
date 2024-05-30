
# Online Python - IDE, Editor, Compiler, Interpreter
import math
def binom(a,b):
    c=math.factorial(b)
    d=1
    while b>0:
        d=d*(a-b+1)
        b=b-1
    return(d//c)
def com(a,b):
    d=1
    while b>0:
        d=d*(a-b+1)
        b=b-1
    return(d)
def change1(C1):
    L1=C1.copy()
    L1.insert(1,L1[0]-1)
    L1.pop(0)
    L1.insert(2,L1[1]+1)
    L1.pop(1)
    return(L1)
def change2(C2):
    L2=C2.copy()
    L2.pop(0)
    L2.insert(1,L2[0]+1)
    L2.pop(0)
    return(L2)
def change3(C3):
    L3=C3.copy()
    L3.insert(2,L3[0]+L3[1]+1)
    L3.pop(0)
    L3.pop(0)
    return(L3)
def change4(C4):
    L4=C4.copy()
    L4.pop(0)
    L4.pop(0)
    if L4==[]:
        return ([])
    L4.insert(1,L4[0]+1)
    L4.pop(0)
    return(L4)
def change5(C5):
    L5=C5.copy()
    L5.pop(0)
    L5.insert(1,L5[0]+2)
    L5.pop(0)
    return(L5)
    

def volume(L):
    if L==[]:
        return 1
    if len(L)==1:
        return(math.factorial(L[0])-pow(2,L[0]-1))
    if L[0]==1:
        return 0
    return(-volume(change1(L))+volume(change2(L))*volume([L[0]])*binom(sum(L)+len(L)-1,L[0])-volume(change3(L))+volume(change4(L))*volume([L[0]+1])*binom(sum(L)+len(L)-1,L[0]+1)*com(sum(L)+len(L)-L[0]-2,L[1])+volume(change5(L))*com(sum(L)+len(L)-1,L[0]-1))
   

def latticevolume(M):
    print(volume(M))


latticevolume([2,1,2])

