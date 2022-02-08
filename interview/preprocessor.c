#include <stdio.h>

/*
GCC: -D매크로이름, -D매크로이름=값
*/
#define DEBUG
#define TEST

int main() {
#ifdef DEBUG
    printf("If macro is defined, compile these.\n");
#endif

#ifndef VERSION10
    prtinf("If macro isn't defined, complie these.\n");
#endif

#if (defined DEBUG && !defined TEST) && !defined VERSION10
    printf("haha\n");

#elif defined VERSION9
    #if 1
        printf("'If' can be dubplicated.\n");
    #else
        // 
    #endif
#else
    printf("else!\n");
#endif
    return 0;
}