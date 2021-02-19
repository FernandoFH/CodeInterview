class Solution {
public:
    string intToRoman(int num) {
            map<int, string> keys_values =  {{1,"I"},
                                             {4,"IV"},
                                             {5,"V"},
                                             {9,"IX"},
                                             {10,"X"},
                                             {40,"XL"},
                                             {50,"L"},
                                             {90,"XC"},
                                             {100,"C"},
                                             {400,"CD"},
                                             {500,"D",},
                                             {900,"CM"},
                                             {1000,"M"}};
 
        stringstream result;
  
        while (num != 0) {
        map<int, string>::iterator it = keys_values.end();

        while ((--it)->first > num)
        {
        }
        result << it->second;
        num -= it->first;
    }

    return result.str();
   }
};
