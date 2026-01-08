/**
 * This program does not test everything your class
 * system is supposed to do, so you might want to write
 * some of your own tests.
 */
public class P3main {

   /**
    * Main driver method.
    * 
    * @param args the arguments (not used)
    */
   public static void main(String[] args) {
      Vet avet = new Vet(50, "Pets R Us");
      Pet p;

      p = new Pet("Rudolph", "Santa Claus", 350);
      p.visit(1);
      avet.add(p);
      avet.add(new Pet("Tweetie Bird", "Looney Tunes", 1.75));
      System.out.println("visit1: " + p.visit(1));
      System.out.println();
      show(avet);

      p = new Cat("Tiger", "Some Body", 8);
      avet.add(p);
      System.out.println("visit0: " + p.visit(0));

      Cat c = new Cat("Sylvester", "Looney Tunes", 15.5);
      System.out.println("inside visit1: " + c.visit(1));
      c.goOutside();
      System.out.println("outside visit1: " + c.visit(1));
      System.out.println("c is " + c);
      avet.add(c);

      System.out.println();
      show(avet);

      Dog d = new Dog("Fido", "Some Body", 32.2, "medium");
      System.out.println("med visit3: " + d.visit(3));
      avet.add(d);

      p = new Dog("Dino", "Flintstones", 150, "large");
      avet.add(p);
      System.out.println("lg visit3: " + p.visit(3));
      System.out.println();
      show(avet);

      avet.add(new Dog("Benji", "Joe Camp", 10, "small"));
      p = new Cat("Tony", "Kellogg", 20);
      avet.add(p);
      System.out.println();
      show(avet);

      System.out.println("\na few more tests...");
      System.out.println("find p: " + avet.find(p));
      p = (Pet) avet.find(new Pet("Tweetie Bird", "Looney Tunes", 1.5));
      System.out.println("Tweetie 5 shots: " + p.visit(5));
      System.out.println("found Tweetie: " + p);

      System.out.println("find Fido: "
            + avet.find(new Dog("Fido", "some body", 32.2, "medium")));

      System.out.println("adding string to Vet: " + avet.add("not a pet"));
      System.out.println("deleting string: " + avet.delete("just a string"));

      System.out.println();
      System.out.println("\ndeleting pets:");
      System.out.println(avet.delete(p));
      System.out.println(avet.delete(d));
      System.out.println(avet.delete(c));
      show(avet);

      avet.add(new Pet("Happy", "Some Body", 13.5));
      avet.sort();
      System.out.println("\nafter sorting:");
      show(avet);
   }

   /**
    * Output the current state of things to the screen.
    * 
    * @param myvet the vet records to display
    */
   public static void show(Vet myvet) {
      System.out.println("--- Vet has " + myvet.size() + " clients");
      myvet.display();
      System.out.println(">> average client weight: " + myvet.averageWeight());
   }
}

/*
 * Here is the result of running the program:
 * 
 * visit1: 115.0
 * 
 * --- Vet has 2 clients
 * Vet Pets R Us client list:
 * Rudolph (owner Santa Claus) 350.0 lbs, $115.00 avg cost/visit
 * Tweetie Bird (owner Looney Tunes) 1.75 lbs, $0.00 avg cost/visit
 * >> average client weight: 175.875
 * visit0: 105.0
 * inside visit1: 135.0
 * outside visit1: 165.0
 * c is outside cat Sylvester (owner Looney Tunes) 15.5 lbs, $150.00 avg
 * cost/visit
 * 
 * --- Vet has 4 clients
 * Vet Pets R Us client list:
 * Rudolph (owner Santa Claus) 350.0 lbs, $115.00 avg cost/visit
 * Tweetie Bird (owner Looney Tunes) 1.75 lbs, $0.00 avg cost/visit
 * inside cat Tiger (owner Some Body) 8.0 lbs, $105.00 avg cost/visit
 * outside cat Sylvester (owner Looney Tunes) 15.5 lbs, $150.00 avg cost/visit
 * >> average client weight: 93.8125
 * med visit3: 197.5
 * lg visit3: 205.0
 * 
 * --- Vet has 6 clients
 * Vet Pets R Us client list:
 * Rudolph (owner Santa Claus) 350.0 lbs, $115.00 avg cost/visit
 * Tweetie Bird (owner Looney Tunes) 1.75 lbs, $0.00 avg cost/visit
 * inside cat Tiger (owner Some Body) 8.0 lbs, $105.00 avg cost/visit
 * outside cat Sylvester (owner Looney Tunes) 15.5 lbs, $150.00 avg cost/visit
 * medium dog Fido (owner Some Body) 32.2 lbs, $197.50 avg cost/visit
 * large dog Dino (owner Flintstones) 150.0 lbs, $205.00 avg cost/visit
 * >> average client weight: 92.90833333333335
 * 
 * --- Vet has 8 clients
 * Vet Pets R Us client list:
 * Rudolph (owner Santa Claus) 350.0 lbs, $115.00 avg cost/visit
 * Tweetie Bird (owner Looney Tunes) 1.75 lbs, $0.00 avg cost/visit
 * inside cat Tiger (owner Some Body) 8.0 lbs, $105.00 avg cost/visit
 * outside cat Sylvester (owner Looney Tunes) 15.5 lbs, $150.00 avg cost/visit
 * medium dog Fido (owner Some Body) 32.2 lbs, $197.50 avg cost/visit
 * large dog Dino (owner Flintstones) 150.0 lbs, $205.00 avg cost/visit
 * small dog Benji (owner Joe Camp) 10.0 lbs, $0.00 avg cost/visit
 * inside cat Tony (owner Kellogg) 20.0 lbs, $0.00 avg cost/visit
 * >> average client weight: 73.43125
 * 
 * a few more tests...
 * find p: inside cat Tony (owner Kellogg) 20.0 lbs, $0.00 avg cost/visit
 * Tweetie 5 shots: 235.0
 * found Tweetie: Tweetie Bird (owner Looney Tunes) 1.75 lbs, $235.00 avg
 * cost/visit
 * find Fido: medium dog Fido (owner Some Body) 32.2 lbs, $197.50 avg cost/visit
 * adding string to Vet: false
 * deleting string: null
 * 
 * 
 * deleting pets:
 * Tweetie Bird (owner Looney Tunes) 1.75 lbs, $235.00 avg cost/visit
 * medium dog Fido (owner Some Body) 32.2 lbs, $197.50 avg cost/visit
 * outside cat Sylvester (owner Looney Tunes) 15.5 lbs, $150.00 avg cost/visit
 * --- Vet has 5 clients
 * Vet Pets R Us client list:
 * Rudolph (owner Santa Claus) 350.0 lbs, $115.00 avg cost/visit
 * inside cat Tiger (owner Some Body) 8.0 lbs, $105.00 avg cost/visit
 * large dog Dino (owner Flintstones) 150.0 lbs, $205.00 avg cost/visit
 * small dog Benji (owner Joe Camp) 10.0 lbs, $0.00 avg cost/visit
 * inside cat Tony (owner Kellogg) 20.0 lbs, $0.00 avg cost/visit
 * >> average client weight: 107.6
 * 
 * after sorting:
 * --- Vet has 6 clients
 * Vet Pets R Us client list:
 * large dog Dino (owner Flintstones) 150.0 lbs, $205.00 avg cost/visit
 * small dog Benji (owner Joe Camp) 10.0 lbs, $0.00 avg cost/visit
 * inside cat Tony (owner Kellogg) 20.0 lbs, $0.00 avg cost/visit
 * Rudolph (owner Santa Claus) 350.0 lbs, $115.00 avg cost/visit
 * Happy (owner Some Body) 13.5 lbs, $0.00 avg cost/visit
 * inside cat Tiger (owner Some Body) 8.0 lbs, $105.00 avg cost/visit
 * >> average client weight: 91.91666666666667
 * 
 */
