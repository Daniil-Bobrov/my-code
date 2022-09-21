#include <iostream>
#include <vector>
#include <map>
#include <stack>
 
using namespace std;
 
using ll = long long;
using ld = long double;
 
void f(map<int, stack<int>>& a, int x){
    while (a[x].size() > 1){
        cout << a[x].top() << endl;
        if (a[a[x].top()].size() > 1){
            f(a, a[x].top());
        }
        a[x].pop();
    }
}
 
int main() {
    int n;
    cin >> n;
    map<int, stack<int>> a;
    vector<int> ans;
    for (int i = 0; i < n; ++i) {
        int t, t1;
        cin >> t >> t1;
        if (a[t1].empty()) {
            ans.push_back(t);
            a[t].push(-1e6);
        } else {
            a[t1].push(t);
            a[t].push(-1e6);
        }
    }
    for (int i = ans.size() - 1; i >= 0; --i) {
        cout << ans[i] << endl;
        f(a, ans[i]);
    }
}










#include <iostream>
#include <bits/stdc++.h>

using namespace std;

int main(){
    int n, m;
    cin >> n >> m;
    vector<int> p(n*m);
    for (int i = 0; i < n*m; ++i) cin >> p[i];
    sort(p.begin(), p.end());
    deque<int> d;
    bool f = false;
    for (int i = 0; i < n; ++i){
        f = false;
        for (int j = i*m+m; j > i*m; --j){
            if (f){
                f = false;
                d.push_back(p[j-1]);
            }
            else{
                f = true;
                d.push_front(p[j-1]);
            }
        }
        while (d.size()){
            cout << d.back() << " ";
            d.pop_back();
        } cout << "\n";
    }
}










#include <iostream>
#include <bits/stdc++.h>

using namespace std;

int main(){
    int n, m;
    string name, cmd;
    cin >> n;
    deque<string> students;
    for (int i = 0; i < n; ++i){
        cin >> name >> cmd;
        if (cmd == "top")
            students.push_front(name);
        else
            students.push_back(name);
    }
    cin >> n;
    for(int i = 0; i < n; ++i){
        cin >> m;
        cout << students[m-1] << "\n";
    }
}
