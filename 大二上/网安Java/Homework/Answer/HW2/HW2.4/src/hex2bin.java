import java.util.Scanner;
public class hex2bin {
    public static void main(String Args[]){
        String[] hexBits = {
            "0000", "0001", "0010", "0011",
            "0100", "0101", "0110", "0111",
            "1000", "1001", "1010", "1011",
            "1100", "1101", "1110", "1111"};
        Scanner scanner=new Scanner(System.in);
        System.out.print("Enter a Hexadecimal string: ");
        String s=scanner.next();
        scanner.close();
        System.out.printf("The equivalent binary for hexadecimal \"%s\" is",s);
        for(int i=0;i<s.length();i++){
            int t;
            if(s.charAt(i)<='9'){
                t=s.charAt(i)-'0';
            }else{
                t=s.charAt(i)-'a'+10;
            }
            System.out.printf(" %s",hexBits[t]);
        }
    }
}
