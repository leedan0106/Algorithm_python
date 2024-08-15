import java.util.*;

class Solution {
    public int[] solution(int[] array, int[][] commands) {
        int[] answer = new int[commands.length];
        
        for(int i=0;i<commands.length;i++) {
            int[] temp = commands[i];
            
            List<Integer> list = new ArrayList<>();

            for(int j=temp[0]-1;j<temp[1];j++) {
                list.add(array[j]);
            }

            Collections.sort(list);
            answer[i] = list.get(temp[2]-1);
        }
        
        return answer;
    }
}