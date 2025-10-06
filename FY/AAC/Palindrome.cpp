#include<bits/stdc++.h>
using namespace std;

void palindrome(string s){
    int n = s.length();
    int l = 0;
    int r = n -1;
    while(l<=r){
        if(s[l]!=s[r]){
            cout<<"Not a palindrome";
            return;
        }
        l++;
        r--;
    }

    cout<<"It's a Palindrome!";
}

int main()
{
    string s;
    cin>>s;
    palindrome(s);
    return 0;
}