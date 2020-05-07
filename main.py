import datetime #commit 1


def test1(): #commit 7
    print(summ(5,3)) #commit 7
    print(sub(10, 4)) #commit 7
    
    
def test2(): #commit 7
    print(div(10,2)) #commit 7
    print(mul(2,6)) #commit 7
    
    
def main(): #commit 2
    print('MAIN') #commit 2

    
def summ(a,b): #commit 3
    return a + b #commit 3


def div(a,b): #commit 4
    if b == 0: #commit 4
        return None #commit 4
    return a / b #commit 4


def mul(a,b): #commit 5
    return a * b #commit 5


def sub(a,b): #commit 6
    return a - b #commit 6


def echo(s): #commit 8
    print(s) #commit 8
    
    
if __name__ == '__main__': #commit 9
    main() #commit 9
    
