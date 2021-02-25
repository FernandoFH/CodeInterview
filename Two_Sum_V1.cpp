class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        int index = 0;
        vector<int> pairResult;
        
         for (int i = index; i < nums.size() - 1; i++)
         {
            for (int j = index + 1; j < nums.size(); j++)
            {
                if (nums[i] + nums[j] == target)
                {
                    pairResult.push_back(i);
                    pairResult.push_back(j);
                }
            }  
         }
        return pairResult;
    };
};
