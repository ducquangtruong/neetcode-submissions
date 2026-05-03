class Solution {
    /**
     * @param {string[]} strs
     * @return {string[][]}
     */
    groupAnagrams(strs) {
        let lookup = {};
        for (let str of strs) {
            let key = str.split("").sort().join("");
            if (!(key in lookup)) {
                lookup[key] = [];
            }
            lookup[key].push(str);
        }

        let res = [];
        for (let key in lookup) {
            res.push(lookup[key]);
        }
        return res;
    }
}
