class Solution {
    /**
     * @param {number[]} nums
     * @return {number}
     */
    maxSubArray(nums) {
        let res = nums[0], curSum = 0;
        for (let n of nums) {
            curSum = Math.max(curSum, 0);
            curSum += n;
            res = Math.max(curSum, res);
        }
        return res;
    }
}
