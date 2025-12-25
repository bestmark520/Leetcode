
void reverse(int* nums, int left, int right) {
    while (left < right) {
        int tmp = nums[left];
        nums[left] = nums[right];
        nums[right] = tmp;
        left++;
        right--;
    }
}

void rotate(int* nums, int numsSize, int k) {
    if (numsSize <= 1 || k == numsSize) return;
    
    k = k % numsSize;   // 處理 k > n 的情況
    reverse(nums, 0, numsSize - 1);
    reverse(nums, 0, k - 1);
    reverse(nums, k, numsSize - 1);
}
