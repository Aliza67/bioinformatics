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

