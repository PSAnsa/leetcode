/**
 * @param {number[]} gain
 * @return {number}
 */
var largestAltitude = function(gain) {
    
    
        let maxaltitude = 0;
        let altitude = 0;
        for(let i = 0; i< gain.length; i++){
            altitude += gain[i]; 
            maxaltitude = Math.max(maxaltitude, altitude);
        } 
        return maxaltitude;  
};