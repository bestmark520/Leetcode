int hIndex(int* citations, int citationsSize) {
    int n = citationsSize;
    int count[n + 1];
    for (int i = 0; i <= n; i++) {
        count[i] = 0;
    }
    
    for (int i = 0; i < n; i++) { // bucket分類
        int c = citations[i];
        if (c >= n) {
            count[n]++;
        } else {
            count[c]++;
        }
    }
    
    int total = 0;
    for (int h = n; h >= 0; h--) {
        total += count[h];  // 被引用 >= h 的論文數
        if (total >= h) {
            return h;
        }
    }
    return 0;
}
