package bfs00;

import java.util.*;

public class Main {

	
	public static ArrayList<ArrayList<Integer>> arrGrp = new ArrayList<ArrayList<Integer>>();
	public static boolean[] arrVst = new boolean[9];
	
	public static void main(String[] args) {
		insertToGraph();
		bfs(1);
	}
	
	public static void bfs(int v) {
		int j;
		Queue<Integer> queGrp = new LinkedList<>();
		queGrp.offer(v);
		arrVst[v] = true;
		
		while(!queGrp.isEmpty()){
			j = queGrp.poll();
			System.out.print(j + " ");
			
			for(int i:arrGrp.get(j)) {
				if( !arrVst[i]) {
					queGrp.offer(i);
					arrVst[i] = true;
				}
			}
		}
	}
	
	public static void insertToGraph() {
		for(int i = 0; i < arrVst.length; i++)
			arrGrp.add(new ArrayList<Integer>());
		
		arrGrp.get(1).add(2);
		arrGrp.get(1).add(3);
		arrGrp.get(1).add(8);

		arrGrp.get(2).add(1);
		arrGrp.get(2).add(7);

		arrGrp.get(3).add(1);
		arrGrp.get(3).add(4);
		arrGrp.get(3).add(5);

		arrGrp.get(4).add(3);
		arrGrp.get(4).add(5);

		arrGrp.get(5).add(3);
		arrGrp.get(5).add(4);

		arrGrp.get(6).add(7);

		arrGrp.get(7).add(2);
		arrGrp.get(7).add(6);
		arrGrp.get(7).add(8);

		arrGrp.get(8).add(1);
		arrGrp.get(8).add(7);
		
	}

}
