import java.util.*;

class Solution {
    public int solution(int[] scoville, int K) {
        PriorityQueue<Integer> queue = new PriorityQueue<>();
        for(int s:scoville){
            queue.add(s);
        }
        
        
        int count = 0;
        while(queue.size() > 1){
            if(queue.peek() >= K)
                break;
            
            int num1 = queue.poll();
            int num2 = queue.poll();
            int new_val = num1 + (num2*2);
            count += 1;
            queue.add(new_val);
            
        }
        
        if(queue.peek() < K)
            return -1;
        return count;
    }
}