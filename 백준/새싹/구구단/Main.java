package 새싹.구구단;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();
        int N = Integer.parseInt(br.readLine());
        int result;
        for (int i = 1; i <= 9; i++) {
            result = N * i;
            sb.append(N).append(' ').append('*').append(' ').append(i).append(' ').append('=').append(' ').append(result).append('\n');
        }
        System.out.println(sb.toString());
    }
}
