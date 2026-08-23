class Solution {
public:
    vector<int> getConcatenation(vector<int>& nums) {
        vector<int> result;
        result = nums;
        for(auto it: nums){
            result.push_back(it);
        }
        return result;
        
    }
};