class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dictS = {}
        dictT = {}

        for c in s:
            if dictS.get(c) is None:
                dictS[c] = 1
            else:
                dictS[c] += 1
        for c in t:
            if dictT.get(c) is None:
                dictT[c] = 1
            else:
                dictT[c] += 1
        if dictS == dictT:
            return True
        return False