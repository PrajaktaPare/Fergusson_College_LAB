
public class MergeStringsAlternately
{
    public String mergeAlternately(String word1,String word2)
    {
        StringBuilder mergedString = new StringBuilder();
        int i=0,j=0;
        while(i < word1.length() && j < word2.length())
        {
            mergedString.append(word1.charAt(i++));
            mergedString.append(word2.charAt(j++));

        }
        while(i < word1.length())
        {
            mergedString.append(word1.charAt(i++));
        }
        while(j < word2.length())
        {
            mergedString.append(word2.charAt(j++));
        }
        return mergedString.toString();
    }
    public static void main(String[] args)
    {
        MergeStringsAlternately m = new MergeStringsAlternately();
        String r1 = m.mergeAlternately("abc","pqr");
        System.out.println("Merged result for abc and pqr : "+r1);
    }
}