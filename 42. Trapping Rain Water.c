int trap(int* height, int heightSize) {
    int n = heightSize;
    int L2R_up = 0;
    int R2L_up = 0;
    int L2R_line[n];
    int R2L_line[n];
    int result = 0;
    int result2 = 0;

    for (int i = 0; i < n; i++) {
        L2R_up = (L2R_up > height[i]) ? L2R_up : height[i];
        L2R_line[i] = L2R_up;
    }

    for (int i = n - 1; i >= 0; i--) {
        R2L_up = (R2L_up > height[i]) ? R2L_up : height[i];
        R2L_line[i] = R2L_up;

        result = (R2L_line[i] < L2R_line[i]) ? R2L_line[i] : L2R_line[i];
        result = result - height[i];

        if (result > 0) result2 += result;
    }
    return result2;
}
