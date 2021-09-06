package gready02;

import java.util.Scanner;
import java.util.ArrayList;
import java.util.Collections;

public class Main {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		int x = sc.nextInt();
		int y = sc.nextInt();
		int min;
		int stm = 0;
		
		
		ArrayList<ArrayList<Integer>> list = new ArrayList<ArrayList<Integer>>();
		
		ArrayList<Integer> ans = new ArrayList<Integer>();
		
		for(int i = 0; i < y; i++) {
			list.add(new ArrayList<Integer>());
			min = 10001;
			for(int j = 0; j < x; j++) {
				stm = sc.nextInt();
				
				list.get(i).add(stm);
				
				min = stm < min ? stm : min;
				
			}
			ans.add(min);
		}
		
		System.out.println(Collections.max(ans));
	}
}
