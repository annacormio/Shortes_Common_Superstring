import pandas as pd
import random
#INPUT
def getGenome(length=16):
    genome="".join(random.choice('ATCG') for i in range(length))
    return genome
def getSubstrings(seq,length=6): #returns the list of subsequences of the genome of given length
    L=[]
    for i in range(len(seq)-length+1):
        L.append(seq[i:i+length])
    return L

#OVERLAP
def overlap(s1,s2):
    over=''
    for i in range(3,len(s1)+1): #at least the first 3 characters must be equal so there is not point in checking below that
        if s2[:i]!=s1[-i:]: #if the suffix of s2 is not the same as the prefix of s1
            pass #go on looking
        else: #when subsequence coincide --> overlapping sequence
            over=s2[:i] #the i-th subsequence is assigned as an overlap
    return over


def higestOverlap(s,l): #s is the sequence which suffix is considered, l is the list of subsequences
    max=0
    p=''
    l.remove(s) #remove the element which suffix is analyse at the moment from a copy of l
    for j in l: #compare all the other substrings prefix against i subsequence
        o=overlap(s,j) #i suffix and j prefix
        if len(o)>max:
            p = j  # prefix match
    l.remove(p) #removing the 2 substrings from the original list
    merge=s[:-len(o)]+o+p[len(o):] #merge the 2 strings
    l.append(merge) #append the merged string to the list of subsequences
    return l


