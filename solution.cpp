class Solution {
public:
    string greatestLetter(string s) {
        unordered_map<char, int> map;
        for(int i = 0; i < s.length(); i++){
            map[s[i]] = 1;
        }

        for(char c = 'Z'; c >= 'A'; c--){
            if(map.contains(c) && map.contains((char)(c + 32))){
                return std::string (1, c);
            }
        }

        return "";
    }
};
