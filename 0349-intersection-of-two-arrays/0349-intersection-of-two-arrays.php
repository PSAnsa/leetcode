class Solution {

    /**
     * @param Integer[] $nums1
     * @param Integer[] $nums2
     * @return Integer[]
     */
    function intersection($nums1, $nums2) {
        $result = array();
        $set1 = array_flip(array_unique($nums1));
        foreach($nums2 as $num){
            if(isset($set1[$num])){
                $result[$num] = $num;
            }
        }
        return $result;
        
    }
}