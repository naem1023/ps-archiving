#include <iostream> 

using namespace std;

int data[10] = {4, 1, 2, 3, 9, 7, 8, 6, 10, 5};
void swap(int& a, int& b) {
    int temp = a;
    a = b;
    b = temp;
}

void quicksort(int* data, int start, int end) {
    if (start >= end) {
        return;
    }

    int pivot = (start + end) / 2;

    int left = start;
    int right = end;

    while (left <= right) {
        while (data[pivot] > data[left]) {
            left++;
        }

        while (data[pivot] < data[right]) {
            right--;
        }

        if (left <= right) {
            swap(data[left], data[right]);
            left++;
            right--;
        }
    }

    quicksort(data, start, right);
    quicksort(data, left, end);
    
}

int main() {
    for (auto& i: data) {
        cout << i << " ";
    }
    cout << endl;
    cout << sizeof(data) / sizeof(int) - 1 << endl;
    quicksort(data, 0, sizeof(data) / sizeof(int) - 1);
    for (auto& i: data) {
        cout << i << " ";
    }
    cout << endl;
    return 0;
}