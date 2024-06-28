import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.LinkedList;
import java.util.Queue;
import java.util.StringTokenizer;

class Main {
	static int N;
	static int M;
	static boolean[] visited;
	static String[][] array;
	static int[] dx= {-1,1,0,0},dy= {0,0,-1,1};
	static int answer =0;
	static char check;
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		String s1 = br.readLine();
		StringTokenizer tokens = new StringTokenizer(s1," ");
		N = Integer.parseInt(tokens.nextToken());
		M = Integer.parseInt(tokens.nextToken());
		array = new String[N][M];
		visited = new boolean[26];
		for(int i =0;i<N;i++) {
			String s2 = br.readLine();
			array[i] = s2.split("");
		}
		int v = array[0][0].charAt(0);
		visited[v-65] = true;
		dfs(0,0,1);
		System.out.println(answer);
	}
	static void dfs(int x,int y,int cnt) {
		answer = Math.max(answer, cnt);
		for(int i =0;i<4;i++) {
			int nx = x+dx[i];
			int ny = y+dy[i];
			if(in_range(nx,ny)) continue;
			int v = array[nx][ny].charAt(0);
			if(visited[v-65]) continue;
			visited[v-65] = true;
			dfs(nx,ny,cnt+1);
			visited[v-65] = false;
		}
	}
	static boolean in_range(int x,int y) {
		return x>=N || y>=M || x<0 || y<0;
	}
}
