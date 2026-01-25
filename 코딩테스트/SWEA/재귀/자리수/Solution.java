package SWEA.재귀.자리수;

import java.util.Scanner;

class Solution
{
    public static void main(String args[]) throws Exception
    {
        Scanner sc = new Scanner(System.in);

        int N = sc.nextInt();

        String str = String.valueOf(N);

        int sum = 0;

        for (int i = 0; i < str.length(); i++)
        {
            char ch = str.charAt(i);
            sum += (ch - '0');
        }
        System.out.println(sum);
        sc.close();
    }
}



