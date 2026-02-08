package Bronze.CLASS2.Hashing;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int L = Integer.parseInt(br.readLine());
        String str = br.readLine();

        int r = 31;
        int M = 1234567891;

        long hash = 0; // 해싱 값
        long pow = 1; // r^1 를 저장할 변수 (처음은 r^0 = 1)

        for (int i = 0; i < L; i++) {
            int value = str.charAt(i) - 'a' + 1; // 알파벳 순서값 (a=1)
            hash = (hash + value * pow) % M; // 해싱 공식 적용
            pow = pow * r % M; // 다음 지수로 업데이트
        }
        System.out.println(hash);
    }
}