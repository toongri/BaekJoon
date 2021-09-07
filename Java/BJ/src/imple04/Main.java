package imple04;

import java.util.Scanner;

public class Main {

	final static int arrDir[][] = {{-1, 0, 1, 0}, {0, 1, 0, -1}};
	static int usrDir;
	static int cntTrn;
	
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
	
		int[] arr = new int[5];
		
		for(int i = 0; i< arr.length; i++)
			arr[i] = sc.nextInt();
		
		int y = arr[0];
		int x = arr[1];
		int usrY = arr[2];
		int usrX = arr[3];
		usrDir = arr[4];
		cntTrn = 0;
		int cntLod = 1;
		int py, px;
		
		int[][] arrSea = new int[y][x];
		int[][] arrChk = new int[y][x];
		
		arrChk[usrY][usrX] = 1;
		
		for(int i = 0; i < y; i++)
			for(int j = 0; j< x; j++)
				arrSea[i][j] = sc.nextInt();
		
		while(true) {
			turnDirect();

			py = usrY + arrDir[0][usrDir];
			px = usrX + arrDir[1][usrDir];
			
			if (arrChk[py][px] == 0 && arrSea[py][px] == 0) {
				usrY = py;
				usrX = px;
				arrChk[py][px] = 1;
				cntLod++;
				cntTrn = 0;
			}
			else {
				if(cntTrn>3) {
					py = usrY - arrDir[0][usrDir];
					px = usrX - arrDir[1][usrDir];
					
					if(arrSea[py][px] == 1)
						break;
					else {
						usrX = px;
						usrY = py;
						cntTrn = 0;
					}
				}
			}
		}
			
		System.out.println(cntLod);
	}
	
	public static void turnDirect() {
		usrDir = (usrDir == 0) ? 3 : usrDir - 1;
		cntTrn++;
	}

}
