## 힙
힙은 특정한 규칙을 갖는 Tree 구조로, 최댓값과 최솟값을 찾는 연산을 빠르게 하기 위해 고안된 완전 이진트리를 기본으로 한다.

파이썬에서는 binary tree 기반의 min heap 자료구조를 제공한다.

min heap을 사용하면 원소들이 항상 정렬된 상태로 추가되고 삭제되며, min heap에서 가장 작은 값은 언제나 index 0, 즉, binary tree의 Root에 위치한다.

내부적으로 min heap 내의 모든 원소(k)는 항상 자식 원소들(2k+1, 2k+2) 보다 크기가 작거나 같도록 원소가 추가되고 삭제된다.

## heapq 모듈 사용

### python 모듈 import
```
import heapq

from heapq import heappush, heappop, heapify
```

### 힙에 원소 추가(push) 및 삭제(pop)

+ heapq.heappush(heap, item) : 힙 구조를 유자하면서, item을 heap 안에 추가
+ heapq.heappop(heap) : 힙 구조를 유지하면서, 가장 작은 항목을 삭제 & 반환
+ heap[0] : 가장 작은 항목을 삭제하지 않고 확인만 하는 경우
+ heappush와 heappop은 O(logN)의 시간 복잡도를 갖는다

+ heapq.heappushpop(heap, item) : 힙에 item을 푸시한 다음, heap에서 가장 작은 항목을 팝하고 반환. heappush와 heappop을 별도로 호출하는 것보다 더 효율적
+ heapq.heapreplace(heap, item) : 힙에서 가장 작은 항목을 pop하고 반환한 뒤 item 푸시. heappop과 heappush를 별도로 호출하는 것보다 더 효율적

```
heap = []

heapq.heappush(heap,4)
heapq.heappush(heap,1)
heapq.heappush(heap,7)
heapq.heappush(heap,3)
print(heap)

>>>[1, 3, 7, 4]

heapq.heappop(heap)
>>> 1

print(heapq)
>>>[3,7,4]


```

### list to heap

+ heapq.heapify(list) : 일반 리스트를 힙 구조로 변환
+ 데이터를 heqp architecture로 변환할 때 두 가지 방식으로 접근할 수 있다.
+ Sift Up : 비어있는 tree를 채워나가는 과정. 주어진 노드의 부모 노드와의 비교연산을 수행하여 이를 만족시키거나, 그렇지 않으면 root에 도착할 때 까지 Swap하는 방법이다. heappush에서 사용된다.
+ Sift Down : 비정렬 상태로 채워진 tree를 재구성하는 과정. 주어진 노드의 child node's 중 key가 큰 값(or 작은 값) 과 비교연산을 수행해 property를 만족하거나, 그렇지 않으면 leaf에 도착할 때 까지 swap하는 방법이다. heappop에서 사용된다.
+ sift up과 sift down의 시간 복잡도는 O(logN)이다.
+ Sift Up의 시간복잡도는 주어진 노드부터 root Node 까지의 높이 로 볼 수 있으며 Sift Down의 시간복잡도는 해당 노드부터 leaf Node 까지의 높이이다.
+ 힙을 구성하는 완전이진트리는 그 성질에 의해 약 n/2 개의 노드는 leaf 노드에 존재하게 된다.
+ 따라서 Sift Up으로 heap을 설계하는 경우 시간 복잡도는 O(NlogN)이 되며, Sift down의 경우 O(N)이 된다.
+ 파이썬에서 제공하는 heapify 함수는 sift down 방식을 따르고 있기에 시간 복잡도는 O(N)이며 heappush를 사용하는 것보다 훨씬 효율적이다
+ 주의할 점은 새로운 리스트를 반환하는 것이 아니라 인자로 넘긴 리스트를 직접 변경하는 것.
+ 따라서 원본 리스트의 형태를 보존해야 하는 경우, 반드시 해당 리스트를 복제한 후에 인자로 넘겨야 한다.

```
heap = [4,1,7,3,2,6]
heapq.heapify(heap)  
print(heap)

>>> [1, 2, 6, 4, 3, 7]
```

### 최대힙
```
nums = [4, 1, 7, 3, 8, 5]
heap = []

for num in nums:
  heapq.heappush(heap, (-num, num)) 

while heap:
  print(heapq.heappop(heap)[1])
 
>>>8
>>>7
>>>5
>>>4
>>>3
>>>1
```

### n번째 최소값/최대값
```
def nth_smallest(nums, n):
    heap = []
    for num in nums:
        heapq.heappush(heap, num)

    nth_min = None
    for _ in range(n):
        nth_min = heapq.heappop(heap)

    return nth_min

print(nth_smallest([4, 1, 7, 3, 8, 5], 3))

>>>4
```
```
def nth_smallest(nums, n):
    heapq.heapify(nums)

    nth_min = None
    for _ in range(n):
        nth_min = heapq.heappop(nums)

    return nth_min
```

+ heapq.nlargest(n, iterable, key) : n개의 가장 큰 요소의 리스트 반환, key로 비교 키 함수 지정 가능
+ heapq.nsmallest(n, iterable, key) : n개의 가장 작은 요소의 리스트 반환, key로 비교 키 함수 지정 가능
+ n값이 작을 때 더 잘 동작하며, 값이 크면 sorted 기능을 사용하는 것이 더 효율적이다.
+ n이 1이면 min()과 max() 함수를 사용하는 것이 더 효율적이다. 이 함수를 반복해서 사용해야 하는 경우 iterable을 힙으로 바꾸는 게 좋다.

```
heap = [4, 1, 7, 3, 8, 5]
heapq.heapify(heap)
print(heapq.nsmallest(3, heap))
print(heapq.nlargest(3, heap))

>>>[1,3,4]
>>>[8,7,5]
```

### 힙 정렬
+ 힙이 사라질 때까지 root 제거, 반환, 재정렬을 반복하는 방식의 정렬법
+ 요소의 개수가 N개라면 시간 복잡도는 항상 O(NlogN)
+ 전체 자료 정렬이 아닌 상위 값 일부만을 필요로 할 때 사용하기 좋다.
+ 다만 데이터의 상태에 따라 다른 정렬법들에 비해 조금 느릴 수 있으며, 안정성을 보장받지 못한다.
```
def heap_sort(nums):
  heapq.heapify(nums)

  sorted_nums = []
  while nums:
    sorted_nums.append(heapq.heappop(nums))
  return sorted_nums

print(heap_sort([4, 1, 7, 3, 8, 5]))

>>>[1, 3, 4, 5, 7, 8]
```


--------------
reference

https://ssocoit.tistory.com/97

https://velog.io/@emplam27/%EC%9E%90%EB%A3%8C%EA%B5%AC%EC%A1%B0-%EA%B7%B8%EB%A6%BC%EC%9C%BC%EB%A1%9C-%EC%95%8C%EC%95%84%EB%B3%B4%EB%8A%94-%ED%9E%99Heap
