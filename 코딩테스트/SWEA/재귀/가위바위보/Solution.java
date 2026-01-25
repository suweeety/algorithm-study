package SWEA.재귀.가위바위보;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;
import java.io.IOException;

public class Solution {

    public static void main(String args[]) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        // A, B 입력받기
        StringTokenizer st = new StringTokenizer(br.readLine());
        int A = Integer.parseInt(st.nextToken());
        int B = Integer.parseInt(st.nextToken());

        // 조건문 분기 (가위 = 1. 바위 = 2, 보 = 3, 비기는 경우 없음)
        if (A == 1) {
            System.out.println(B == 2 ? "B" : "A");
        } else if (A == 2) {
            System.out.println(B == 1 ? "B" : "A");
        } else {
            System.out.println(B == 1 ? "B" : "A");
        }
    }
}
