import java.util.*;

class Solution {
    int max_count = 0;
    
    public int solution(int k, int[][] dungeons) {
        int[] visited = new int[dungeons.length];
        dfs(k, dungeons, visited, 0);
        return max_count;
    }
    
    private void dfs(int k, int[][] dungeons, int[] visited, int count) {
        int len = dungeons.length;
        for(int i=0;i<len;i++) {
            if (visited[i] == 0 && k >= dungeons[i][0])  {
                visited[i] = 1;
                dfs(k-dungeons[i][1], dungeons, visited, count+1);
                visited[i] = 0;
            }
        }
        if(count > max_count)
            max_count = count;
    }
}