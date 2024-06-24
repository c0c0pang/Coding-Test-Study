import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.StringTokenizer;

public class Main {
	static int N;
	static int M;
	static int answer = Integer.MAX_VALUE;
	static int x = -Integer.MAX_VALUE;
	static int [][]array;
	static int[] dx = {-1,1,0,0},dy= {0,0,-1,1};
	static ArrayList<int[]> home;
	static ArrayList<int[]> target;
	static int[][] ans;
	static boolean[][] visited;
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		String s1 = br.readLine();
		StringTokenizer tokens = new StringTokenizer(s1," ");
		N = Integer.parseInt(tokens.nextToken());
		M = Integer.parseInt(tokens.nextToken());
		array = new int[N][N];
		for(int i =0;i<N;i++) {
			int cnt = 0;
			String s2 = br.readLine();
			StringTokenizer row = new StringTokenizer(s2," ");
			while(row.hasMoreTokens()) {
				array[i][cnt] = Integer.parseInt(row.nextToken());
				cnt++;
			}
		}
		home = new ArrayList<int[]>();
		target = new ArrayList<int[]>();
		ans = new int[M][1];
		for(int i =0;i<N;i++) {
			for(int j=0;j<N;j++) {
				int[] v = new int[]{i,j};
				if(array[i][j]==1) {
					home.add(v);
				}
				if(array[i][j]==2) {
					target.add(v);
				}
			}
		}
		visited = new boolean[target.size()][1];
		dfs(0,0);//조합으로 풀기 위해 start의 값을 지정
		System.out.println(answer);
		
	}
	static void dfs(int cnt,int start) {
		int result = Integer.MAX_VALUE;
		int sum = 0;
		if(cnt==M) {
			for(int i =0;i<home.size();i++) {
				result = Integer.MAX_VALUE;
				for(int j =0;j<ans.length;j++) {
					int q = Math.abs(home.get(i)[0]-ans[j][0])+Math.abs(home.get(i)[1]-ans[j][1]);
					result= Math.min(result,q);			
				}
				sum+=result;
			}
			answer = Math.min(sum, answer);
			return;
		}
		for(int i =start;i<target.size();i++) {
			if(!visited[i][0]) {
				visited[i][0] = true;
				ans[cnt] = target.get(i);
				dfs(cnt+1,i+1);
				visited[i][0] = false;
			}
		}
	}
}
 