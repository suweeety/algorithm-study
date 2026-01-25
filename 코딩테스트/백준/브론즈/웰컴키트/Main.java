package Bronze.CLASS2.웰컴키트;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int N = Integer.parseInt(br.readLine());

        StringTokenizer st = new StringTokenizer(br.readLine());
        StringBuilder sb = new StringBuilder();
        int[] num = new int[6];

        for (int i = 0; i < num.length; i++) {
            num[i] = Integer.parseInt(st.nextToken());
        }

        st = new StringTokenizer(br.readLine());
        int T = Integer.parseInt(st.nextToken());
        int P = Integer.parseInt(st.nextToken());

        int count = 0; // 티셔츠 주문 묶음 수
        for (int i = 0; i < num.length; i++) {
            count += num[i] / T;
            if (num[i] % T != 0) {
                count++;
            }
        }
        sb.append(count).append('\n');

        sb.append(N / P).append(" ").append(N % P);

        System.out.println(sb.toString());
    }
}
