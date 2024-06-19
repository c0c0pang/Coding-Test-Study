import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		String s1 = br.readLine();
		StringTokenizer tokens = new StringTokenizer(s1," ");
		int N = Integer.parseInt(tokens.nextToken());
		int M = Integer.parseInt(tokens.nextToken());
		int R = Integer.parseInt(tokens.nextToken());
		int range = Math.min(N, M)/2;
		int[][] arr = new int[N][M];
		for(int i =0;i<N;i++) {
			int cnt =0;
			String s2 = br.readLine();
			StringTokenizer nums = new StringTokenizer(s2," ");
			while(nums.hasMoreTokens()) {
				arr[i][cnt] = Integer.parseInt(nums.nextToken());
				cnt++;
			}
		}
		for(int i =0;i<R;i++) {
			for(int j =0;j<range;j++) {
				int temp = arr[j][j];
				for(int z = j;z<M-j-1;z++) {
					arr[j][z] = arr[j][z+1];
				}
				for(int z=j;z<N-j-1;z++) {
					arr[z][M-j-1] = arr[z+1][M-j-1];
				}
				for(int z=M-j-1;z>0+j;z--) {
					arr[N-j-1][z] = arr[N-j-1][z-1];
				}
				for(int z=N-j-1;z>0+j;z--) {
					arr[z][j] = arr[z-1][j];
				}
				arr[j+1][j] = temp;
			
		}
		}
		for(int i =0;i<N;i++) {
			for(int j=0;j<M;j++) {
				System.out.print(arr[i][j]+" ");
			}
			System.out.println();
		}
	}
}
