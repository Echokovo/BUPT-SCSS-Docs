public class Dog extends Pet {

    private final String size;

    public Dog(String pname, String oname, double wt, String s) {
        super(pname, oname, wt);
        this.size = s;
    }

    @Override
    public String toString() {
        return size + " dog " + super.toString();
    }

    @Override
    public double visit(int shots) {
        double tempCost = shots;
        if ("medium".equals(size))
            tempCost *= 2.5;
        if ("large".equals(size))
            tempCost *= 5;
        if ("small".equals(size))
            tempCost = 0;
        return super.visit(shots, 15 + tempCost);
    }
}
