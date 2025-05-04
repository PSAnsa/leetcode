class Solution {

    /**
     * @param Integer[] $nums1
     * @param Integer[] $nums2
     * @return Integer[][]
     */
    function findDifference($nums1, $nums2) {
        $result = array();
        $result[0] = array_unique(array_diff($nums1, $nums2));
        $result[1] = array_unique(array_diff($nums2, $nums1));
        return $result;
    }
}