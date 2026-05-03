class Solution {
    /**
     * @param {number[]} height
     * @return {number}
     */
    trap(height) {
        let res = 0;
        let start = 0, end = height.length - 1;
        let leftMax = height[0], rightMax = height[height.length - 1];

        while (start < end) {
            if (leftMax < rightMax) {
                start += 1;
                leftMax = Math.max(leftMax, height[start]);
                res += leftMax - height[start];
            } else {
                end -= 1;
                rightMax = Math.max(rightMax, height[end]);
                res += rightMax - height[end];
            }
        }

        return res;
    }
}
