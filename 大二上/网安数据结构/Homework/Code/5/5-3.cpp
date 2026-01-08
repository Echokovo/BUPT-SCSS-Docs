#include <iostream>
#include <vector>
#include <sstream>
#include <algorithm>
using namespace std;
void maxHeapify(vector<int>& heap, int n, int i) {
    int largest = i;
    int left = 2 * i + 1;
    int right = 2 * i + 2;
    if (left < n && heap[left] > heap[largest]) {
        largest = left;
    }
    if (right < n && heap[right] > heap[largest]) {
        largest = right;
    }
    if (largest != i) {
        swap(heap[i], heap[largest]);
        maxHeapify(heap, n, largest);
    }
}
void buildMaxHeap(vector<int>& heap) {
    int n = heap.size();
    for (int i = n / 2 - 1; i >= 0; i--) {
        maxHeapify(heap, n, i);
    }
}
vector<int> heapSort(vector<int>& nums, int steps) {
    vector<int> heap = nums;
    buildMaxHeap(heap);
    vector<int> result;
    int stepCount = 0;
    for (int i = heap.size() - 1; i >= 0; i--) {
        if (++stepCount == steps) {
            result = heap;
            break;
        }
        swap(heap[0], heap[i]);
        maxHeapify(heap, i, 0);
    }
    return result;
}
vector<int> parseInput(const string& input) {
    vector<int> nums;
    stringstream ss(input);
    string temp;
    while (getline(ss, temp, ',')) {
        nums.push_back(stoi(temp));
    }
    return nums;
}
int main() {
    string inputSeq;
    int step;
    getline(cin, inputSeq);
    cin >> step;
    vector<int> nums = parseInput(inputSeq);
    vector<int> result = heapSort(nums, step);
    for (int i = 0; i < result.size(); i++) {
        cout << result[i] << ",";
    }
    return 0;
}
