import java.util.Objects;
public class Human {
    String name;
    int age;
    static int id=100;
    void eat(){
        System.out.println(name+" is eating.");
    }
    void getId(){
        System.out.println("id:"+id);
    }
    public Human(String name, int age) {
        this.name=name;
        this.age=age;
        id++;
    }
    public boolean equals(Object obj){
        if(this == obj)
            return true;
        if (!(obj instanceof Human))
            return false;
        Human h = (Human) obj;
        return this.name.equals(h.name) && this.age == h.age;
    }
    public String toString(){
        return "["+id+"]"+name;
    }
    public int hashCode(){
        return Objects.hash(name,id);
    }
}
