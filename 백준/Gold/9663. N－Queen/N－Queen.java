import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
	static int N;
	static int[] ans;
	static int answer=0;
	static boolean check;
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		String s1 = br.readLine();
		N = Integer.parseInt(s1);
		ans = new int[N];
		dfs(0);
		System.out.println(answer);
	}
	static void dfs(int cnt) {
		if(cnt==N) {
			result();
			return;
		}
		for(int i=0;i<N;i++) {
			ans[cnt] = i;
			check = false;
			if(cnt>0) {
				for(int j =0;j<cnt;j++) {
					if(ans[j]==ans[cnt] || (Math.abs(ans[cnt]-ans[j]) == cnt-j)) {
						check = true;
						break;
					}
				}		
			}
			if(check) continue;
			dfs(cnt+1);
		}
	}
	static void result() {
		answer++;
	}
}
