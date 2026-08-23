class Solution {
public:
    bool isAnagram(string s, string t) {
        if(s.length()!=t.length()) return false;
        int freq[26] ={0};
        //int tfreq[26] ={0};
        for(int i=0;i<s.length();i++){
            freq[s[i]%97] +=1;
            freq[t[i]%97] -=1;
        }
        for(int i=0;i<26;i++){
            if(freq[i]!=0){
                return false;
            }
        }
        // sort(s.begin(),s.end());
        // sort(t.begin(),t.end());
        // int n = s.length();
        // for(int i=0;i<n;i++){
        //     if(s[i]!=t[i]){
        //         return false;
        //     }
        // }
        return true;
        
    }
};
