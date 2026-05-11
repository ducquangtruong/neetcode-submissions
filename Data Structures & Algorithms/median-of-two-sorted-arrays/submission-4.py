class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # Idea: We take x numbers from one array and (half - x) numbers from the other
        A, B = nums1, nums2
        if len(A) > len(B):
            A, B = B, A
        m, n = len(A), len(B)
        total = m + n
        half = total // 2

        l, r = 0, m - 1
        while True:
            i = (l + r) // 2
            j = half - i - 2

            leftA = A[i] if i >= 0 else float("-inf")
            rightA = A[i+1] if i < m - 1 else float("inf")
            leftB = B[j] if j >= 0 else float("-inf")
            rightB = B[j+1] if j < n - 1 else float("inf")

            # Check if the pivots give two correct halves
            if leftA <= rightB and leftB <= rightA:
                if total % 2 == 1:
                    return min(rightA, rightB)
                else:
                    return (max(leftA, leftB) + min(rightA, rightB)) / 2
            elif leftA > rightB:
                r = i - 1
            else:
                l = i + 1
