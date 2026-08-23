class Solution {
public:
    bool hasDuplicate(vector<int>& nums) {
        unordered_map<int,int> hashSet;
        for(int it:nums){
            if(hashSet[it]==1) return true;
            hashSet[it] +=1;
            
        }
        return false;
    }
};