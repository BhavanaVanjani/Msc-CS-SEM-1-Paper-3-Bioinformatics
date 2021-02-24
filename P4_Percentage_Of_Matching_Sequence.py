#Write a program to calculate Percentage of Sequence.
seq1 = list(input("Enter the First sequence::"))
seq2 = list(input("Enter the second sequence::"))

#for identity
score=[]
def identity(a,b):
    value=0
    length=len(a)
    for i in range(0,length):
        if(a[i]==b[i]):
            score.append('1')
            value=value+1
        else:
            score.append('0')
    return value


# for similarity
how_many=int(input("How many elements for similarity condition?"))
similarities=[]
for i in range(0,how_many):
    a=input("Enter an element")
    c=int(input("How many elements is it similar to"))
    similarities.append([])
    similarities[i].append(a)

    for j in range(0,c):
        b=input("What is it similar to?")
        similarities[i].append(b)
        
def compare(o,t,s):
    print(o)
    print(t)
    print(s)
    #checking if similar
    score=0
    for i in range(len(o)):
        for j in range(len(s)):
            if o[i] in s[j] and t[i] in s[j] and o[i] != t[i]:
                score += 1
    #calculating similarity
    similarity=score
    return similarity


identi=(identity((seq1),(seq2)))
simi=(compare((seq1),(seq2),similarities))
print("similarity of the Sequences::",simi)
print("identity of the Sequences::",identi)
total=identi + simi

#counting
gap_in_sequence1=seq1.count('-')
gap_in_sequence2=seq2.count('-')
total_gap=gap_in_sequence1 + gap_in_sequence2
print("Gap in the sequence",total_gap)

percentage_of_sequence=(total/(len(seq1)-total_gap))*100
print("Percentage of sequence are::",percentage_of_sequence,"%")

Output:
= RESTART: C:\Users\bhavana vanjani\Documents\Msc CS Part1  Pracs\Bioinformatics - paper 3\P4_Percentage_of_Sequence.py
Enter the First sequence::ACTG
Enter the second sequence::AGCT
How many elements for similarity condition?1
Enter an elementC
How many elements is it similar to1
What is it similar to?G
['A', 'C', 'T', 'G']
['A', 'G', 'C', 'T']
[['C', 'G']]
similarity of the Sequences:: 1
identity of the Sequences:: 1
Gap in the sequence 0
Percentage of sequence are:: 50.0 %
