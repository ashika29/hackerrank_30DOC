// Question link:
// https://www.hackerrank.com/challenges/30-conditional-statements/problem
// Code section:
#include <bits/stdc++.h>

using namespace std;

string solve(int n){
    int x = n%2;
    switch(x){
        case 0:
            if((n>1)&&(n<6))
                return "Not Weird";
            if((n>5)&&(n<21))
                return "Weird";
            if(n>20)
                return "Not Weird";
        default:
            return "Weird";
    }
}

int main()
{
    int N;
    cin >> N;
    cin.ignore(numeric_limits<streamsize>::max(), '\n');
    cout<<solve(N);
    return 0;
}
