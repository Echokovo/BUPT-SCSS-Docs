import java.util.Arrays;

/**
 * Class to keep track of client (Pet) information for a Veterinary
 * practice. Some methods are sketched for you, but others will need
 * to be added in order to implement the Database interface and
 * support the P3main program and expected output. You'll also need
 * to add the data members.
 */
public class Vet implements Database {

    int startSize;
    String name;
    int numOfClients;
    Pet[] clients;

    /**
     * Create a veterinary practice.
     * 
     * @param startSize the capacity for how
     *                  many clients they can handle
     * @param who       the name of the vet practice
     */
    public Vet(int startSize, String who) {
        this.startSize = startSize;
        this.name = who;
        numOfClients = 0;
        clients = new Pet[startSize];
    }

    /**
     * Display the name of the Vet and all the clients, one per line,
     * on the screen. (See sample output for exact format.)
     */
    @Override
    public void display() {
        System.err.println("Vet " + name + " client list: ");
        for (Pet pet : clients)
            if (pet != null)
                System.out.println(pet);
    }

    /**
     * Add an item to the database, if there is room.
     * You are limited by the initial capacity.
     * 
     * @param o the object to add (must be a Pet)
     * @return true if added, false otherwise
     */
    @Override
    public boolean add(Object o) {
        if (o instanceof Pet && numOfClients <= startSize) {
            clients[numOfClients++] = (Pet) o;
            return true;
        }
        return false;
    }

    @Override
    public Object find(Object o) {
        for (Pet pet : clients)
            if (pet != null && pet.equals((Pet) o))
                return pet;
        return null;
    }

    /**
     * Delete an item from the database, if it is there,
     * maintaining the current ordering of the list.
     * 
     * @param o the object to delete
     * @return the item if one is deleted, null otherwise
     */
    @Override
    public Object delete(Object o) {
        if (!(o instanceof Pet))
            return null;
        for (int i = 0; i < numOfClients; i++) {
            if (clients[i] != null && clients[i].equals(o)) {
                Pet removedPet = clients[i];
                for (int j = i; j < numOfClients - 1; j++) {
                    clients[j] = clients[j + 1];
                }
                clients[numOfClients - 1] = null;
                numOfClients--;
                return removedPet;
            }
        }
        return null;
    }

    /**
     * Compute the average weight over all clients.
     * 
     * @return the average
     */
    public double averageWeight() {
        double ret = 0;
        for (Pet pet : clients)
            if (pet != null)
                ret += pet.getWeight();
        return ret / numOfClients;
    }

    @Override
    public int size() {
        return numOfClients;
    }

    /**
     * Sort the clients. (This is complete.)
     */
    public void sort() {
        Arrays.sort(this.clients, 0, this.size());
    }

}
