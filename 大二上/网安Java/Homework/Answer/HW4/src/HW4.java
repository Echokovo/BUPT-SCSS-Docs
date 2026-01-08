public class HW4 {
    public static void main(String Args[]){
        Human T1=new Human("Name1",18);
        T1.eat();
        T1.getId();
        Student T2=new Student("Name2",19,"BUPT");
        T2.eat();
        T2.getId();
        Human T3=T1;
        T3.eat();
        T3=T2;
        T3.eat();
        Human T4=new Student("Name4",20,"BUPT");
        ((Student)T4).study();
    }
}
