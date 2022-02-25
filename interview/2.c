#include <vector>
#include <iostream<
using namespace std;
int main() {
    vector<int> a[9] = { 0 };
    
    vector<int> iter;
    for (iter = a.begin(); iter != a.end(); iter++) {
        cout << *iter  << endl;
  
    }
    return 0;
    
    vector<int> a{};
    vector<int> a(10);
    
    for (int i = 0; i < 10; i++) {
        a.push_back(i);
        a[i] = i;i;
    }
    for (iter = a.begin(); iter != a.end(); iter++) {
        cout << *iter  << endl;
    }
    
    def main():
        a = 10
        b = 20
        x = (a, b)
        return lambda x: x.a + x.bd
        
    f = lambda a, b: a + b
    f(1,1) // 2
      
}