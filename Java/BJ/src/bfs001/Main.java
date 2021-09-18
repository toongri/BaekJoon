package bfs001;

import java.util.LinkedList;
import java.util.Queue;
import java.util.Scanner;

public class Main {

	public static int[][] arrGrp;
	public static int[][] arrVst;
	public static int[][] arrVec = {{1, 0, -1, 0}, {0, 1, 0, -1}};
	public static final int vecLen = arrVec[0].length;
	public static int arrX,arrY;
	
	public static void main(String[] args) {
		
		Scanner sc = new Scanner(System.in);
		String str;
		
		arrY = sc.nextInt();
		arrX = sc.nextInt();
        sc.nextLine(); // 버퍼 지우기
		arrGrp = new int[arrY][arrX];
		arrVst = new int[arrY][arrX];
		
		for(int i = 0; i < arrY; i++) {
			str = sc.nextLine();
			for(int j = 0; j < arrX; j++)
				arrGrp[i][j] = str.charAt(j) - '0';
		}
		
		System.out.println(bfs(0,0));
		
		sc.close();
	}

	public static int bfs(int startX, int startY) {
		Node newNod;
		int px, py, x, y;
		arrVst[startY][startX]++;
		Queue<Node> queBfs = new LinkedList<>();
		queBfs.offer(new Node(startX, startY));
		
		while(!queBfs.isEmpty()) {
			newNod = queBfs.poll();
			
			x = newNod.getX();
			y = newNod.getY();
			
			for(int i = 0; i < vecLen; i++) {
				px = x + arrVec[0][i];
				py = y + arrVec[1][i];
				
				if (px >= 0 && px < arrX && py >= 0 && py < arrY) {
					
					if(arrVst[py][px] == 0 && arrGrp[py][px] == 1) {
						queBfs.offer(new Node(px, py));
						arrVst[py][px] = arrVst[y][x] + 1;
					}
				}
			}
		}
		
		return arrVst[arrY - 1][arrX - 1];
		
	}
}

class Node{
	int x, y;
	
	Node(int x, int y){
		this.x = x;
		this.y = y;
	}
	
	int getX() {
		return this.x;
	}
	
	int getY() {
		return this.y;
	}
}
