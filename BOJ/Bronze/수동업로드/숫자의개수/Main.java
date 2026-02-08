package Bronze.CLASS1.숫자의개수;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int A = Integer.parseInt(br.readLine());
        int B = Integer.parseInt(br.readLine());
        int C = Integer.parseInt(br.readLine());

        int result = A * B * C;
        // 문자열로 변환
        String str = String.valueOf(result);
        //숫자 0~9를 세려면 길이가 10짜리 정수 배열을 만든다
        int[] count = new int[10];

        for (int i = 0; i < str.length(); i++) {
            int num = str.charAt(i) - '0';
            count[num]++;
        }
        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < 10; i++) {
            sb.append(count[i]).append('\n');
        }
        System.out.println(sb.toString());
    }
}
