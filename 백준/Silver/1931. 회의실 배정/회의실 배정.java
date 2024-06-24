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
			//끝 시간이 같으면 처음 시간이 빠른 순으로 정렬 
			if(a[1]==b[1]) {
				return a[0] - b[0];
 			}
			//끝 시간을 기준으로 오름차순 정렬
			return a[1] - b[1];
		});
		//이전의 위치를 저장하는 변수.
		int prev=0;
		for(int i =0;i<array.length;i++) {
			//초기화 작업
			if(i==0) {
				prev= array[i][1];
				answer++;
				continue;
			}
			//회의시간의 시작과 끝이 같은 경우는 반영이 안되기에 카운팅만 실시.
			if(array[i][0]==array[i][1]) {
				answer++;
				continue;
			}
			//이전 위치와 현재 위치의 시작점을 비교함.
			if(prev<=array[i][0]) {
				prev = array[i][1];
				answer++;
				continue;
			}
		}
		System.out.println(answer);
	}
}
