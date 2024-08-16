import java.util.*;

class Solution {
    public int solution(int n, int[][] computers) {
        int[] visited = new int[n];
        
        int count = 0;
        for(int i=0;i<n;i++){
            
            if(visited[i] == 0) {
                visited[i] = 1;
                count += 1;
                dfs(visited, i, computers);
            }
        }
        
        return count;
    }
    
    private void dfs(int[] visited, int i, int[][] computers) {
        int[] adj = computers[i];
        
        for(int k=0;k<adj.length;k++){
            if(visited[k] == 0 && adj[k] == 1){
                visited[k] = 1;
                dfs(visited, k, computers);
            }
                
        }
    }
}