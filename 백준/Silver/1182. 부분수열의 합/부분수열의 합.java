import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
	static int N;
	static int M;
	static int[] array;
	static int[] ans;
	static boolean[] visited;
	static int answer = 0;
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		String s1 = br.readLine();
		StringTokenizer tokens = new StringTokenizer(s1," ");
		N = Integer.parseInt(tokens.nextToken());
		M = Integer.parseInt(tokens.nextToken());
		String s2 = br.readLine();
		StringTokenizer nums = new StringTokenizer(s2," ");
		int cnt = 0;
		array = new int[N];
		ans = new int[N];
		visited = new boolean[N];
		while(nums.hasMoreTokens()) {
			array[cnt] = Integer.parseInt(nums.nextToken()); 
			cnt++;
		}
		for(int i =1;i<=N;i++) {
			dfs(0,0,i);	
		}
		System.out.println(answer);
		
	}
	static void dfs(int cnt,int start,int end) {
		if(end==cnt) {
			result();
			return;
		}
		for(int i =start;i<N;i++) {
			if(!visited[i]) {
				visited[i] = true;
				ans[cnt] = array[i];
				dfs(cnt+1,i,end);
				visited[i] = false;
			}
		}
	}
	static void result() {
		int sum=0;
		for(int i =0;i<N;i++) {
			sum+=ans[i];
		}
		if(sum==M) {
			answer++;
		}
	}
}
