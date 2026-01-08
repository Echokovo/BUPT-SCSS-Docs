public class HW5 {
    public static void main(String[] args) throws Exception {
        DataSet ds=new DataSet();
        Human H1=new Human(10);
        Human H2=new Human(20);
        Human H3=new Human(30);
        Student S1=new Student(20+8,"BUPT");
        Student S2=new Student(20+18,"BUPT");
        Student S3=new Student(20+28,"BUPT");
        ds.add(H1);
        ds.add(H2);
        ds.add(H3);
        System.out.println(ds.getAverage());
        System.out.println(ds.getMaximum());
        ds.add(S1);
        ds.add(S2);
        ds.add(S3);
        System.out.println(ds.getAverage());
        System.out.println(ds.getMaximum());
    }
}
