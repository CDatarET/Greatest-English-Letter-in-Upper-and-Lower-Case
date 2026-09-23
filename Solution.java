class Solution {
    public String greatestLetter(String s) {
        HashMap<Character, Integer> map = new HashMap<>();
        for(int i = 0; i < s.length(); i++){
            map.put(s.charAt(i), 1);
        }

        for(char c = 'Z'; c >= 'A'; c--){
            if(map.get(c) != null && map.get(Character.toLowerCase(c)) != null){
                return "" + c;
            }
        }

        return "";
    }
}
