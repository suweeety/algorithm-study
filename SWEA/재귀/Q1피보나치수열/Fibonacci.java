package SWEA.재귀.Q1피보나치수열;

public class Fibonacci {

    /**
     * @param n
     * @return
     */
    public static int fibo(int n) {
        // [Base Case] n이 1이나 2이면 1을 반환 (이미지 속 조건: n <= 2)
        if (n <= 2) {
            return 1;
        }

        // [Recursive Step] F(n) = F(n-1) + F(n-2)
        return fibo(n - 1) + fibo(n - 2);
    }

    public static void main(String[] args) {
        int n = 10;

        System.out.println(n + "번째 피보나치 수: " + fibo(n));

        // 반복문을 통해 수열 여러 개 출력해보기
        System.out.print("피보나치 수열: ");
        for (int i = 1; i <= n; i++) {
            System.out.print(fibo(i) + " ");
        }
    }
}
