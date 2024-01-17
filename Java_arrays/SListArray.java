import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;
import java.util.HashMap;
import java.util.Map;

public class SListArray extends SList{

    String[] test = new String[8];
    String[] backing = new String[8];

    // doubles the size of the given array
    public void bigger_array(int size){
        backing = test;
        test = new String[size*2];        

        for(int i=0; i < backing.length; i++){
            test[i] = backing[i];
        }
        backing = new String[test.length];
    }

    // creates an empty array
    public SListArray(){
        test = new String[8];
    }

    //creates a list with the strings in elements
    public SListArray(String[] elements){

        test = new String[8];

        // makes array larger when reached max capacity
        if(elements.length >= test.length){
            bigger_array(elements.length);
        }
        
        // transfers elements from given array to this array
        for(int i=0; i < elements.length; i++){
            test[i] = elements[i];
        }
    }

    @Override
    public String get(int position){
        if(test[position] != null){
            return test[position];
        }
        else{
            return INDEX_OUT_OF_RANGE;
        }
    }

    @Override
    public String set(int position, String element){
        String og;

        // if position is in range
        if(position > -1){
            if(test[position] != null){
                og = test[position];
                test[position] = element;
                return og;
            }
            else{
                return INDEX_OUT_OF_RANGE;
            }
        }
        else{
            return INDEX_OUT_OF_RANGE;
        }
    }

    @Override
    public String add(int position, String element){
        String value = "";
        String next_value = "";
    
        // doubles the size of array if it's at max capacity
        if(position > -1){
            if(this.size() == test.length){
                bigger_array(this.size());
            }

            // if 0 <= position <= length of array
            if(position >= 0 && position <= this.size()){
                
                // adds the element to the given array position & moves the other values up an index
                for(int i=position; i < test.length; i++){
                    if(i == position){
                        next_value = test[i];
                        test[i] = element;
                    }
                    else{
                        value = next_value;
                        next_value = test[i];
                        test[i] = value;
                    }
                }
                return INDEX_OK;
            }
            else{
                return INDEX_OUT_OF_RANGE;
            }
        }
        else{
            return INDEX_OUT_OF_RANGE;
        }
    }

    @Override
    public String remove(int position){
        String value;
        String next_value;

        // if there exists a value at given index position
        if(position > -1){
            if(test[position] != null){
                value = test[position];
                for(int i=position; i < test.length-1; i++){
                    next_value = test[i+1];
                    test[i] = next_value;
                }
                return value;
            }
            else{
                return INDEX_OUT_OF_RANGE;
            }
        }
        else{
            return INDEX_OUT_OF_RANGE;
        }
    }

    @Override
    public int size(){
        int size = 0;
        for(int i=0; i < test.length; i++){
            if(test[i] != null){
                size++;
            }
        }
        return size;
    }

    @Override
    public void append(SList anotherSList){
        int len = this.size();
        int len_2 = anotherSList.size();
        int size = len + len_2;

        // doubles the size of array+anotherSList if it's at max capacity
        if((test.length - this.size()) < len_2){
            bigger_array(size);
        }
        
        // appends the elements of another SList to the end of this array
        for(int i=0; i < len_2; i++){
            this.add(len, anotherSList.get(i));
            len++;
        }
    }

    @Override
    public SList commonStrings(){
        HashMap<String, Integer> map_frequency = new HashMap<String, Integer>();
        SList new_list = new SListArray();
        int large_value = 0;
        int count = 0;
        String key;
        int value;

        // iterates over list to fill HashMap
        for(int i=0; i < this.size(); i++){
            map_frequency.merge(this.get(i), 1, Integer::sum);
        }
        // finds the largest frequency(value) in the HashMap
        for(Map.Entry<String, Integer> entry : map_frequency.entrySet()){
            value = entry.getValue();
            if(value > large_value){
                large_value = value;
            }
        }
        // builds new SList containing the highest frequency strings
        for(Map.Entry<String, Integer> entry : map_frequency.entrySet()){
            key = entry.getKey();
            value = entry.getValue();
            if(value == large_value){
                new_list.add(count, key);
                count++;
            }
        }
        return new_list;
    }

    @Override
    public SList[] commonStrings(int n){
        HashMap<String, Integer> map_frequency = new HashMap<String, Integer>();
        ArrayList<Integer> array_1 = new ArrayList<>();
        SList[] multiple_dim = new SListArray[n];
        String[] new_array_2 = new String[0];
        
        String key;
        int value;
        int count;

        // iterates over list to fill HashMap
        for(int i=0; i < this.size(); i++){
            map_frequency.merge(this.get(i), 1, Integer::sum);
        }

        // builds an ArrayList containing the frequency of every string
        for(Map.Entry<String, Integer> entry : map_frequency.entrySet()){
            value = entry.getValue();
            if(!array_1.contains(value))
                array_1.add(value);
        }

        // sorts ArrayList in descending order
        Collections.sort(array_1, Collections.reverseOrder());

        // fills 2D SList
        for(int i=0; i < n; i++){
            
            // resets the attributes
            count = 0;
            ArrayList<String> array_2 = new ArrayList<>();

            // iterates through HashMap to find the key that maps to the required frequency value
            for(Map.Entry<String, Integer> entry : map_frequency.entrySet()){
                key = entry.getKey();
                value = entry.getValue();
                if(array_1.get(i) == value){
                    array_2.add(count, key);
                    count++;
                }
            }
            
            // converts the ArrayList to a String array
            new_array_2 = new String[array_2.size()];
            for(int j=0; j < array_2.size(); j++){
                new_array_2[j] = array_2.get(j);
            }

            // creates a new SList containing the String array made above
            SList new_list = new SListArray(new_array_2);
            multiple_dim[i] = new_list;
        }
        return multiple_dim;
    }
    
    @Override
    public String toString(){
        return Arrays.toString(test);
    }


}