#include <stdio.h>
#include <stdlib.h>
void trans(char* ans, int n, int base, int cnt) {
    if (n) {
        trans(ans, n / base, base, cnt + 1);

        int res = n % base;

        if (res <= 9) 
            ans[cnt] = res + '0';
        else
            ans[cnt] = res - 10 + 'A';
    }
}

int main() {
    int n, base;
    scanf("%d %d", &n, &base);
    char* ans = (char*)malloc(sizeof(char) * 10000);
    trans(ans, n, base, 0);
    printf("Answer is %s", ans);
    
    return 0;
}

