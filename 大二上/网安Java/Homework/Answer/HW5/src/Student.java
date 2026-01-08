public class Student extends Human implements Measurable{
    private String school;

    public Student(int age,String school) {
        super(age);
        this.school=school;
    }
    public double getMeasurement(){
        return age;
    }
}
