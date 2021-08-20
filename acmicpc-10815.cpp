#include <iostream>
#include <vector>
#include <algorithm>
#include <map>
using namespace std;

bool bs(int* arr, int start, int end, int target_num) {
    int mid;

    while (start <= end) {   
        mid = (start + end) / 2;
        if (arr[mid] == target_num) {
            return true;
        }
        else if (arr[mid] > target_num) {
            end = mid - 1;        
        }
        else{
            start = mid + 1;
        }
    }
    return false;
}

int main() {
    cin.tie(NULL);
    cout.tie(NULL);
    ios_base::sync_with_stdio(false);    
    
    int N, M;
    cin >> N;

    int* n_arr = new int[N];
    for (int i = 0; i < N; i++) {
        cin >> n_arr[i];
    }

    cin >> M;

    int* m_arr = new int[M];
    for (int i = 0; i < M; i++) {
        cin >> m_arr[i];    
    }
    
    sort(n_arr, n_arr + N);

    map<int, int> m;
    for (int i = 0; i < M; i++) {
        m.insert({m_arr[i], 0});
    }

    bool find_flag = false;
    for (int i = 0; i < M; i++) {
        if (bs(n_arr, 0, N - 1, m_arr[i])) {
            m[m_arr[i]] = 1;
        }
    }

    for (int i = 0; i < M; i++) {
        cout << m[m_arr[i]] << " ";
    }
    
    return 0;
}