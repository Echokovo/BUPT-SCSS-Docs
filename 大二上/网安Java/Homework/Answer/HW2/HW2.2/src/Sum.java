import java.util.Scanner;
public class Sum {
    public static void main(String Args[]){
        Scanner scanner=new Scanner(System.in);
        System.out.print("Enter an integer: ");
        int n=scanner.nextInt();
        System.out.print("Enter a floating point number: ");
        double d=scanner.nextDouble();
        System.out.print("Enter your name: ");
        String s=scanner.next();
        System.out.printf("Hi! %s, the sum of %d and %.2f is %.2f",s,n,d,n+d);
        scanner.close();
    }
}
