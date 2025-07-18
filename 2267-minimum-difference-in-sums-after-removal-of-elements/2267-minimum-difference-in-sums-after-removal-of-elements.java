import java.util.*;

class Solution {
    public long minimumDifference(int[] nums) {
        int n = nums.length / 3;
        int len = nums.length;

        long[] leftSum = new long[len];
        PriorityQueue<Integer> maxHeap = new PriorityQueue<>(Collections.reverseOrder());
        long leftTotal = 0;


        for (int i = 0; i < 2 * n; i++) {
            maxHeap.add(nums[i]);
            leftTotal += nums[i];
            if (maxHeap.size() > n) {
                leftTotal -= maxHeap.poll();
            }
            if (maxHeap.size() == n) {
                leftSum[i] = leftTotal;
            }
        }

        long[] rightSum = new long[len];
        PriorityQueue<Integer> minHeap = new PriorityQueue<>();
        long rightTotal = 0;
        for (int i = len - 1; i >= n; i--) {
            minHeap.add(nums[i]);
            rightTotal += nums[i];
            if (minHeap.size() > n) {
                rightTotal -= minHeap.poll(); 
            }
            if (minHeap.size() == n) {
                rightSum[i - 1] = rightTotal;
            }
        }

        long res = Long.MAX_VALUE;
        for (int i = n - 1; i < 2 * n; i++) {
            res = Math.min(res, leftSum[i] - rightSum[i]);
        }

        return res;
    }
}
