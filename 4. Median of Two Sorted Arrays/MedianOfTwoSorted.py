class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        if len(nums1) > len(nums2):
            return self.findMedianSortedArrays(nums2, nums1)
        
        i, j = 0, 0          
        merged = []
        len1, len2 = len(nums1), len(nums2)
        while i < len1 and j < len2:
            if nums1[i] < nums2[j]:
                merged.append(nums1[i])
                i += 1
            else:
                merged.append(nums2[j])
                j += 1
        merged.extend(nums1[i:])
        merged.extend(nums2[j:])

        total = len1 + len2
        if total % 2 == 1:
            return float(merged[total // 2])
        else:
            mid1 = merged[total // 2 - 1]
            mid2 = merged[total // 2]
            return (mid1 + mid2) / 2


nums1 = [1,3]
nums2 = [2]
solution = Solution()
res = solution.findMedianSortedArrays(nums1, nums2)
print(res) 