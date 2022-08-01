/*
 * @lc app=leetcode.cn id=1374 lang=cpp
 *
 * [1374] 生成每种字符都是奇数个的字符串
 */

// @lc code=start
#include <iostream>
#include <vector>
using namespace std;

class Solution {
public:
    string generateTheString(int n) {
        // 法1:
        // return (n & 1) ? string(n, 'a') : string(n - 1, 'a') + string(1, 'b');

        // 法2:
        string str="";
        if(n%2==0){
            str.append(1,'a');
            str.append(n-1,'b');
        }
        else{
            str.append(n,'a');
        }
        return str;
    }
};
// @lc code=end

