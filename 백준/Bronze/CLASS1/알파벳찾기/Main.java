package Bronze.CLASS1.알파벳찾기;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String S = br.readLine();

        int[] arr = new int[26];
        for (int i = 0; i < arr.length; i++) {
            arr[i] = -1;
        }
        // arr 배열의 인덱스(원소 위치)는 ch 가 갖고 있는 문자 인코딩 값(=아스키코드 값과 동일)에 'a' 또는 97 을 빼주면 된다.
        //( a 는 10진수로 97 이라는 값에 대응된다.)
       for (int i = 0; i < S.length(); i++) {
            int idx = S.charAt(i) - 'a';
           if (arr[idx] == -1) {
               arr[idx] = i;
           }
       }
       StringBuilder sb = new StringBuilder();
        for (int i = 0; i < 26; i++) {
            sb.append(arr[i]).append(" ");
        }
        System.out.println(sb.toString());
    }
}
