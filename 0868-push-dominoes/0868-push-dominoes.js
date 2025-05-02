/**
 * @param {string} s
 * @return {string}
 */
//  Calcuklating the net force and identifying which way it went to
var pushDominoes = function(s) {
    let n = s.length
    const forces =  new Array(n).fill(0)
    let force = 0
    for(let i=0;i<n;i++){
        //a strong right force
        if(s[i] == 'R'){
            force = n
        } else if(s[i] == 'L'){
            force = 0
        }else{
            // a force from left or right came, so force weeked, so decrement by 1
            force = Math.max(force-1, 0)
        }
        forces[i] += force

    }
    // calculating force from right to left
    force = 0
    for(let i = n-1; i>= 0; i--){
        if(s[i] == 'L'){
            force = n
        }else if(s[i] == "R"){
            force = 0
        }else{
            force = Math.max(force-1, 0)
        }
        forces[i] -= force

    }
    let str = "";
    for(const f of forces){
        if(f > 0){
            str += 'R';
        }else if(f < 0){
            str += 'L'
        }else{
            str += '.'
        }
    }
    return str;
    
};