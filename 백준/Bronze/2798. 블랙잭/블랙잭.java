import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.StringTokenizer;

public class Main {
	static int N;
	static int M;
	static int[]ans;
	static boolean[] visited;
	static int answer = -Integer.MAX_VALUE;
	static ArrayList<Integer> arr;
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		String s1 = br.readLine();
		StringTokenizer tokens_s1 = new StringTokenizer(s1," ");
		N = Integer.parseInt(tokens_s1.nextToken());
		M = Integer.parseInt(tokens_s1.nextToken());
		visited = new boolean[N];
		ans = new int[N];
		String s2 = br.readLine();
		StringTokenizer tokens_s2 = new StringTokenizer(s2," ");
		arr = new ArrayList<Integer>();
		while(tokens_s2.hasMoreTokens()) {
			arr.add(Integer.parseInt(tokens_s2.nextToken()));
		}
		dfs(0);
		System.out.println(answer);
	}
	static void dfs(int cnt) {
		if(cnt==3) {
			sum();
			return;
		}
		for(int i =0;i<N;i++) {
			if(!visited[i]) {
				ans[cnt] = arr.get(i);
				visited[i] = true;
				dfs(cnt+1);
				visited[i] = false;
			}
		}
	}
	static void sum() {
		int sum=0;
		for(int i = 0;i<3;i++) {
			sum+=ans[i];
		}
		if(sum<=M) {
			answer = Math.max(sum, answer);
		}
	}
}
