import java.util.*;

class Solution {
    public List<Integer> solution(int[] progresses, int[] speeds) {
        List<Integer> diff = new ArrayList<>();
        int size = progresses.length;
        for(int i=0;i<size;i++){
            int num = (int)Math.ceil((100 - progresses[i]) / (double)speeds[i]);
            diff.add(num);
        }

        List<Integer> result = new ArrayList<>();
        Stack<Integer> stack = new Stack<>();
        int count = 0;
        int preNum = -1;
        for(int i=0;i<diff.size();i++) {
            if (preNum == -1) {
                count = 1;
                preNum = diff.get(i);
                continue;
            }
            
            if(preNum < diff.get(i)) {
                result.add(count);
                count = 1;
                preNum = diff.get(i);
                continue;
            }
            
            count += 1;
        }
        result.add(count);
        return result;
    }
}