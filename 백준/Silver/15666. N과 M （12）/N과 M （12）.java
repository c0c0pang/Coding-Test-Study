import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Comparator;
import java.util.Iterator;
import java.util.List;
import java.util.Set;
import java.util.StringTokenizer;
import java.util.TreeSet;
import java.util.stream.Collector;
import java.util.stream.Collectors;

public class Main {
	static boolean[] visited;
	static int n;
	static int m;
	static ArrayList<Integer> arr;
	static Set<List<Integer>> set = new TreeSet<>(new Comparator<List<Integer>>() {

		@Override
		public int compare(List<Integer> o1, List<Integer> o2) {
            for (int i = 0; i <m; i++) {
                int comparison = Integer.compare(o1.get(i), o2.get(i));
                if (comparison != 0) {
                    return comparison;
                }
            }
			return 0;
		}
		
	});
	static int[] ans;
	static StringBuilder sb = new StringBuilder();
	static Iterator<List<Integer>> it;
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		String str = br.readLine();
		StringTokenizer tokens = new StringTokenizer(str," ");
		n = Integer.parseInt(tokens.nextToken());
		m = Integer.parseInt(tokens.nextToken());
		visited = new boolean[n];
		String s1 = br.readLine();
		StringTokenizer v = new StringTokenizer(s1," ");
		arr = new ArrayList<Integer>();
		while(v.hasMoreTokens()) {
			int num = Integer.parseInt(v.nextToken());
			arr.add(num);
		}
		arr.sort(null);
		ans = new int[m];
		nAndm(0,0);
		it = set.iterator();
		while(it.hasNext()) {
			List<Integer> s = it.next();
			for(int i =0;i<m;i++) {
				sb.append(s.get(i)).append(' ');
			}
			sb.append('\n');
		}
		System.out.println(sb);
	}
	static void nAndm(int cnt,int start) {
		if(m==cnt) {
			set();
			return;
		}
		for(int i =start;i<n;i++) {
			if(visited[i]) continue;
			ans[cnt] = arr.get(i);
			nAndm(cnt+1,i);
		}
	}
	static void set() {
		int[] s = ans.clone();
		set.add(convertArrayToList(s));

	}
    static List<Integer> convertArrayToList(int[] array) {
        return Arrays.stream(array).boxed().collect(Collectors.toList());
    }

}
