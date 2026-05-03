class Solution {
    /**
     * @param {number[]} nums
     * @return {number}
     */
    longestConsecutive(nums) {
        let numSet = new Set(nums);
        let res = 0;
        for (let num of nums) {
            // Check if num is start of chain
            if (numSet.has(num - 1)) continue;
            let cur = 0;
            while (numSet.has(num)) {
                cur += 1;
                num += 1;
            }
            res = Math.max(res, cur);
        }
        return res;
    }
}
