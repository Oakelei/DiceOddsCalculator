def oddscalculator(DieType=6, NumberOfDice=1,droplowest=0,drophighest=0):
    result=dotheoddsy(DieType, NumberOfDice,droplowest,drophighest)
    print(result)
    avg = 0
    print(sum(result))
    for i in range(len(result)):
        avg = avg+result[i]*(i+1)
    print(avg)


def dotheoddsy(Type,NumberOfDice,droplowest,drophighest):
    a=[]
    b=[]
    for i in (range(Type*(NumberOfDice-droplowest-drophighest))):
        a.append(0)
    dotheodds(Type, NumberOfDice,a,b,droplowest,drophighest)
    for i in range(len(a)):
        a[i] = a[i]/pow(Type,NumberOfDice)

    return(a)


def dotheodds(dicetype,numberofdice,a,b,droplowest,drophighest):
    if numberofdice == 0:
        total=sum(sorted(b)[slice(0+droplowest,len(b)-drophighest)])
        a[total-1]=a[total-1]+1
        return()
    for i in range(1,dicetype+1):
        c=b[:]
        c.append(i)
        dotheodds(dicetype,numberofdice-1,a,c[:],droplowest,drophighest)

def matrixcreatory(width, debth):
    startarray = []
    for i in range(1, width+1):
        startarray.append(i)
    alen = len(startarray)
    return matrixcreator(debth, startarray[:], alen)

def matrixcreator(n, a, len):
    if n == 0:
        return a[:]
    b = a[:]
    for i in range(len):
        b[i] = matrixcreator(n - 1, a[:], len)
    return b[:]


if __name__ == '__main__':
    DieType: int = 6
    NumberOfDice: int = 3
    droplowest: int = 1
    drophighest: int = 0
    oddscalculator(DieType, NumberOfDice,droplowest,drophighest)
