import java.util.Scanner;

public class 사칙연산 {
    public static void main(String []args) {
        Scanner scanner = new Scanner(System.in);

        int a,b;
        a = scanner.nextInt();
        b = scanner.nextInt();

        System.out.println(a+b);
        System.out.println(a-b);
        System.out.println(a*b);
        System.out.println(a/b);
        System.out.println(a%b);
    }
}
