// Question link:
// https://www.hackerrank.com/challenges/30-operators/problem/

import java.io.*;
import java.math.*;
import java.util.*;

public class D2 {

    // Complete the solve function below.
    static void solve(double meal_cost, int tip_percent, int tax_percent) {
        double total_cost = 0.0, tax=0.0,tip=0.0;
        tax = meal_cost*tax_percent/100;
        tip = meal_cost*tip_percent/100;
        total_cost = meal_cost + tax + tip;
        System.out.format("%d\n",Math.round(total_cost));
    }

    private static final Scanner scanner = new Scanner(System.in);

    public static void main(String[] args) {
        double meal_cost = scanner.nextDouble();
        scanner.skip("(\r\n|[\n\r\u2028\u2029\u0085])?");

        int tip_percent = scanner.nextInt();
        scanner.skip("(\r\n|[\n\r\u2028\u2029\u0085])?");

        int tax_percent = scanner.nextInt();
        scanner.skip("(\r\n|[\n\r\u2028\u2029\u0085])?");

        solve(meal_cost, tip_percent, tax_percent);

        scanner.close();
    }
}
