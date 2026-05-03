class Solution {
    /**
     * @param {number[]} hand
     * @param {number} groupSize
     * @return {boolean}
     */
    isNStraightHand(hand, groupSize) {
        if (hand.length % groupSize !== 0) return false;
        // Count the cards
        let freq = new Map();
        for (let card of hand) {
            if (!freq.has(card)) {
                freq.set(card, 0);
            }
            freq.set(card, freq.get(card) + 1);
        }
        for (let card of hand) {
            let start = card;
            while (freq.has(start - 1) && freq.get(start - 1) > 0) start -= 1;
            while (start <= card) {
                while (freq.get(start) > 0) {
                    for (let i = start; i < start + groupSize; i++) {
                        if (!freq.has(i) || freq.get(i) == 0) {
                            return false;
                        }
                        freq.set(i, freq.get(i) - 1);
                    }
                }
                start += 1;
            }
        }
        return true;
    }
}
