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
    for i in range(3,len(s1) + 1):  # at least the first 3 characters must be equal so there is not point in checking below that
        if s1[-i:] != s2[:i]:  # if the suffix of s2 is not the same as the prefix of s1
            pass  # go on looking
        else:  # when subsequence coincide --> overlapping sequence
            over = s2[:i]  # the i-th subsequence is assigned as an overlap
    return over





def SCS(l):  #l is the list of subsequences
    if len(l) == 1:
        return l[0]
    else:
        l_max = 0  # var for the max length of the computed overlap
        o_max = ''  # variable for the max overlap sequence
        max_pairs = []
        for pair in itertools.permutations(l, 2): #iter over each pair
            o = overlap(pair[0], pair[1])  # compute overlap of 1st seq suffix and 2nd seq prefix of the pair
            if len(o) > l_max:  # if the length of the computed pair overlap is greater than the stored max length up to that point
                l_max = len(o)  # the max length is updated
                max_pairs.clear() #removes all elements from  a list when we find a new pair which has greater length than the one stored before
                max_pairs.append(pair) #append the max found

            elif len(o) == l_max:  # if 2 pairs have the same overlap length
                max_pairs.append(pair) #append the other pair with same max overlap length to the listù

        #print(f'max pair list   {max_pairs}')
        if len(max_pairs) == 1: #only one pair with max overlap length
            p = max_pairs[0] #extract the only pair from the list
            suf = p[0]
            pre = p[1]
            o_max = overlap(suf,pre)  # overlap sequence

        else: #if there are more pairs with that overlpa max length
            p=random.choice(max_pairs) #choose one randomly within the list
            #print(f'random choice is {p}')
            suf= p[0]
            pre=p[1]
            o_max = overlap(suf,pre)

        if o_max: #if we have an overlap in the seq
            l.remove(suf)
            l.remove(pre)  # removing the 2 substrings from the original list
            merge = suf[:-l_max] + o_max + pre[l_max:]  # merge the 2 strings
            l.append(merge)  # append the merged string to the list of subsequences
            #print(l)
            #print(l[0])
            return SCS(l) #recursive call

        else: #if no pair combination overlaps
            merge = ''
            for i in l:
                merge += i   #merge all remaining sequences together
            return merge

# MAIN
DNA = getGenome(15)
#gen='TAGTAGCGATCA'
subseq = getSubstrings(DNA, 6)
#subseq= ['AGTACG','GTACGT','CCCGAT', 'GACTGG', 'AACGCC','GACCTT']
print(DNA)
print(subseq)
print(SCS(subseq))