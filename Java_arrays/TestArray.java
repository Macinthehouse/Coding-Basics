import java.util.Arrays;
import java.util.ArrayList;

public class TestArray{
    public static void main(String[] args){
        // {"C", "D", "E", "F", "G", "H", "I", "J", "A", "A", "B", "B", "C", "C", "C", "C", "E", "E", "E", "E", "A", "B", "D", "D"};
        String[] a = {"A", "A", "B", "A", "B"};
        String[] b = {"I", "J", "K", "D", "E", "F", "G", "H", "I", "J", "A", "A", "B", "B", "C", "C", "E", "E", "E", "E", "A", "B", "D", "D"};
        SList x = new SListArray(a);
        SList y = new SListArray(b);
        System.out.println(x.toString());

        // String z = x.remove(-1);
        // x.append(y);
        // System.out.println(x.toString());
        // System.out.println(z);

        SList[] new_list = (SListArray[]) x.commonStrings(2);

        System.out.println(Arrays.deepToString(new_list));
        
        // for(int i=0; i < x.length; i++){
        //     System.out.println(x[i]);
        // }
    }
}