import java.util.*;

class Solution {
    public int solution(int[][] maps) {
        int[] x = {0, 1, 0, -1};
        int[] y = {1, 0, -1, 0};
        int n = maps.length;
        int m = maps[0].length;
        
        Queue<int []> queue = new LinkedList<>();
        int[] temp = {0, 0, 1};
        int count = 0;
        maps[0][0] = 0;
        queue.offer(temp);
        
        int check = 0;
        while(!queue.isEmpty()) {
            int[] current = queue.poll();
            
            if(current[0] == n-1 && current[1] == m-1){
                count = current[2];
                check = 1;
                break;
            }
            
            for(int i=0;i<4;i++){
                int new_x = current[0] + x[i];
                int new_y = current[1] + y[i];
                
                if(new_x >= 0 && new_x < n && new_y >= 0 && new_y < m && maps[new_x][new_y] == 1){
                    maps[new_x][new_y] = 0;
                    count += 1;
                    int[] new_temp = {new_x, new_y, current[2]+1};
                    queue.offer(new_temp);
                    
                }
            }
            
        }
        if(check == 0)
            return -1;
        
        return count;
    }
}