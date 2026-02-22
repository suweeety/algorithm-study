package Bronze.CLASS1.ACM호텔;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int T = Integer.parseInt(br.readLine());
        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < T; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            int H = Integer.parseInt(st.nextToken()); // 층수
            int W = Integer.parseInt(st.nextToken()); // 각 층의 방 수
            int N = Integer.parseInt(st.nextToken()); // 몇 번째 손님인지

            int floor = N % H;
            int room = N / H + 1;

            if (floor == 0) {
                floor = H;
                room = N / H;
            }
            sb.append(floor * 100 + room).append('\n');
        }
        System.out.println(sb.toString());
    }
}
