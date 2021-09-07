package imple02;

import java.util.Scanner;

public class Main {

	public static void main(String[] args) {
		
		Scanner sc = new Scanner(System.in);
		int[] arr = {sc.nextInt() + 1, 60, 60};
		int cnt = 0;
		
		for (int i = 0; i < arr[0]; i++) {
			for(int j = 0; j < arr[1]; j++ ) {
				for(int k = 0; k < arr[2]; k++) {
					if ((Integer.toString(i) + Integer.toString(j) + Integer.toString(k)).contains("3"))
						cnt++;
				}
			}
		}
		
		System.out.println(cnt);
		
	}

}
