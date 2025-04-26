class Solution {

    /**
     * @param String $s
     * @param Integer $k
     * @return Integer
     */
    function maxVowels($s, $k) {
        $vowels = ["a", "e", "i","o","u"];
        $start = 0;
        $val = 0;
        $maxvalue  = 0;
        for($end = 0;$end < strlen($s);$end++){
            if(in_array($s[$end], $vowels)){
                $val++;
            }
            if($end >= $k-1){
                $maxvalue = max($maxvalue, $val);
                if(in_array($s[$start], $vowels)){
                    $val--;
                }
                $start++;
            }
        }
        return $maxvalue;
    }
}