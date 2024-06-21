import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {
	static int[] ans;
	static boolean[] visited;
	static ArrayList<Integer> arr;
	static int N=9;
	static int[] answer;
	static int SIZE = 7;
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		arr = new ArrayList<Integer>();
		for(int i=0;i<N;i++) {
			String s = br.readLine();
			arr.add(Integer.parseInt(s));
		}
		visited = new boolean[N];
		ans = new int[SIZE];
		dfs(0);
		print();
	}
	static void dfs(int cnt) {
		if(cnt==SIZE) {
			result();
			return;
		}
		for(int i=0;i<N;i++) {
			if(!visited[i]) {
				ans[cnt] = arr.get(i);
				visited[i] = true;
				dfs(cnt+1);
				visited[i] = false;
			}
		}
	}
	static void result() {
		int sum = 0;
		for(int i =0;i<SIZE;i++) {
			sum+=ans[i];
		}
		if(sum==100) answer = ans.clone();
	}
	static void print() {
		Arrays.sort(answer);
		for(int i =0;i<SIZE;i++) {
			System.out.println(answer[i]);
		}
	}
}
