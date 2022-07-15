#User function Template for python3
from collections import defaultdict
class Solution:
    def Anagrams(self, words, n):
        '''
        words: list of word
        n:      no of words
        return : list of group of anagram {list will be sorted in driver code (not word in grp)}
        '''
        
        #code here
        d=defaultdict(list)
        for ele in words:
            string = "".join(sorted(ele))
            if(string not in d):
                d[string]=[ele]
            else:
                d[string].append(ele)
            
        return sorted(d.values())