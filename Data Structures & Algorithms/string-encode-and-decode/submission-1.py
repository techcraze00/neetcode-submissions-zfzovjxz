class Solution:

    def encode(self, strs: List[str]) -> str:
        res=""
        for s in strs: # -->["neet", "code"]
            res += str(len(s)) + ":" + s
        return res # --> "4:neet4:code"

    def decode(self, s: str) -> List[str]:

        res=[]
        idx=0

        while idx<len(s):
            j=idx # --> i=j= "4" [from the str 4:neet4:code]

            while s[j] != ":":
                j+=1 # --> i= "4", j= ":"
            
            length_of_str = int(s[idx:j]) # slicing --> "4" --> int("4")

            res.append(s[j+1 : j+1+length_of_str]) # --> j+1 => start after ":" delimiter upto the next number in the string

            idx = j+1+length_of_str

        return res