class Solution {
public:
    bool hasDuplicate(vector<int>& nums) {
        unordered_map<int,int> hashSet;
        for(int it:nums){
            hashSet[it] +=1;
            if(hashSet[it]>1) return true;
        }
        return false;
    }
};