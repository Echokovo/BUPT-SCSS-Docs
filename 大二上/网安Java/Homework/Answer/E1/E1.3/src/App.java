import java.util.Calendar;
import java.util.Scanner;
public class App {
    public static void main(String[] args) {
        System.out.println("请输入出生日期，格式为'2007 12 3'");
        Scanner s = new Scanner(System.in);
        int tyear = s.nextInt();
        int tmonth = s.nextInt() - 1;
        int tday = s.nextInt();
        s.close();
        Calendar c = Calendar.getInstance();
        int nyear = c.get(Calendar.YEAR);
        int[] rate = new int[7];
        for (int i = tyear; i <= nyear; i++) {
            rate[printCalendar(i, tmonth, tday) - 1]++;
        }
        printRate(rate);
    }
    public static int printCalendar(int year, int month, int day) {
        System.out.println(year);
        Calendar c = Calendar.getInstance();
        c.clear();
        c.set(year, month, 1);
        int cnt = (c.get(Calendar.DAY_OF_WEEK) + 5) % 7;
        System.out.println("Mon\tTue\tWed\tThu\tFri\tSat\tSun");
        for (int i = 1; i <= cnt; i++) {
            System.out.print("\t");
        }
        for (int i = 1; i <= c.getActualMaximum(Calendar.DAY_OF_MONTH); i++) {
            if (i == day) {
                System.out.print(i + "*\t");
            } else {
                System.out.print(i + "\t");
            }
            if ((i + cnt) % 7 == 0) {
                System.out.println();
            }
        }
        System.out.println();
        int rate = (day + cnt - 7) % 7;
        return rate;
    }
    public static void printRate(int[] arr) {
        int sum = 0;
        for (int i = 0; i < arr.length; i++) {
            sum += arr[i];
        }
        for (int i = 0; i < arr.length; i++) {
            double rate = 1.0 * arr[i] / sum;
            System.out.printf("星期%d : %.3f\n", (i + 1), rate);
        }
    }
}