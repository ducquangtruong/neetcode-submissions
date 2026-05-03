class Solution {
    /**
     * @param {number[]} nums
     * @return {number[]}
     */
    productExceptSelf(nums) {
        // Idea: Prefix product from both sides
        let n = nums.length;
        let res = new Array(n).fill(1);
        let left = 1, right = 1;
        for (let i = 0; i < n; i++) {
            res[i] *= left;
            left *= nums[i];
            res[n - i - 1] *= right;
            right *= nums[n - i - 1];
        }

        return res;
    }
}
