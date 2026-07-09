            int diff = arr[j] - swapPrev;

            if (diff > 0 && lowestDiff >= diff) {
                lowestDiff = diff;
                swapNext = arr[j];
                sn = j;
            }
        }

        swap(arr[sp], arr[sn]);

        // Reverse the suffix to get the smallest arrangement
        reverse(arr.begin() + sp + 1, arr.end());
    }
};
