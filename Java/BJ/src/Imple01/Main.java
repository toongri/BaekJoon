package Imple01;

import java.util.Arrays;
import java.util.Scanner;

public class Main {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		int n = sc.nextInt();
		
		String[] arr = {"D", "L", "R", "U"};
		int[][] arr2 = {{1, 0, 0, -1}, {0, -1, 1, 0}};
		sc.nextLine();
		
		String[] arrStr = sc.nextLine().split(" ");
		
		int idx, fx, fy;
		
		int[] xy = {1,1};
		
		for(String str : arrStr) {
			idx = Arrays.binarySearch(arr, str);
			fy = xy[0] + arr2[0][idx];
			fx = xy[1] + arr2[1][idx];
			
			if (!(fx < 1 || fx > n || fy < 1 || fy > n )) {
				xy[0] = fy;
				xy[1] = fx;
			}
		}
		
		System.out.println(xy[0] + " " + xy[]);
	}

}
