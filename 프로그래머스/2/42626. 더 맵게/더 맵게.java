import java.util.PriorityQueue;
import java.util.Arrays;
class Solution {
    static PriorityQueue<Integer> queue = new PriorityQueue<Integer>();
    public int solution(int[] scoville, int K) {
        int answer = 0;
        Arrays.sort(scoville);
        for(int n : scoville){
            queue.add(n);
        }
        while(queue.size()!=1){
            int n1 = queue.peek();
            if(n1>=K) break;
            n1 =queue.poll();
            int n2 =queue.poll();
            int n3 = n1+(n2*2);
            queue.offer(n3);
            answer++;
        }
        if(queue.peek()<K) return -1;
        return answer;
    }
}