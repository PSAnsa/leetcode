class Solution {

    /**
     * @param String $s
     * @param Integer $t
     * @return Integer
     */
    function lengthAfterTransformations($s, $t) {
        $mod = 1000000007; // This is 10^9 + 7
        $count = array_fill(0, 26, 0);

        // --- Step 1: Populate initial character counts ---
        // Iterate through the input string 's'.
        for($i=0; $i<strlen($s); $i++){
            
            $charindex = ord($s[$i]) - ord('a'); // Get 0-indexed position (e.g., 'a' -> 0)
            $count[$charindex]++; // Increment count for this character.
        }
        
        // --- Step 2: Perform 't' transformations ---
        // This loop simulates each transformation step.
        for($step=0;$step<$t;$step++){
            // Create a temporary array for the counts *after* this transformation.
            // This prevents using partially updated counts within the same step.
            $tempcount = array_fill(0, 26, 0);
            
            // Handle 'z' transformation: 'z' becomes "ab".
            // All 'z's from the current state ($count[25]) contribute to 'a's ($tempcount[0])
            // and 'b's ($tempcount[1]) in the next state.
            $tempcount[0] = ($tempcount[0] + $count[25]) % $mod; // 'z' contributes to 'a'
            $tempcount[1] = ($tempcount[1] + $count[25]) % $mod; // 'z' contributes to 'b'

            // Handle 'a' through 'y' transformations: character becomes the next letter.
            for($i=0;$i<25;$i++){ // Loop from 'a' (index 0) to 'y' (index 24)
                $tempcount[$i + 1] = ($tempcount[$i + 1] + $count[$i]) % $mod;
            }
            $count = $tempcount; 
        } 
        
        $ans = 0;
        for($i=0;$i<26;$i++){
            $ans = ($ans + $count[$i]) % $mod; // Modulo for the sum.
        }
        
        // Return the final length modulo $mod$.
        return $ans;
    }
}