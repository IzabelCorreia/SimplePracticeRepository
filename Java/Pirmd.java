public class Pirmd{

    public void reservePyramid(){
        int rows = 8;
        for(int i=rows; i >= 1; i--){
            for(int j=0; j <= rows-i; j++){
                System.out.print(" ");
            }
            for (int k = 0; k <= i - 1; k++){
               System.out.print("*" + " "); 
            }   
            System.out.println();
        }

    }
    public void pyramid(){
        int rows = 8;
        for(int i = 0; i<= rows; i++){
            for(int j=0; j <= rows-i; j++){
                System.out.print(" ");
            }
            for(int k=0; k <= i - 1; k++){
                System.out.print("*" + " ");
            }
            System.out.println();
        }
    }
    public static void main(String [] args){
        Pirmd rs = new Pirmd();
        System.out.println("\nPIRAMEDE INVERTIDA \n");
        rs.reservePyramid();
        rs.pyramid();
    }
}
