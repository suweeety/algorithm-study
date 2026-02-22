package SWEA.재귀.Q1피보나치수열;

public class FibonacciStairs {
    /**
     * 4개의 계단을 오르는 경우 5가지의 경우의 수를 반환합니다.
     */
    public static void main(String[] args) {
        int n = 4;

        System.out.println("계단을 오르는 방식 : " + calcDynamicFibonacci(n)); // 동적계획법 : 5
        System.out.println("계단을 오르는 방식 : " + calcRecursiveFibonacci(n + 1)); // 재귀함수 : 5
    }

    /**
     * 피보나치수를 이용한 경우의 수 계산방법 : 동적 계획법(DP)을 이용한 방법
     *
     * @param n
     * @return
     */
    public static int calcDynamicFibonacci(int n) {
        // [STEP1] 계단이 1개일 경우 값을 즉시 1로 리턴합니다.
        if (n <= 1) {
            return n;
        }

        // [STEP2] 계단을 오르는 방법에는 한 계단과 두 계단 방법으로 첫번째와 두번째 배열에 값을 지정합니다.
        int[] dp = new int[n + 1];
        dp[1] = 1;
        dp[2] = 2;

        // [STEP3] 3번째 요소부터 배열을 순회하면서 이전 계단을 오르는 방법의 수를 더하여 계산을 합니다.
        for (int i = 3; i <= n; i++) {
            dp[i] = dp[i - 1] + dp[i - 2];
        }

        return dp[n];
    }

    /**
     * 피보나치수를 이용한 경우의 수 계산방법 : 재귀함수를 이용한 방법
     * @param n
     * @return
     */
    public static int calcRecursiveFibonacci(int n) {
        if (n <= 1) {
            return n;
        } else {
            return calcRecursiveFibonacci(n - 1) + calcRecursiveFibonacci(n - 2);
        }
    }

}

