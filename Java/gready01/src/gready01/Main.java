package gready01;

import java.util.Arrays;
import java.util.Scanner;

public class Main {

	public static void main(String[] args) {

		Scanner sc = new Scanner(System.in);

		String[] str = sc.nextLine().split(" ");

		int arrLen = Integer.parseInt(str[0]);

		int ansLen = Integer.parseInt(str[1]);

		int anstop = Integer.parseInt(str[2]);

		int dddl;

		int ans = 0;

		int[] arr = new int[arrLen];

		for (int i = 0; i < arrLen; i++)
			arr[i] = sc.nextInt();

		Arrays.sort(arr);

		int maxKey = arr[arrLen - 1];
		int mscKey = arr[arrLen - 2];

		if (maxKey == mscKey) {
			ans = maxKey * ansLen;
		} else {
			dddl = ansLen / (anstop + 1);

			ans = maxKey * (anstop * dddl + ansLen % (anstop + 1)) + mscKey * dddl;
		}

		System.out.println(ans);

	}

}
