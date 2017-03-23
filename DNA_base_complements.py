Python 2.7.11 (v2.7.11:6d1b6a68f775, Dec  5 2015, 20:32:19) [MSC v.1500 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> basecomplement = {'A': 'T', 'C': 'G', 'T': 'A', 'G': 'C'}
>>> basecomplement['A']
'T'
>>> basecomplement['C']
'G'
>>> for base in basecomplement.keys(): 
   print "The complement of", base, "is", basecomplement[base]

   
The complement of A is T
The complement of C is G
The complement of T is A
The complement of G is C
>>> letters = list('CCGGAAGAGCTTACTTAG')
>>> [basecomplement[base]for base in letters]
['G', 'G', 'C', 'C', 'T', 'T', 'C', 'T', 'C', 'G', 'A', 'A', 'T', 'G', 'A', 'A', 'T', 'C']
>>> def complement(s): 
    """Return the complementary sequence string.""" 
    basecomplement = {'A': 'T', 'C': 'G', 'G': 'C', 'T': 'A'} 
    letters = list(s) 
    letters = [basecomplement[base] for base in letters] 
    return ''.join(letters)

>>> complement('CCGGAAGAGCTTACTTAGATTGGGTCCCTGTCGTAAAATAT')
'GGCCTTCTCGAATGAATCTAACCCAGGGACAGCATTTTATA'
>>> 
