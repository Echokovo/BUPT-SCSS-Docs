/** An interface with common collection operations.
*/
public interface Database {

   // REMEMBER THAT ALL MEMBERS OF AN INTERFACE ARE PUBLIC BY DEFAULT

   /** The default initial size of a database. */
   int STARTSIZE = 20;  // this is public, static, final by default

   /** Find out how many things are actually in the database.
       @return the number
   */
   int size();

   /** Display the items in the database on the screen.
   */
   void display();

   /** Find a particular item in the database.
       @param o the object to search for, based on equals
       @return the object if found, null otherwise
   */
   Object find(Object o);

   /** Add an item to the database, if there is room.
       @param o the object to add
       @return true if added, false otherwise
   */
   boolean add(Object o);

   /** Delete an item from the database, if it is there.
       @param o the object to delete
       @return the item if deleted, null otherwise
   */
   Object delete(Object o);

}
