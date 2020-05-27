package Big_O;

public class Big_O {

    public static int[] my_list_of_items = new int[]{1, 2, 3, 4, 5, 6, 7, 8};
    // Methods

    /**
     * This function runs in O(1) time (or "constant time") relative to its input.
     * The input list could be 1 item or 1,000 items, but this function would still just require one "step."
     *
     * @param items
     */
    public static void print_first_item(int[] items) {
        System.out.println(items[0]);
    }

    /***
     * This function runs in O(n) time (or "linear time"), where nn is the number of items in the list.
     * If the list has 10 items, we have to print 10 times. If it has 1,000 items, we have to print 1,000 times.
     * @param items
     */
    public static void print_all_items(int[] items) {
        for (int item : items) {
            System.out.println(item);
        }
    }

    /***
     * Here we're nesting two loops. If our list has nn items, our outer loop runs nn times
     * and our inner loop runs n times for each iteration of the outer loop,
     * giving us n^2n total prints. Thus this function runs in O(n^2) time (or "quadratic time").
     * If the list has 10 items, we have to print 100 times. If it has 1,000 items, we have to print 1,000,000 times.
     * @param items
     */
    public static void print_all_possible_items(int[] items) {
        for (int firstItem : items) {
            for (int secondItem : items) {
                System.out.println(firstItem + ", " + secondItem);
            }
        }
    }

    public static void main(String[] args) {
        print_first_item(my_list_of_items);
        System.out.println("-----");
        print_all_items(my_list_of_items);
        System.out.println("-----");
        print_all_possible_items(my_list_of_items);
    }
}
