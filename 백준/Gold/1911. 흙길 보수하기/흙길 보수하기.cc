#include <cstdio>
#include <vector>
#include <algorithm>

using namespace std;
int main() {
  int n, l;
  scanf("%d %d", &n, &l);
  vector< pair<int, int> > gu;

  for(int i=0;i<n;i++){
    int s, e;
    scanf("%d %d", &s, &e);
    gu.push_back(make_pair(s, e));
  }

  sort(gu.begin(), gu.end());

  int start = gu[0].first;
  int count = 0;
  for(int i=0;i<n;i++){
    pair<int, int> temp = gu[i];
    start = max(start, temp.first);
    int size = temp.second - start;
    int cnt = (size + l - 1) / l;
    count += cnt;
    start = start + cnt * l;
  }
  printf("%d\n", count);

  return 0;
}