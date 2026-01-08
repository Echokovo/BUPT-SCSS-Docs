import java.util.Objects;
public class Student extends Human{
    String school;
    void eat(){
        System.out.println("["+school+"]"+name+" is eating.");
    }
    void study() {
        System.out.println("["+school+"]"+name+" is studying.");
    }
    public Student(String name, int age, String school){
        super(name,age);
        this.school=school;
    }
    public String toString(){
        return "["+id+"]"+"["+school+"]"+name;
    }
    public boolean equals(Object obj){
        if (this == obj)
            return true;
        if (!(obj instanceof Student))
            return false;
        Student s = (Student) obj;
        return super.equals(s) && Objects.equals(this.school, s.school);
    }
    public int hashCode() {
        return Objects.hash(super.hashCode(), school);
    }
}
