package Bronze.CLASS1.별찍기마이너스2;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
    public static void main(String[] args) throws IOException {
        // 공백개수 : N-i개
        // 별개수 : i개

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());
        StringBuilder sb = new StringBuilder();
        for (int i = 1; i <= N; i++) {
            // 공백
            for (int j = 0; j < N - i; j++) {
                sb.append(' ');
            }
            // 별 찍기
            for (int j = 0; j < i; j++) {
                sb.append('*');
            }
            sb.append('\n');
        }
        System.out.println(sb.toString());
    }
}
