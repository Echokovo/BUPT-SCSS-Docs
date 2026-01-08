public class HW3 {
    public static void main(String[] args) {
        //b. 可以以当前时间构造对象
        Timer T1=new Timer();
        System.out.println(T1);
        //a. 提供两种计时功能，一种以24小时计时，一种以12小时计时；默认以24小时计时
        //c. 可以设置一个特定的时间来构造对象
        //j. 提供toString()方法用来打印时间
        Timer T2=new Timer(14,12);
        Timer T3=new Timer(14,12,true);
        System.out.println(T2);
        System.out.println(T3);
        //d. 能够访问时间的小时数
        //e. 能够访问时间的分钟数
        Timer T4=new Timer(14,12);
        System.out.println(T4.getHour());
        System.out.println(T4.getMinute());
        //f. 提供方法能够将时间增加1小时；
        //g. 提供方法能够将时间增加n小时；
        //h. 提供方法能够将时间增加1分钟；
        //i. 提供方法能够将时间增加n分钟；
        Timer T5=new Timer(11,20,true);
        T5.addHour();
        System.out.println(T5);
        T5.addHour(13);
        System.out.println(T5);
        T5.addMinute();
        System.out.println(T5);
        T5.addMinute(100);
        System.out.println(T5);
    }
}