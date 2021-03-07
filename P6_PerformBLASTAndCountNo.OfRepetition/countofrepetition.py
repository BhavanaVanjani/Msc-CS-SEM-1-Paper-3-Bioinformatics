# program to find count of repetition of a sequence for a given nucleotide.
file=open("genes.txt","r")  
r=file.read()  
size=len(r)  
score_A=0  
score_C=0  
score_T=0  
score_G=0  
for i in range(size):  
     if(r[i]=='A'):  
          score_A+=1  
     elif (r[i]=='C'): 
          score_C+=1  
     elif (r[i]=='T'): 
          score_T+=1  
     elif (r[i]=='G'): 
          score_G+=1  
print("score of A is ",score_A)  
print("score of C is ",score_C)  
print("score of T is ",score_T)  
print("score of G is ",score_G)

""" Genes.txt should ne in the same folder/location as python file for count
of repetition of sequence. """

Output:
===== RESTART: C:\Users\bhavana vanjani\Downloads\P6_CountNoOfRepetition.py ====
score of A is  206
score of C is  236
score of T is  217
score of G is  279
