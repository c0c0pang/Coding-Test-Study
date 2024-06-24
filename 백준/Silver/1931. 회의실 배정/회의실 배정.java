import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {
	static int N;
	static int[][] array;
	static int answer = 0;
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		String s1 = br.readLine();
		N = Integer.parseInt(s1);
		array = new int[N][1];
		for(int i =0;i<N;i++) {
			String s2 = br.readLine();
			StringTokenizer tokens = new StringTokenizer(s2," ");
			int s = Integer.parseInt(tokens.nextToken());
			int e = Integer.parseInt(tokens.nextToken());
			int[] r = {s,e};
			array[i]= r;
		}
		Arrays.sort(array,(a,b)->{
			if(a[1]==b[1]) {
				return a[0] - b[0];
 			}
			return a[1] - b[1];
		});
		int cy=0;
		for(int i =0;i<array.length;i++) {
			if(i==0) {
				cy = array[i][1];
				answer++;
				continue;
			}
			if(array[i][0]==array[i][1]) {
				answer++;
				continue;
			}
			if(cy<=array[i][0]) {
				cy = array[i][1];
				answer++;
				continue;
			}
		}
		System.out.println(answer);
	}
}
