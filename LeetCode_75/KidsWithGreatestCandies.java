
import java.util.ArrayList;
import java.util.List;
public class KidsWithGreatestCandies {
    public static List<Boolean> kidswithcandies(int[] candies,int extraCandies)
    {
        List<Boolean> result = new ArrayList<>();
        int maxCandies= 0;
        for(int candy: candies)
        {
            if(candy > maxCandies)
            {
                maxCandies = candy;

            }
        }
        for(int candy : candies)
        {
            result.add(candy + extraCandies >= maxCandies);
        }
           return result ;
    }
    public static void main(String[] args)
    {
        int[] candies ={2,3,5,1,3};
        int extraCandies= 3;
        List<Boolean> result=kidswithcandies(candies, extraCandies);
        System.out.println(result);
    }
}
