def logestSubseq(s1,s2, ls1, ls2):
    if ls1==0 or ls2==0:
        return ''
    elif s1[ls1-1] ==s2[ls2-1]:
        return (s1[ls1-1] + logestSubseq(s1, s2, ls1-1, ls2-1))
    else:
        return max(logestSubseq(s1, s2, ls1, ls2-1), logestSubseq(s1, s2, ls1-1, ls2))
    
s1 = "aggtab"
s2 = "gxtxayb"
s3 = logestSubseq(s1,s2, len(s1), len(s2))
print(s3[::-1])