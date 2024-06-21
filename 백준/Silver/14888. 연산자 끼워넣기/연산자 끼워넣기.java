import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.StringTokenizer;

public class Main {
	static int n1;
	static int SIZE;
	static int[] A_arr;
	static int[] S_arr;
	static boolean[] visited;
	static char[] ans;
	static ArrayList<Character> sign;
	static ArrayList<Integer> result;
	static int max = -Integer.MAX_VALUE;
	static int min = Integer.MAX_VALUE;
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int cnt=0;
		n1 = Integer.parseInt( br.readLine());
		String s1 = br.readLine();
		String s2 = br.readLine();
		StringTokenizer A = new StringTokenizer(s1," ");
		StringTokenizer S = new StringTokenizer(s2," ");
		A_arr = new int[n1];	
		S_arr = new int[4];
		sign = new ArrayList<Character>();
		result = new ArrayList<Integer>();
		while(A.hasMoreTokens()) {
			A_arr[cnt] = Integer.parseInt(A.nextToken());
			cnt++;
		}
		cnt = 0;
		while(S.hasMoreTokens()) {
			S_arr[cnt] = Integer.parseInt(S.nextToken());
			cnt++;
		}
		for(int i=0;i<4;i++) {
			if(i==0) {
				for(int j =0;j<S_arr[i];j++) {
					sign.add('+');
				}
			}
			if(i==1) {
				for(int j =0;j<S_arr[i];j++) {
					sign.add('-');
				}
			}
			if(i==2) {
				for(int j =0;j<S_arr[i];j++) {
					sign.add('*');
				}
			}
			if(i==3) {
				for(int j =0;j<S_arr[i];j++) {
					sign.add('/');
				}
			}
		}
		SIZE = sign.size();
		ans = new char[SIZE];
		visited = new boolean[SIZE];
		dfs(0);
		System.out.printf("%d\n%d",max,min);
	}
	static void dfs(int n) {
		if(n==SIZE) {
			print();
			return;
		}
		for(int i=0;i<SIZE;i++) {
			if(!visited[i]) {
				ans[n] = sign.get(i);
				visited[i] = true;
				dfs(n+1);
				visited[i] = false;
			}
		}
	}
	static void print() {
		int sum = A_arr[0];
		for(int i =1;i<n1;i++) {
				if(ans[i-1]=='+') {
					sum = sum + A_arr[i];
				}
				if(ans[i-1]=='-') {
					sum = sum - A_arr[i];
				}
				if(ans[i-1]=='*') {
					sum = sum * A_arr[i];
				}
				if(ans[i-1]=='/') {
					sum = sum / A_arr[i];
				}
			
		}
		max = Math.max(sum, max);
		min = Math.min(sum, min);
	}
}
