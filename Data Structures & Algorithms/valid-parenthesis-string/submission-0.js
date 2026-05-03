class Solution {
    /**
     * @param {string} s
     * @return {boolean}
     */
    checkValidString(s) {
        let leftStk = [], starStk = [];
        for (let i = 0; i < s.length; i++) {
            let c = s[i];
            switch(c) {
                case "(":
                    leftStk.push(i);
                    break;
                case "*":
                    starStk.push(i);
                    break;
                default:
                    if (leftStk.length != 0) {
                        leftStk.pop();
                        continue;
                    }
                    if (starStk.length != 0) {
                        starStk.pop();
                        continue;
                    }
                    return false;
            }
        }
        while (leftStk.length != 0) {
            if (starStk.length == 0 || leftStk.pop() > starStk.pop()) return false;
        }
        return true;
    }
}
