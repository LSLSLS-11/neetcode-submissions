class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_string=''
        for s in strs:
            encoded_string+=str(len(s))+'*'+s+'*'
        return encoded_string

    def decode(self, s: str) -> List[str]:
        decoded_strs=[]
        while len(s)>0:
            word=''
            l=0
            i=0
            while s[i].isdigit() :
                i+=1
            l=int(s[:i])
            word=s[i+1:i+l+1]
            s=s[i+l+2:]
            decoded_strs.append(word)
        return decoded_strs



