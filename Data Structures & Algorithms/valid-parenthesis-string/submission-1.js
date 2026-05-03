class Solution {
    /**
     * @param {string} s
     * @return {boolean}
     */
    checkValidString(s) {
        let lefts = [], stars = [];
        for (let i = 0; i < s.length; i++) {
            let c = s[i];
            switch(c) {
                case "(":
                    lefts.push(i);
                    break;
                case "*":
                    stars.push(i);
                    break;
                default:
                    if (lefts.length === 0 && stars.length === 0) return false;
                    if (lefts.length !== 0) {
                        lefts.pop();
                    } else {
                        stars.pop();
                    }
            }
        }
        while (lefts.length !== 0 && stars.length !== 0) {
            if (lefts.pop() > stars.pop()) return false;
        }
        return lefts.length === 0;
    }
}
