class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        h={}
        for i in range(len(nums)):
            h[nums[i]]=h.setdefault(nums[i],0)+1
        r=[]
        for i in range(k):
            max_key = max(h, key=h.get)
            r.append(max_key)
            del h[max_key]
        return r