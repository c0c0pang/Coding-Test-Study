import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {
	static int N;
	static int[]dp;
	static int[]arr;
	public static void main(String[] arge) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		String s1  = br.readLine();
		N = Integer.parseInt(s1);
		int sum = 0;
		for(int i =1;i<=N;i++) {
			sum+=i;
		}
		dp = new int[sum];
		arr = new int[sum];
		int cnt = 0;
		for(int i =0;i<N;i++) {
			String s2 = br.readLine();
			StringTokenizer tokens = new StringTokenizer(s2," ");
			while(tokens.hasMoreTokens()) {
				int v = Integer.parseInt(tokens.nextToken());
				arr[cnt] = v;
				dp[cnt] = v;
				cnt++;
			}
		}
		int prev = 0;
		int num = 1;
		int plus = 0;
		int x = 0;
		while(num<sum) {
			for(int i=num;i<num+plus+1;i++) {
				dp[i] =Math.max(dp[i],arr[i] + dp[prev]);
				dp[i+1] =Math.max(dp[i+1],arr[i+1] + dp[prev]);
				prev++;
				x = i+1;
			}
			num=x+1;
			plus++;
		}
		Arrays.sort(dp);
		System.out.println(dp[dp.length-1]);
		
	}
}
