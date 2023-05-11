import random
import itertools


# INPUT
def getGenome(length=1000):
    genome = "".join(random.choice('ATCG') for i in range(length))
    return genome

def getSubstrings(seq, length=100):  # returns the list of subsequences of the genome of given length
    L = []
    for i in range(len(seq) - length + 1):
        L.append(seq[i:i + length])
    return L


# OVERLAP
def overlap(s1, s2):
    over = ''
    for i in range(3,min(len(s1),len(s2)) + 1):  # at least the first 3 characters must be equal so there is not point in checking below that
        if s1[-i:] != s2[:i]:  # if the suffix of s2 is not the same as the prefix of s1
            pass  # go on looking
        else:  # when subsequence coincide --> overlapping sequence
            over = s2[:i]  # the i-th subsequence is assigned as an overlap
    return over


#CHOOSE PAIR among equal overlap length once
def maxPair(l):
    if len(l) == 1:  # only one pair with max overlap length
        p = l[0]  # extract the only pair from the list
    else:  # if there are more pairs with that overlap max length
        p = random.choice(l)  # choose one randomly within the list
    return p

#MERGE
def merge(l): #merge all elements in a list one after the other
    p=[]
    merge=''
    for merge_per in itertools.permutations(l,len(l)): #create all possible permutations of remianing non overlapping sequences
        p.append(list(merge_per))

    # among all possible permutations of the non overlapping seuqences stored in p list i pick one randomly and merge it
    for i in random.choice(p):
        merge += i  # merge all sequences of the permutation together in order left-right
    return merge  # return merged sequence



#COMPUTE SHORTES COMMON SUPERSTRING
def SCS(l):  #l is the list of subsequences
    if len(l) == 1: #only one seq in the list
        return l[0]
    else: #more than one seq in the list
        l_max = 0  # var for the max length of the computed overlap=shortest sequence
        max_pairs = []
        for pair in itertools.permutations(l, 2): #iter over each pair
            o = overlap(pair[0], pair[1])  # compute overlap of 1st seq suffix and 2nd seq prefix of the pair --> function defined above
            if len(o) > l_max:  # if the length of the computed pair overlap is greater than the stored max length up to that point
                l_max = len(o)  # the max length is updated
                max_pairs.clear() #removes all elements from  a list when we find a new pair which has greater length than the one stored before
                max_pairs.append(pair) #append the max found

            elif len(o) == l_max:  # if 2 pairs have the same overlap length
                max_pairs.append(pair) #append the other pair with same max overlap length to the list

        p=maxPair(max_pairs) #choose pair among the built list --> function defined above
        suf = p[0]  # seq with suffix overlap
        pre = p[1]  # seq with prefix ovverlap
        o_max = overlap(suf, pre)  # overlap sequence

        if o_max: #if we have an overlap in the seq
            l.remove(suf)
            l.remove(pre)  # removing the 2 substrings from the original list
            mer = suf[:-l_max] + o_max + pre[l_max:]  # merge the 2 strings
            l.append(mer)  # append the merged string to the list of subsequences
            return SCS(l) #recursive call

        else: #if no pair combination overlaps
            return merge(l) #function defined above

#MAIN
if __name__ == "__main__":
    DNA = getGenome(15)
    subseq = getSubstrings(DNA, 6)
    #subseq = ['ATCGGA', 'TACCCA', 'AGCTAC', 'CGGATT', 'TTGCTA']
    print(subseq)
    scs=SCS(subseq)
    print(scs)

