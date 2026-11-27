#include <bits/stdc++.h>
using namespace std;
class Solution {
public:
    NestedInteger deserialize(string s) {
        if (s[0] != '[') return NestedInteger(stoi(s));
        stack<NestedInteger> st;
        int n = s.size();
        for (int i = 0; i < n; ++i) {
            char c = s[i];
            if (c == '[') {
                st.push(NestedInteger());
            } else if (c == ']') {
                NestedInteger cur = st.top(); st.pop();
                if (st.empty()) return cur;
                st.top().add(cur);
            } else if (c == ',') {
                continue;
            } else {
                int sign = 1;
                if (c == '-') {
                    sign = -1;
                    ++i;
                }
                int num = 0;
                while (i < n && isdigit(s[i])) {
                    num = num * 10 + (s[i] - '0');
                    ++i;
                }
                --i;
                NestedInteger ni(sign * num);
                if (!st.empty()) st.top().add(ni);
                else return ni;
            }
        }
        return NestedInteger();
    }
};