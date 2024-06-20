import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
	static boolean[] visited;
	static int n;
	static int m;
	static int[] ans;
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		String str = br.readLine();
		StringTokenizer tokens = new StringTokenizer(str," ");
		n = Integer.parseInt(tokens.nextToken());
		m = Integer.parseInt(tokens.nextToken());
		visited = new boolean[n];
		ans = new int[m];
		nAndm(0);
	}
	static void nAndm(int cnt) {
		if(m==cnt) {
			print();
			return;
		}
		for(int i =0;i<n;i++) {
			if(!visited[i]) {
				ans[cnt] = i+1;
				visited[i] = true;
				nAndm(cnt+1);
				visited[i] = false;
			}
		}
	}
	static void print() {
		for(int i =0;i<m;i++) {
			System.out.print(ans[i]+" ");
		}
		System.out.println();
	}
}
