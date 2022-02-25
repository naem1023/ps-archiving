#include <iostream>

using namespace std;

int data[10] = {123,3456,345634,5,235,45,234,12};

void swap(int& a, int& b) {
    int temp = a;
    a = b;
    b = temp;
}

void quicksort(int* data, int start, int end) {
    if (start >= end) return;

    int pivot = (start + end) / 2;
    int left = start;
    int right = end;

    while (left <= right) {
        while (data[pivot] > data[left]) left++;
        while (data[pivot] < data[right]) right--;

        if (left <= right) {
            swap(data[left], data[right]);
            left++; right--;
        }
    }

    quicksort(data, start, right);
    quicksort(data, left, end);

}

int main() {
    for (auto& val: data) {
        cout << val << " ";
    }
    cout << endl;

    quicksort(data, 0, sizeof(data) / sizeof(data[0] - 1));
    for (auto& val: data) {
        cout << val << " ";
    }
    cout << endl;
    return 0;
}