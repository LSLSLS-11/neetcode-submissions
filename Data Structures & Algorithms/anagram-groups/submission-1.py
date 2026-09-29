class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        k={}
        r=[]
        for i in range(len(strs)):
            if ''.join(sorted(strs[i])) not in k:
                k[''.join(sorted(strs[i]))]=len(r)
                r.append([strs[i]])
            else:
                r[k[''.join(sorted(strs[i]))]].append(strs[i])
        return r
