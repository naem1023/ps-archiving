#include <iostream>
#include <stdio.h>

int N, arr[10000001];
int *arr2;

void merge(int left, int right) {
    int mid = (left + right) / 2;

    int i = left;
    int j = mid + 1;
    int k = left; // counter of arr2

    while (i <= mid && j <= right) {
        if (arr[i] <= arr[j]) {
            arr2[k++] = arr[i++];
        }
        else {
            arr2[k++] = arr[j++];
        }
    }

    int tmp = i > mid ? j : i;

    // 남은 원소를 모두 넣는다.
    while (k <= right) {
        arr2[k++] = arr[tmp++];
    }

    for (int i = left; i <= right; i++) {
        arr[i] = arr2[i];
    }
}


void partition(int left, int right) {
    int mid;
    if (left < right) {
        mid = (left + right) / 2;
        partition(left, mid);
        partition(mid + 1, right);
        merge(left, right);
    }
}
int main() {
    scanf("%d", &N);
    arr2 = new int[N];
    for (int i = 0; i < N; i++) {
        scanf("%d", &arr[i]);
    }

    partition(0, N - 1);

    for (int i = 0; i < N; i++) {
        printf("%d\n", arr[i]);
    }
    return 0;
}