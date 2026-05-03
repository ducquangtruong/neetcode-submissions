class Solution {
    /**
     * @param {string} S
     * @return {number[]}
     */
    partitionLabels(S) {
        let START = 97;
        let freq = new Array(26).fill(-1);
        for (let i = 0; i < S.length; i++) {
            freq[S.charCodeAt(i) - START] = i;
        }

        let startIdx = 0, lastIdx = 0;
        let output = [];
        for (let i = 0; i < S.length; i++) {
            lastIdx = Math.max(lastIdx, freq[S.charCodeAt(i) - START]);
            if (i == lastIdx) {
                output.push(lastIdx - startIdx + 1);
                startIdx = i + 1;
                lastIdx = i + 1;
            }
        }
        return output;
    }
}
