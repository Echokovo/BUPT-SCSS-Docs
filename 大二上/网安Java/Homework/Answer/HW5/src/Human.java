public class Human implements Measurable{
    protected int age;

    public Human(int age) {
        this.age=age;
    }
    public double getMeasurement(){
        return age;
    }
}
