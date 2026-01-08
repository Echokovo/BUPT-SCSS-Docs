import java.text.DecimalFormat;

/**
 * This is a class to define Pet objects. Pets should be compared
 * according to their owner's names, ignoring capitalization. Ties
 * should be broken based on the pet's name, ignoring capitalization.
 * 
 * Your job is to add the necessary data and methods to support the
 * P3main program, as well as the related classes in this system. Some
 * required methods are noted below with comments, but these are not the
 * only things you will need.
 */
public class Pet implements Comparable<Pet> {

   /** Handy for formatting. */
   private static DecimalFormat money = new DecimalFormat("0.00");

   /* The access specifiers for these variables must not be changed! */

   private final String name;
   private final String owner;
   private final double weight;

   private int vis;
   private double totalCost;

   /**
    * Create a Pet object, initializing data members.
    * 
    * @param pname the Pet's name
    * @param oname the owner's name
    * @param wt    the weight of the pet
    */
   public Pet(String pname, String oname, double wt) {
      this.name = pname;
      this.owner = oname;
      this.weight = wt;
      vis = 0;
      totalCost = 0;
   }

   @Override
   public String toString() {
      return this.name + " (owner " + this.owner + ") " + this.weight
            + " lbs, $" + money.format(this.avgCost()) + " avg cost/visit  ";
   }

   @Override
   public int compareTo(Pet p) {
      if (this.owner.compareToIgnoreCase(p.owner) != 0)
         return this.owner.compareToIgnoreCase(p.owner);
      if (this.name.compareToIgnoreCase(p.name) != 0)
         return this.name.compareToIgnoreCase(p.name);
      return 1;
   }

   public boolean equals(Pet p) {
      return this.owner.compareToIgnoreCase(p.owner) == 0 && this.name.compareToIgnoreCase(p.name) == 0;
   }

   public double getWeight() {
      return weight;
   }

   /**
    * The Pet is visiting the vet, and will be charged accordingly.
    * The base cost for a visit is $85.00, and $30/shot is added.
    * 
    * @param shots the number of shots the pet is getting
    * @return the entire cost for this particular visit
    */
   public double visit(int shots, double extra) {
      vis++;
      totalCost += 85 + shots * 30 + extra;
      return 85 + shots * 30 + extra;
   }

   public double visit(int shots) {
      vis++;
      totalCost += 85 + shots * 30;
      return 85 + shots * 30;
   }

   /**
    * Determine the average cost per visit for this pet.
    * 
    * @return that cost, or 0 if no visits have occurred yet
    */
   public double avgCost() {
      if (vis == 0)
         return 0;
      return totalCost / vis;
   }

}
