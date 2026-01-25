package Bronze.CLASS2.분해합;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        String N = br.readLine();
        int n = Integer.parseInt(N);

        for (int i = 1; i < n; i++) {
            int result = i;
            String str = String.valueOf(i);
            for (int j = 0; j < str.length(); j++) {
                result += str.charAt(j) - '0';
            }
            if (result == n) {
                System.out.println(i);
                return;
            }
        }
        System.out.println(0);
    }
}
