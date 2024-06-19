
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.StringTokenizer;

public class Main {
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		String s1 = br.readLine();
		StringTokenizer tokens = new StringTokenizer(s1," ");
		int n = Integer.parseInt(tokens.nextToken()); 
		int m = Integer.parseInt(tokens.nextToken()); 
		ArrayList<Integer> box = new ArrayList<Integer>();
		String s2 = br.readLine();
		StringTokenizer arr = new StringTokenizer(s2," ");
		int []plus = new int[n+1];
		for(int i =0;i<plus.length;i++) {
			plus[i]=0;
		}
		while(arr.hasMoreTokens()) {
			box.add(Integer.parseInt(arr.nextToken()));
		}
		for(int i =1;i<=box.size();i++) {
			plus[i] = plus[i-1]+box.get(i-1);
		}
		for(int z = 0;z<m;z++) {
			String s3 = br.readLine();
			StringTokenizer range = new StringTokenizer(s3," ");
			int i = Integer.parseInt(range.nextToken());
			int j = Integer.parseInt(range.nextToken());
			System.out.println(plus[j]-plus[i-1]);
			
		}
	}
}
