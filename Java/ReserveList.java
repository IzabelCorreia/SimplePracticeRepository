import java.util.ArrayList;
import java.util.Collections;
import java.util.List;

public  class ReserveList{
   
   public void reserveList(){
    List <String> names = new ArrayList<>();
    names.add("Izabel");
    names.add("Cristiano Ronaldo");

    System.out.println(names);
    Collections.reverse(names);
   }

   public static void main(String [] args){
    ReserveList rl = new ReserveList();
    rl.reserveList();
   }
}
