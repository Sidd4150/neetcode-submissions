class Solution {
    /**
     * @param {string} s
     * @return {boolean}
     */
    isValid(s) {
        const map = new Map()
        let stack = [];
        map.set("}","{")
        map.set("]","[")
        map.set(")","(")
        for (const check of s) {
            
            if ("{[(".includes(check))  {
                stack.push(check)
            }else if ("}])".includes(check)) {
                if (stack.pop() != map.get(check)) {
                    return false 
                }
            }
   
        
        }
        return stack.length === 0
    }
}
