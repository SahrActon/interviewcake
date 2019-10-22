import java.util.HashSet;
import java.util.Set;

public class hasPalindromePermutation {

    public static boolean hasPalindromePermutationFunction(String theString) {
        // Track characters we have seen an odd number of times

        Set<Character> unpairedCharacters = new HashSet<>();

        for (char c : theString.toCharArray()) {
            if (unpairedCharacters.contains(c)) {
                unpairedCharacters.remove(c);
            } else {
                unpairedCharacters.add(c);
            }
        }
        // the String had a palindrome permutation if it has a one or zero characters without a pair

        return unpairedCharacters.size() <= 1;
    }

    // Run the function by uncommenting the lines below
 /*   public static void main(String[] args) {
        System.out.println("Hello I work");
        System.out.println("Word is: tom - " + hasPalindromePermutationFunction("tom"));
        System.out.println("Word is: mom - " + hasPalindromePermutationFunction("mom"));
        System.out.println("Word is: civic - " + hasPalindromePermutationFunction("civic"));
        System.out.println("Word is: jacob - " + hasPalindromePermutationFunction("jacob"));
        System.out.println("Word is: mom - " + hasPalindromePermutationFunction("mom"));

    }*/

 /* Expected output

Hello I work

Word is: tom - false
Word is: mom - true
Word is: civic - true
Word is: jacob - false
Word is: mom - true

 * */
}
