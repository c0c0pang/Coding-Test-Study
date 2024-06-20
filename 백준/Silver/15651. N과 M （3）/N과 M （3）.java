import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
	static boolean[] visited;
	static int n;
	static int m;
	static int[] ans;
	public static StringBuilder sb = new StringBuilder();
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		String str = br.readLine();
		StringTokenizer tokens = new StringTokenizer(str," ");
		n = Integer.parseInt(tokens.nextToken());
		m = Integer.parseInt(tokens.nextToken());
		ans = new int[m];
		nAndm(0);
		System.out.println(sb);
	}
	static void nAndm(int cnt) {
		if(m==cnt) {
			print();
			return;
		}
		for(int i =0;i<n;i++) {
			ans[cnt] = i+1;
			nAndm(cnt+1);
		}
	}
	static void print() {
		for(int i =0;i<m;i++) {
			sb.append(ans[i]).append(' ');
		}
		sb.append('\n');
	}
}
