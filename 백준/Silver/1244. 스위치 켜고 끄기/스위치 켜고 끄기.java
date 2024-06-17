import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.List;
import java.util.StringTokenizer;

public class Main {
	public static void main(String[] args) throws IOException{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int n = Integer.parseInt(br.readLine()); 
		String array = br.readLine();
		StringTokenizer tokens = new StringTokenizer(array," ");
		List<Boolean> swit = new ArrayList<Boolean>();
		while(tokens.hasMoreTokens()) {
			if(tokens.nextToken().equals("1")) {
				swit.add(true);
			}
			else {

				swit.add(false);	
			}
		}
		int s = Integer.parseInt(br.readLine());
		for(int i=0;i<s;i++) {
			String w = br.readLine();
			StringTokenizer box = new StringTokenizer(w," ");	
			int j = Integer.parseInt(box.nextToken());
			int t = Integer.parseInt(box.nextToken());
			if(j==1) {
				for(int z=t;z<=swit.size();z+=t) {
					swit.set(z-1, !swit.get(z-1));
				}
			}
			else {
					t -=1;
					int l = t-1;
					int r = t+1;
					swit.set(t, !swit.get(t));
					while(l>-1 && r<swit.size()) {
						if(swit.get(l)==swit.get(r)) {
							swit.set(l, !swit.get(l));
							swit.set(r, !swit.get(r));
						}
						else {
							break;
						}
						l-=1;
						r+=1;
					}
				
			}
		}
		for(int i =1;i<=swit.size();i++) {
	
			if(swit.get(i-1)) {
				System.out.print(1+" ");
			}
			else {
				System.out.printf(0+" ");
			}		
			if(i%20==0) {
				System.out.println();
			}
		}
	}
}
