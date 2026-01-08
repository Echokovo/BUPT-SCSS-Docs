public class Cat extends Pet {
    boolean state;

    public Cat(String pname, String oname, double wt) {
        super(pname, oname, wt);
        state = false;
    }

    @Override
    public String toString() {
        if (state)
            return "outside cat " + super.toString();
        return "inside cat " + super.toString();
    }

    void goOutside() {
        state = true;
    }

    @Override
    public double visit(int shots) {
        if (state == true)
            return super.visit(shots + 1, 20);
        return super.visit(shots, 20);
    }
}
