class Solution {
    /**
     * @param {string[]} strs
     * @returns {string}
     */
    encode(strs) {
        let res = "";
        for (let str of strs) {
            res += str.length.toString() + "#" + str;
        }
        return res;
    }

    /**
     * @param {string} str
     * @returns {string[]}
     */
    decode(str) {
        let start = 0, end = 0;
        let res = [];
        while (end < str.length) {
            while (str.charAt(end) !== "#") {
                end += 1;
            }
            let length = parseInt(str.slice(start, end));
            res.push(str.slice(end + 1, end + 1 + length));
            start = end + 1 + length;
            end = end + 1 + length;
        }

        return res;
    }
}
