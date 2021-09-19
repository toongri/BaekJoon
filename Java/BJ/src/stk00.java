import java.util.Scanner;
import java.util.Stack;

public class stk00 {

	public static void main(String[] args) {
		//postorder(5);
		fuckorder(5);
	}
	
	public static void fuckorder(int j) {
		if(j>0) {
			fuckorder(j-1);
			fuckorder(j-2);
			System.out.println(j);
		}
	}
	
	public static void postorder (int j) {
		Stack<Integer> stk = new Stack<>();
		Stack<Integer> stk2 = new Stack<>();
		int n = j;
		int dfd;
		
		stk.push(n);
		
		while(!stk.empty()) {
			dfd = stk.pop();
			stk2.push(dfd);
			
			if(dfd > 2) {
				stk.push(dfd - 1);
				stk.push(dfd - 2);
			}
			else if (dfd > 1) {
				stk.push(dfd - 1);
			}
			
		}
		while(!stk2.empty())
			System.out.println(stk2.pop());
		
	}

}
