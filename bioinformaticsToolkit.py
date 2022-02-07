def CountingDNANucleotides(x) :
    a=0
    g=0
    t=0
    c=0
    for acide in x :
        if acide=='A':
            a=a+1
        if acide=='G':
            g=g+1
        if acide=='C':
            c=c+1
        if acide=='T':
            t=t+1
    print('A:', a, ' C:', c, ' G:', g, ' T:', t)

def transcribingDnaToRna(string):
    print(string.replace("T", "U"))

def complementingDna(dna):
    str =''
    for x in dna :
        if x=='T':
            str = str+'A'
        elif x == 'A' :
            str = str + 'T'
        elif x == 'C':
            str = str + 'G'
        elif x == 'G':
            str = str + 'C'
    result = str[::-1]
    print(result)

def wascalliWabbits(months, rep):
    pop=[1]
    
    pop.append(1)
    x=2
    while (x<(months)):
        pop.append(pop[x-1]+pop[x-2]*rep)
        x=x+1
    result=0
   
    print(pop[months-1])
