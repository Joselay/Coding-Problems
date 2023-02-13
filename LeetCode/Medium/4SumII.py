class Solution:
    def fourSumCount(self, A: List[int], B: List[int], C: List[int], D: List[int]) -> int:
        count_ab = collections.Counter(a + b for a in A for b in B)
        return sum(count_ab[-c - d] for c in C for d in D)
