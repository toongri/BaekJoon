package imple03;

import java.util.Scanner;

public class Main {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		int[][] arr = {{1, 1, -1, -1, 2, 2, -2, -2},
				{2, -2, 2, -2, 1, -1, 1, -1}};
		
		String ans = sc.next();
		
		int a = ans.charAt(0)-97;
		int b= Character.getNumericValue(ans.charAt(1)) - 1;
		int arrLen = arr[1].length;
		int pa, pb, cnt = 0;
		
		for (int i =0; i< arrLen; i++) {
			pa = a+arr[0][i];
			pb = b+arr[1][i];
			
			if(pa<8 && pa>=0 && pb<8 && pb>=0)
				cnt++;
			
		}
		
		System.out.println(cnt);
	}

}
