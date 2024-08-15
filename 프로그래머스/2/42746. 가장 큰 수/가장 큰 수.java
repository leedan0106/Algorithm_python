import java.util.*;

class Solution {
    public String solution(int[] numbers) {
        List<Integer> list = new ArrayList<>();
        
        for(int n : numbers){
            list.add(n);
        }

        Collections.sort(list, new Comparator<Integer>() {
            @Override
            public int compare(Integer n1, Integer n2){
                String case1 = n1.toString() + n2.toString();
                String case2 = n2.toString() + n1.toString();
                
                if(case1.compareTo(case2) > 0) {
                    return -1;
                }
                if(case1.compareTo(case2) == 0) {
                    return 0;
                }
                    
                return 1;
            }
        });
        
        String result = "";
        if (list.get(0) == 0) {
            return "0";
        }
        
        for(Integer a : list) {
            result = result + a.toString();
        }
        return result;
    }
}