class Solution {
    /**
     * @param {number[]} nums
     * @return {boolean}
     */
    canJump(nums) {
        let furthest = 0;
        for (let i = 0; i < nums.length; i++) {
            if (i > furthest) return false;
            furthest = Math.max(furthest, nums[i] + i);
            if (furthest >= nums.length - 1) return true;
        }
        return false;
    }
}
