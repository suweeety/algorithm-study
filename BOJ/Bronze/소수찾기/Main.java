package Bronze.CLASS2.소수찾기;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        // 소수 : 1보다 크고, 1과 자기 자신 외에는 나누어떨어지지 않는 수
        // Math.sqrt(n) : n의 제곱근(√n) 을 구하는 함수
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int N = Integer.parseInt(br.readLine());
        int count = 0;
        StringTokenizer st = new StringTokenizer(br.readLine());
        for (int i = 0; i < N; i++) {
            int num = Integer.parseInt(st.nextToken());

            if (num > 1) {
                boolean prime = true;
                for (int j = 2; j <= Math.sqrt(num); j++) {
                    if (num % j == 0) {
                        prime = false;
                        break;
                    }
                }
                if (prime) count++;
            }
        }

        System.out.println(count);
    }
}
