package Bronze.CLASS1.나머지;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        boolean[] check = new boolean[42]; // 나머지의 범위 0~41

        for (int i = 0; i < 10; i++) {
            int n = Integer.parseInt(br.readLine());
            int result = n % 42;
            check[result] = true;
        }

        int count = 0;

        for (int i = 0; i < 42; i++) {
            if (check[i]) count++;
        }
        System.out.println(count);
    }
}
