class Solution {
    /**
     * @param {number[]} gas
     * @param {number[]} cost
     * @return {number}
     */
    canCompleteCircuit(gas, cost) {
        if (
            gas.reduce((sum, val) => sum + val, 0) < 
            cost.reduce((sum, val) => sum + val, 0)
        ) return -1;
        let minIndex = 0, tank = 0;
        for (let i = 0; i < gas.length; i++) {
            tank += gas[i] - cost[i];
            if (tank < 0) {
                tank = 0;
                minIndex = i + 1;
            }
        }
        return minIndex;
    }
}
