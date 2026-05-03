class Solution {
    /**
     * @param {number[]} height
     * @return {number}
     */
    trap(height) {
        let res = 0;
        let start = 0, end = height.length - 1;
        let leftMax = height[0], rightMax = height[height.length - 1];

        while (start <= end) {
            if (leftMax < rightMax) {
                leftMax = Math.max(leftMax, height[start]);
                res += leftMax - height[start];
                start += 1;
            } else {
                rightMax = Math.max(rightMax, height[end]);
                res += rightMax - height[end];
                end -= 1;
            }
        }

        return res;
    }
}
