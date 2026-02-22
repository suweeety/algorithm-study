package Bronze.새싹.학점계산;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String grade = br.readLine();
        double score = 0.0;

        // F는 1글자이므로 예외 처리
        if (grade.equals("F")) {
            System.out.println(score);
            return;
        }

        char ch = grade.charAt(0);
        if (ch == 'A') score = 4.0;
        else if (ch == 'B') score = 3.0;
        else if (ch == 'C') score = 2.0;
        else if (ch == 'D') score = 1.0;

        ch = grade.charAt(1);
        if (ch == '+') score += 0.3;
        else if (ch == '-') score -= 0.3;

        System.out.println(score);
    }
}
