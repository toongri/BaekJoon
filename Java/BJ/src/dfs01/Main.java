package dfs01;

import java.util.Scanner;

public class Main {
	static int[][] arrVst;
	static int[][] arrGrp;
	static int[][] arrMov = { { 1, 0, -1, 0 }, { 0, 1, 0, -1 } };
	static final int lenMov = 4;
	static int lenx;
	static int leny;
	static int cnt = 0;

	public static void main(String[] args) {

		Scanner sc = new Scanner(System.in);

		leny = sc.nextInt();
		lenx = sc.nextInt();
		sc.nextLine();

		arrGrp = new int[leny][lenx];
		arrVst = new int[leny][lenx];

		for (int i = 0; i < leny; i++) {
			String str = sc.nextLine();
			for (int j = 0; j < lenx; j++) {
				arrGrp[i][j] = str.charAt(j) - '0';
			}
		}

		for (int i = 0; i < leny; i++) {
			for (int j = 0; j < lenx; j++) {
				if (arrGrp[i][j] == 0 && arrVst[i][j] == 0) {
					cnt++;
					dfs(i, j);
				}

			}
		}

		System.out.println(cnt);
	}

	public static void dfs(int y, int x) {
		arrVst[y][x] = 1;
		int px;
		int py;

		for (int i = 0; i < lenMov; i++) {
			py = y + arrMov[0][i];
			px = x + arrMov[1][i];
			if (py >= 0 && py < leny && px >= 0 && px < lenx) {
				if (arrGrp[py][px] == 0 && arrVst[py][px] == 0) {
					dfs(py, px);
				}
			}

		}
	}

}
