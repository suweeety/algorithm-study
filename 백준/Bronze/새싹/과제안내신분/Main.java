package Bronze.새싹.과제안내신분;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        // 출석번호 할당
        boolean[] arr = new boolean[31];
        // 출석한 28명 체크
        for (int i = 0; i < 28; i++) {
            int n = Integer.parseInt(br.readLine());
            arr[n] = true;
        }
        // false 출력(작은 번호 먼저)
        for (int i = 1; i <= 30; i++) {
            if (!arr[i]) {
                System.out.println(i);
            }
        }
    }
}
