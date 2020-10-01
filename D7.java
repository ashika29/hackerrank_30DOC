// Question link: https://www.hackerrank.com/challenges/30-arrays/problem
// Code section:
import java.io.*;
import java.math.*;
import java.security.*;
import java.text.*;
import java.util.*;
import java.util.concurrent.*;
import java.util.regex.*;

public class D7 {



    private static final Scanner scanner = new Scanner(System.in);
    public static void reverseArray(int[] arr, int n){
        for(int i=n-1;i > -1; --i){
            System.out.printf("%d ",arr[i]);
        }
    }
    public static void main(String[] args) {
        int n = scanner.nextInt();
        scanner.skip("(\r\n|[\n\r\u2028\u2029\u0085])?");

        int[] arr = new int[n];

        String[] arrItems = scanner.nextLine().split(" ");
        scanner.skip("(\r\n|[\n\r\u2028\u2029\u0085])?");

        for (int i = 0; i < n; i++) {
            int arrItem = Integer.parseInt(arrItems[i]);
            arr[i] = arrItem;
        }

        reverseArray(arr, n);
        scanner.close();
    }
}
