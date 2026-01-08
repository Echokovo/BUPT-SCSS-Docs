import java.util.Scanner;
public class bin2dec {
    public static void main(String Args[]){
        Scanner scanner=new Scanner(System.in);
        System.out.print("Enter an integer: ");
        String s=scanner.next();
        scanner.close();
        for(int i=0;i<s.length();i++){
            if(s.charAt(i)>='2'){
                System.out.printf("Error: Invalid Binary String \"%s\"",s);
                return;
            }
        }
        System.out.printf("The equivalent decimal number for binary \"%s\" is %d",s,Integer.parseInt(s,2));
    }
}
