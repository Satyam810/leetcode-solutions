class Solution {
public:
    void nextPermutation(vector<int>& arr) {
        int n = arr.size();

        int swapPrev, sp;
        int swapNext, sn;

        bool descendingOrderFlag = true;

        int lowestDiff = INT_MAX;

        // Find the first breakpoint from the right
        for (int i = n - 2; i >= 0; i--) {
            if (arr[i] < arr[i + 1]) {
                swapPrev = arr[i];
