import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.LinkedList;
import java.util.Queue;
import java.util.StringTokenizer;

public class Main {
	static int N;
	static int M;
	static int[][] arr;
	static Queue<int[]> queue = new LinkedList<int[]>();
	static boolean[][] v_visited;
	static int SIZE = 3;
	static int answer=-Integer.MAX_VALUE;
	static int[] dx = {-1,1,0,0},dy= {0,0,-1,1};
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		String s1 = br.readLine();
		StringTokenizer tokens = new StringTokenizer(s1," ");
		N = Integer.parseInt(tokens.nextToken());
		M = Integer.parseInt(tokens.nextToken());
		arr = new int[N][M];
		v_visited = new boolean[N][M];
		for(int i = 0;i<N;i++) {
			int cnt = 0;
			String s2 = br.readLine();
			StringTokenizer row = new StringTokenizer(s2," ");
			while(row.hasMoreTokens()) {
				arr[i][cnt] = Integer.parseInt(row.nextToken());
				cnt++;
			}
		}
		dfs(0);
		System.out.println(answer);
	}
	static void dfs(int cnt) {
		if(cnt == SIZE) {
			bfs();
			return;
		}
		for(int i = 0 ;i<N;i++) {
			for(int j =0;j<M;j++) {
				if(v_visited[i][j]) continue;
				if(arr[i][j]!=0) continue;
				arr[i][j] = 1;
				v_visited[i][j] = true;
				dfs(cnt+1);
				arr[i][j] = 0;
				v_visited[i][j] = false;
			}
		}
	}
	static void bfs() {
		int[][] copy = new int[N][M];
		for(int i =0;i<N;i++) {
			copy[i] = arr[i].clone();
		}
		boolean[][] visited = new boolean[N][M];
		for(int i =0;i<N;i++) {
			for(int j =0;j<M;j++) {
				if(copy[i][j]==2) {
					int[] start = {i,j};
					queue.offer(start);
					visited[i][j] = true;
					while(!queue.isEmpty()) {
						int[] v =queue.poll();
						for(int z =0;z<4;z++) {
							int nx = v[0] + dx[z];
							int ny = v[1] + dy[z];
							if(in_range(nx,ny)) continue;
							if(visited[nx][ny]) continue;
							if(copy[nx][ny]==0) {
								copy[nx][ny] = 3;
								visited[nx][ny] = true;
								int[] end = {nx,ny};
								queue.offer(end);
							}
						}
					}
				}
			}
		}
		counting(copy);
	}
	static boolean in_range(int x,int y) {
		return x>=N || y>=M || x<0 || y<0;
	}
	static void counting(int[][] copy) {
		int cnt = 0;
		for(int i =0;i<N;i++) {
			for(int j =0;j<M;j++) {
				if(copy[i][j]==0) {
					cnt++;
				}
			}
		}
		answer = Math.max(cnt, answer);
	}
}
