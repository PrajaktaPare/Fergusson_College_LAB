
public class CanPlaceFlower {

    public boolean flower(int[] flowerbed, int n) {
        int count = 0;
        for (int i = 0; i < flowerbed.length; i++) {
            if (flowerbed[i] == 0 && (i == 0 || flowerbed[i - 1] == 0) && (i == flowerbed.length - 1 || flowerbed[i + 1] == 0)) {
                flowerbed[i] = 1;
                count++;
                i++;
            }
            if (count >= n) {
                return true;
            }

        }

        return count >= n;
    }

    public static void main(String[] args)
    {
        CanPlaceFlower pf = new CanPlaceFlower();
        int[] flowerbed ={1,0,0,0,1};
        int n=2;
        System.out.println(pf.flower(flowerbed, n));

    }

}