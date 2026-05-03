class Solution {
    /**
     * @param {string} s
     * @return {number}
     */
    lengthOfLongestSubstring(s) {
        let chars = new Set();
        let res = 0;
        let start = 0, end = 0;
        while (end < s.length) {
            let ch = s.charAt(end);
            if (chars.has(ch)) {
                res = Math.max(res, end - start);
                while (start < end && chars.has(ch)) {
                    chars.delete(s.charAt(start));
                    start += 1;
                }
            }
            chars.add(ch);
            end += 1;
        }
        return Math.max(res, end - start);
    }
}
