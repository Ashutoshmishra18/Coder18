class Solution {
    public boolean isValid(String word) {
        if (word.length()<3) return false;

        for(char c: word.toCharArray()){
            if (!Character.isLetterOrDigit(c)) return false;
        }
        String vowels="aeiouAEIOU";
        boolean hasVowels=false;
        boolean hasConsonant=false;
        for (char c: word.toCharArray()){
            if(Character.isLetter(c)){
                if(vowels.indexOf(c)!=-1){
                    hasVowels=true;
                }else{
                    hasConsonant=true;
                }
            }
            if (hasVowels && hasConsonant) return true;
        }
        return false;
        
    }
}