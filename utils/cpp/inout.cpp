//go:build ignore
#include <bits/stdc++.h>
using namespace std;

string scan_line() {
    string line;
    getline(cin, line);
    return line;
}

vector<string> scan_all_lines() {
    vector<string> lines;
    for (string line; getline(cin, line); ) {
        lines.push_back(line);
    }
    return lines;
}

vector<int> scan_int_vector() {
    string line = scan_line();
    istringstream iss(line);
    vector<int> v;
    int num;
    while (iss >> num) {
        v.push_back(num);
    }
    return v;
}
