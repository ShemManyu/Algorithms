public class Insertionsort{
    public static void main(String[] args){

        int[] anArray = {11,9,15,0,9,0};
        for (int i = 1; i < anArray.length; i++){
            for(int j = 0; j < i; j++){
                if (anArray[i] < anArray[j]){
                    int temp = anArray[i];
                    for(int k = 1; k <= i-j; k++){
                        anArray[i-k+1] = anArray[i-k];
                    }
                    anArray[j] = temp;
                    break;
                }
            }
            for (int item: anArray){
                System.out.print(item + ",");
            }
            System.out.println("");
        }
    }
}