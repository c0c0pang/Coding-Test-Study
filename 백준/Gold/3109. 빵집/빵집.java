import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
	static int N;
	static int M;
	static String[][] bread; 
	static int[][] ans;
	static boolean[][] visited;
	static int answer=0;
	static int[] dx= {-1,0,1};
	static int[] dy= {1,1,1};
	static boolean check;
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		String s1 = br.readLine();
		StringTokenizer tokens = new StringTokenizer(s1," ");
		N = Integer.parseInt(tokens.nextToken());
		M = Integer.parseInt(tokens.nextToken());
		bread = new String[N][M];
		ans = new int[N][M];
		visited = new boolean[N][M];
		for(int i =0;i<N;i++) {
			int cnt=0;
			String s2 = br.readLine();
			StringTokenizer token = new StringTokenizer(s2,"");
			while(token.hasMoreTokens()) {
				bread[i] = token.nextToken().split("");
			}
		}
		for(int i =0;i<N;i++) {
			check = false;
			dfs(i,0);	
		}
		System.out.println(answer);
	}
	static void dfs(int col,int row) {
		if(row==M-1) {
			answer++;
			check = true;
			return;
		};
		for(int i =0;i<3;i++) {
			if(check) break;
			int nx = col + dx[i];
			int ny = row + dy[i];
			if(in_range(nx,ny)) {
				continue;
			}
			if(visited[nx][ny]) {
				continue;
			}
			if(bread[nx][ny].equals("x")) {
				continue;
			}
			visited[nx][ny] = true;
			dfs(nx,ny);
		}
	}
	static boolean in_range(int x,int y) {
		return x>=N || y>=M || x<0 || y<0;
	}
}
