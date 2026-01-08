import java.util.*;
public class App {
    public static void main (String Args[]){
        String str,str1,str2,ans;
        Scanner s=new Scanner(System.in);
        str1=s.next();
        str2=s.next();
        str=s.nextLine().trim();
        s.close();
        ans=str.substring(0,1).toUpperCase()+str.substring(1,str.length()-1)+", ";
        ans+=str1.substring(0,1).toLowerCase()+str1.substring(1)+" "+str2+"?";
        System.out.println(ans);
    }
}
