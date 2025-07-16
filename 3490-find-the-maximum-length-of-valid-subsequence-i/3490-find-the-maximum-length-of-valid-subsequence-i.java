public class Solution {
    public int maximumLength(int[] nums) {
        int i = nums.length;
        if (i == 2) {
            return 2;
        }
        int a = nums[0] & 1;
        int[] gen = new int[3];
        gen[0] = 1 - a;
        gen[1] = a;
        gen[2] = 1;

        for (int j = 1; j < nums.length; j++) {
            int h = nums[j];
            int g = h & 1;
            gen[g & 1]++;
            if (g != a) {
                gen[2]++;
                a = 1 - a;
            }
        }
        return Math.max(Math.max(gen[0], gen[1]), gen[2]);
    }
}
