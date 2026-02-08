package Bronze.새싹.아스키코드;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        // 자바에서 char 타입을 정수형으로 출력하면 자동으로 ASCII 코드값이 출력된다.
        char ch = br.readLine().charAt(0);

        System.out.println((int)ch);
    }
}
