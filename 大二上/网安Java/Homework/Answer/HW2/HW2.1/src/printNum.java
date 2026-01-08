public class printNum {
    public static void main(String Args[]){
        System.out.print(" * |  1  2  3  4  5  6  7  8  9\n");
        for(int i=1;i<=9;i++){
            System.out.print(" "+i+" |");
            for(int j=i;j<=(9*i);j+=i){
                System.out.printf("%3d",j);
            }
            System.out.print("\n");
        }
    }
}
