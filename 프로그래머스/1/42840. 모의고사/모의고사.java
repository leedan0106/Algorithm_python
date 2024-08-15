import java.util.*;

class Solution {
    public int[] solution(int[] answers) {
        
        int[] an1 = {1,2,3,4,5}; //5
        int[] an2 = {2,1,2,3,2,4,2,5}; //8
        int[] an3 = {3,3,1,1,2,2,4,4,5,5}; //10
        
        int len = answers.length;
        List<Integer> currect = Arrays.asList(0, 0, 0);
        
        for(int i=0;i<len;i++){
            if(answers[i] == an1[i%5]) 
                currect.set(0, currect.get(0)+1);
            
            if(answers[i] == an2[i%8])
                currect.set(1, currect.get(1)+1);
            
            if(answers[i] == an3[i%10])
                currect.set(2, currect.get(2)+1);
        }
        
        int max_val = Collections.max(currect);
        List<Integer> result = new ArrayList<>();
        for(int i=0;i<3;i++){
            if(currect.get(i) == max_val)
                result.add(i+1);
        }
        
        int[] answer = result.stream().mapToInt(x->x).toArray();
        return answer;
    }
}