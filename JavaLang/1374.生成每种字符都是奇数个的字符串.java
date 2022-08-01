/*
 * @lc app=leetcode.cn id=1374 lang=java
 *
 * [1374] 生成每种字符都是奇数个的字符串
 */

// @lc code=start
class Solution {
    public String generateTheString(int n) {
        int count = (n % 2 == 0) ? n - 1 : n;
        StringBuilder result  = new StringBuilder();
        
        for (int i = 0; i < count; i++){
            result.append('a');
        }
        
        if( n % 2 == 0){
            result.append('b');
        }
        return result.toString();
    }
}
// @lc code=end

