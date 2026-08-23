// Brute Force

class Solution {
  public:
    vector<int> twoSum(vector<int>& nums, int target) {
        vector<int> pairResult;

         for (int i = 0; i < nums.size() -1 ; i++)
         {
            for (int j = i + 1; j < nums.size(); j++)
            {
                if (nums[j] + nums[i] == target)
                {
                    pairResult.push_back(i);
                    pairResult.push_back(j);
                }
            }  
         }
    return pairResult;
   };
};
