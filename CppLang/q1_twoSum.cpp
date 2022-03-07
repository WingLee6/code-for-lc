/***
 * 给定一个整数数组 nums 和一个整数目标值 target，请你在该数组中找出 和为目标值 target  的那 两个 整数，并返回它们的数组下标。
 * 你可以假设每种输入只会对应一个答案。但是，数组中同一个元素在答案里不能重复出现。
 * 你可以按任意顺序返回答案。
 * 示例 1：
 * 输入：nums = [2,7,11,15], target = 9
 * 输出：[0,1]
 * 解释：因为 nums[0] + nums[1] == 9 ，返回 [0, 1] 。
 * 来源：力扣（LeetCode）
 * 链接：https://leetcode-cn.com/problems/two-sum
 * 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
***/

#include <iostream>
#include <vector>
using namespace std;
 
class Solution {  
public:
    vector<int> twoSum(vector<int>& nums, int target) {
		// 本算法暴力求解
		vector<int> result;
		for (int i = 0; i < nums.size(); i++)
		{
			for (int j = i+1; j < nums.size(); j++)
			{	
				if (target == nums[i]+nums[j])
				{
					result.push_back(i);
					result.push_back(j);
					return result;
				}	
			}
		}
		// 没找到返回空结果
		return result;
    }
};
 
int main(){
	Solution solu;
	// 初始化顺序数组/int型
	vector<int> position;
	vector<int> arr;
	
	// 元素插入数组
	for(int i=0; i<3; i++) {
		// 产生 1～10 的随机数并插入数组
        arr.push_back(rand()%10 + 1);
        // cout << arr[i] << ",";    
    }
	
	// 目标和
	int target = 12;

	// 带入方法
	position = solu.twoSum(arr, target);
	
	// 输出结果
	for(int i=0; i<position.size(); i++)
		cout << position[i] << endl;
	return 0 ;
}