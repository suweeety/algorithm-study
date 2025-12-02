package 새싹.개수세기;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        // BufferedReader를 생성하여 입력 속도를 빠르게 함
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        // 첫 번째 줄에서 정수의 개수를 읽어옴
        int N = Integer.parseInt(br.readLine());

        // 두 번째 줄에서 N개의 정수를 공백 기준으로 나누기 위해 StringTokenizer 사용
        StringTokenizer st = new StringTokenizer(br.readLine(), " ");

        // 세 번째 줄에서 찾고자 하는 숫자 v를 읽어옴
        int v = Integer.parseInt(br.readLine());

        // v의 개수를 세기위한 변수 선언
        int count = 0;

        // 반복문
        for (int i = 0; i < N; i++) {
            // st.nextToken()으로 다음 숫자를 문자열로 꺼내고, 정수로 변환
            if (Integer.parseInt(st.nextToken()) == v) {
                count++;
            }
        }
        //출력
        System.out.println(count);
    }
}
