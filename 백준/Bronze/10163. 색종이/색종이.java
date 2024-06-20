import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int H=1001,W=1001;
		int[][] arr = new int[H][W];
		String s1 = br.readLine();
		int N = Integer.parseInt(s1);
		for(int i =1;i<=N;i++) {
			String s2 = br.readLine();
			StringTokenizer tokens = new StringTokenizer(s2," ");
			int y = Integer.parseInt(tokens.nextToken());
			int x = Integer.parseInt(tokens.nextToken());
			int w = Integer.parseInt(tokens.nextToken());
			int h = Integer.parseInt(tokens.nextToken());
			for(int j=x;j<h+x;j++) {
				for(int z=y;z<w+y;z++) {
					arr[j][z] = i;
				}
			}
		}
		for(int i=1;i<=N;i++) {
			int answer = 0;
			for(int j=0;j<H;j++) {
				for(int z=0;z<W;z++) {
					if(arr[j][z]==i) {
						answer++;
					}
				}	
			}
			System.out.println(answer);
		}
		
	}
}
