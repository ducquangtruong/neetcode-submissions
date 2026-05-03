class Solution {
    /**
     * @param {number[]} nums
     * @return {number}
     */
    jump(nums) {
        if (nums.length == 1) return 0;
        let steps = 0, furthest = 0;
        for (let i = 0; i < nums.length; i++) {
            if (i > furthest) return -1;
            if (nums[i] + i > furthest) {
                furthest = nums[i] + i;
                steps += 1;
            }
            if (furthest >= nums.length - 1) break;
        }
        return steps;
    }
}
