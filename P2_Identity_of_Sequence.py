se1=input("Enter the First sequence::")
se2=input("Enter the Second sequence::")
seq1=list(se1)
seq2=list(se2)
def find_identity(a,b):
    gap(a,b)
    print(a)
    print(b)
    score=0
    length=len(a)
    total_elements=len(a)*len(b)
    for i in range(0,length):
        for j in range(0,length):
            if(a[i] == b[j]):
                score=score+1
    identity=(score/total_elements)*100
    print("Matching Score::",score)
    print("Identity of the Sequences::",identity)

def gap(a,b):
    if(len(a)==len(b)):
        print()
    else:
        k=int(input("Enter the position to insert gap::"))
        if(len(a)<len(b)):
            a.insert(k,'-')
        else:
            b.insert(k,'-')
    return(a,b)

find_identity(seq1,seq2)

Output:
= RESTART: C:\Users\bhavana vanjani\Documents\Msc CS Part1  Pracs\Bioinformatics - paper 3\P2_Identity.py
Enter the First sequence::ACTG
Enter the Second sequence::AGCT

['A', 'C', 'T', 'G']
['A', 'G', 'C', 'T']
Matching Score:: 4
Identity of the Sequences:: 25.0