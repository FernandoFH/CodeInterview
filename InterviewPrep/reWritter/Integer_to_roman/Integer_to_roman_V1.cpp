//Convert Integer to Roman Numeral
class Solution {
public:
    string intToRoman(int num) {
        // List values and edge cases 
        vector<int> keys({1, 4, 5, 9, 10, 40, 50, 90, 100, 400, 500, 900, 1000});    
        vector<string> values({"I", "IV", "V", "IX", "X", "XL", "L", "XC", "C", "CD", "D", "CM", "M"});
 
        string result = "";
        int index = values.size() - 1;   
                
        while (num && index >= 0) {
            if (num/keys[index] == 0) {
                index--;
            } else {
                int count = num/keys[index];
                while(count--)
                    result += values[index];
                num %= keys[index];
            }
        }
        return result;
   }
};
