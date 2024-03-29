import java.util.Arrays;
import java.util.LinkedList;

/**
 * A string list specification. 
 */
public abstract class SList{
    /** A static attribute that tells the autograder to display test cases that 
     * passed. Setting this to <code>false</code> in the concrete class
     * constructors will tell the autograder to hide your passed tests and
     * only show failed test cases. This is experimental and may not be implemented
     * in the autograder.  
     */
    public static boolean SHOW_PASSED_TEST_CASES = true;

    /** A constant string used to indicate that an operation failed 
     * because it wanted to access a list element that did not exist.
     * We use this to ensure that the code does not crash with  
     * <code>java.lang.ArrayIndexOutOfBoundsException</code>*/ 
    public static final String INDEX_OUT_OF_RANGE = "INDEX_OUT_OF_RANGE";

    /** A constant string used to indicate that the index specified 
     * for an operation were valid. */ 
    public static final String INDEX_OK = "INDEX_OK";



    /**
     * Returns (but does not remove) the string at the given position.
     * 
     * @param position is the position of the string that is retrieved. 
     * @return The string at the given position. 
     *         If the <code>position</code> was not a valid list position 
     *         then returns <code>INDEX_OUT_OF_RANGE</code>. 
     */
    public abstract String get(int position);

    /**
     * Sets the list element at the given position. 
     * <p>
     * Changes the value (string) of the list element at the given position and
     * returns the original value (string)
     * 
     * @param position specifies the location in the list whose value will be changed.
     * @param element specifies the new value that the list element at the given <code>position</code> will have. 
     * @return Returns the string that was initially in location <code>position</code>.
     *         If the <code>position</code> was not a valid list position 
     *         then returns <code>INDEX_OUT_OF_RANGE</code>. 
     */
    public abstract String set(int position, String element);

    /**
     * Adds a new string to the given location of the list. 
     * <p>
     * Adds a new string to the list at the given position. In order to 
     * successfully add a new item to the list, the <code>position</code>
     * must satisfy 0 <= <code>position</code> <= <code>this.size()</code>
     * If this is not satisfied, then the method simply returns <code>INDEX_OUT_OF_RANGE</code>.
     * If this is satisfied, it adds the new string and returns <code>INDEX_OK</code>.
     * 
     * @param position specifies the location in the list where the new <code>element</code> will be added. 
     * @param element specifies string that is being added at the given <code>position</code> will have. 
     * @return If the input <code>position</code> was valid then returns <code>INDEX_OK</code>. 
     *         Otherwise, returns <code>INDEX_OUT_OF_RANGE</code>. 
     */
    public abstract String add(int position, String element);

    /**
     * Removes the string at a given location from the list and returns it. 
     * <p>
     * Removes the string in the list at the given position. If that items exists, the 
     * method removes and returns it. If there is no string with the given position, 
     * the list is left unchanged and returns <code>INDEX_OUT_OF_RANGE</code>.
     * 
     * @param position specifies the position of the string to remove. 
     * @return the string that was removed from the list if it existed, otherwise 
     *         returns <code>INDEX_OUT_OF_RANGE</code>. 
     */
    public abstract String remove(int position);

   
    /**
     * Returns the size of the list. 
     * 
     * @return the size of the list. (That is, the number of strings in it.)
     */
    public abstract int size();

 
    
    /**
     * Appends another SList to this list. 
     * <p>
     * Adds a list to the end of this list. 
     * <p>
     * There are no restrictions on the length of either <code>this</code> list
     * or the input <code>anotherSList</code>. 
     * <p>
     * 
     * @param anotherSList is the list that we adding to <code>this</code> list. 
     */
    public abstract void append(SList anotherSList);

    /**
     * Finds the strings that appear the most times in <code>this</code> list.
     * <p>
     * There may be zero, one or more than one string that appears the 
     * most times in <code>this</code> list. The method returns a new 
     * list that contains these strings. 
     * <p>
     * For example, if <code>this</code> is empty, then there are no strings
     * that appear the most times. 
     * <p>
     * If the list is ["cat", "dog", "cat", "eel", "dog"] then the method should
     * return the list ["cat", "dog"].
     * 
     * @return a list containing the strings that appear the most times in <code>this</code> list.
     */
    public abstract SList commonStrings();
        
    /**
     * Finds the strings that appear the most times in <code>this</code> list.
     * <p>
     * Instead of returning a list of the strings that appear the MOST, this 
     * returns <code>n</code> lists, that contain the MOST, Second MOST, ..., <code>n</code>-th MOST 
     * frequently appearing strings in <code>this</code> list.   
     * <p>
     * Examples: If the list is ["A", "A", "A", "B", "B", "C", "C", "D"] 
     * then <code>commonString(1)</code> will return [["A"]] (a list with 1 list in it), and  
     * <code>commonString(2)</code> will return the list [["A"], ["B","C"]], and  
     * <code>commonString(3)</code> will return the list [["A"], ["B","C"], ["D"]].
     *   
     * @param n is the number of lists of commonly used words. <code>n</code> must be 
     *        at least 1.
     * @return a list of lists of the <code>n</code> most commonly appearing strings in <code>this</code> list. 
     */
    public abstract SList[] commonStrings(int n);


    @Override
    public String toString(){
        return "toString(): YOU NEED TO OVERRIDE THIS IN YOUR SListArray CLASS";
    }

    @Override
    public final boolean equals(Object other){
        SList otherList = (SList)other;
        if( this.size() != otherList.size()){
            return false;
        }
        for(int i=0; i<this.size(); i+=1){
            if( !this.get(i).equals(otherList.get(i))){
                return false;
            }
        }
        return true;
    }

}