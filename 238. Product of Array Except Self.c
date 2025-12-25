int* productExceptSelf(int* nums, int n, int* returnSize){
    *returnSize = n;

    int* answer = (int*)malloc(sizeof(int) * n);
    for (int i = 0; i < n; i++) {
        answer[i] = 1;
    }

    int left = 1;
    for (int i = 0; i < n - 1; i++) {
        left *= nums[i];
        answer[i + 1] *= left;
    }

    int right = 1;
    for (int i = n - 1; i > 0; i--) {
        right *= nums[i];
        answer[i - 1] *= right;
    }
    return answer;
}
