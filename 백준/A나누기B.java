import java.util.Scanner;

public class A나누기B {

/*
문제에서 실제 정답과 출력값의 절대 오차 또는 상대오차 이하로 출력 하려면
반드시 double(실수)형으로 출력 해주어야 한다.
나눗셈을 할 때는 반드시 하나의 값이 실수여야 한다.
*/

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        double a,b;
        a = scanner.nextDouble();
        b = scanner.nextDouble();

        System.out.println(a/b);
    }
}