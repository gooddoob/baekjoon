class MinHeap:
    def __init__(self):
        self.heap = []

    def heappush(self, value):
        self.heap.append(value)
        self._siftup(len(self.heap) - 1)

    def heappop(self):
        if len(self.heap) == 1:
            return self.heap.pop()
        min_value = self.heap[0]
        self.heap[0] = self.heap.pop()
        self._siftdown(0)
        return min_value

    def _siftup(self, pos):
        while pos > 0:
            parent = (pos - 1) // 2
            if self.heap[pos] < self.heap[parent]:
                self.heap[pos], self.heap[parent] = self.heap[parent], self.heap[pos]
                pos = parent
            else:
                break

    def _siftdown(self, pos):
        end = len(self.heap)
        start = pos
        child = 2 * pos + 1
        while child < end:
            right = child + 1
            if right < end and self.heap[right] < self.heap[child]:
                child = right
            if self.heap[child] < self.heap[start]:
                self.heap[start], self.heap[child] = self.heap[child], self.heap[start]
                start = child
                child = 2 * start + 1
            else:
                break

def min_comparison_count(card_bundles):
    heap = MinHeap()
    for bundle in card_bundles:
        heap.heappush(bundle)
    
    total_comparisons = 0
    
    while len(heap.heap) > 1:
        first = heap.heappop()
        second = heap.heappop()
        
        combined = first + second
        total_comparisons += combined
        
        heap.heappush(combined)
    
    return total_comparisons

# 입력 받기
n = int(input())
card_bundles = [int(input()) for _ in range(n)]

# 최소 비교 횟수 출력
print(min_comparison_count(card_bundles))
