import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.HashMap;
import java.util.Map;
import java.util.StringTokenizer;

public class Main {
	static int[] minOccurs;
	public static void main(String[] args) throws IOException{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		String array = br.readLine();
		StringTokenizer tokens = new StringTokenizer(array," ");
		int n = Integer.parseInt(tokens.nextToken());
		int m = Integer.parseInt(tokens.nextToken());
		int answer = 0;
		String dna = br.readLine();
		String p = br.readLine();
		StringTokenizer ps = new StringTokenizer(p," ");
		minOccurs = new int[4];
		for(int i=0;i<minOccurs.length;i++) {
			minOccurs[i] = Integer.parseInt(ps.nextToken()); 
		}
		Map<Character,Integer> map  = new HashMap<Character, Integer>();
		map.put('A', 0);
		map.put('C', 0);
		map.put('G', 0);
		map.put('T', 0);
		for(int i =0;i<m;i++) {
			map.put(dna.charAt(i), map.get(dna.charAt(i))+1);
		}
		if(check(map)) answer++;
		check(map);
		for(int i=1;i+m<=n;i++) {
			char delKey = dna.charAt(i-1);
			char addKey = dna.charAt(i-1+m);
			
			map.put(delKey,map.get(delKey)-1);
			map.put(addKey,map.get(addKey)+1);
			if(check(map)) answer++;
		}
		System.out.println(answer);
	}
	static boolean check(Map<Character,Integer> map) {
		for(Character key:map.keySet()) {
			if(key =='A') {
				if(map.get(key)<minOccurs[0]) return false;
			}
			else if(key =='C') {
				if(map.get(key)<minOccurs[1]) return false;
			}
			
			else if(key =='G') {
				if(map.get(key)<minOccurs[2]) return false;
			}
			else if(key =='T') {
				if(map.get(key)<minOccurs[3]) return false;
			}
		}
		return true;
	}
}
