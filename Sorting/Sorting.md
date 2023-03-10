# Sorting

## 소개
- 데이터를 특정한 기준에 따라 순서대로 나열한다.
- 이진 탐색(Binary Search)에 전처리 과정이므로 중요한 알고리즘이다.

## 정렬 알고리즘 종류
1. 선택 정렬(Select Sort): 현재 데이터들 중에 가장 작은(큰) 것을 선택하는 알고리즘
    - 시간 복잡도
        - 최악: O(N^2^)
2. 삽입 정렬(Insertion Sort): 현재 데이터들 중 하나씩 확인하며 적절한 위치에 삽입하는 알고리즘
    - 특징
        - 정렬이 이루어진 데이터는 오름차순이나 내림차순을 유지하고 있음
        - 이미 정렬이 어느정도 되어있는 데이터들 이라면 Quick Sort 보다 빠를수도 있음
    - 시간 복잡도
        - 최악: O(N^2^)
        - 최선: O(N)
3. 퀵 정렬(Quick Sort): 기준이 되는 데이터를 설정하고 그 기준보다 큰 데이터와 작은 데이터의 위치를 바꾸는 알고리즘
    - 특징
        - 피벗(Pivot)이 사용되면 이는 기준이 된다.
        - 탐색 과정중 큰 데이터와 작은 데이터가 서로 엇길리면 작은 데이터와 피벗이 서로 자리를 바꾸며 분할이 일어난다.
        - 데이터들이 이미 정렬이 되어 있다면 피벗보다 작은것은 없기에 작은것을 찾기위해 모든 데이터를 탐색하기에 비효율적이다.
    - 시간 복잡도
        - 최악: O(N^2^) -> 모두 정렬이 되어진 데이터들
        - 평균: O(NlogN)
4. 계수 정렬(Count Sort): 가장 작은 데이터와 가장 큰 데이터를 담을 수 있는 범위를 가진 하나의 배열을 만들어 현재 데이터들의 수를 카운팅하는 알고리줌
    - 특징
        - 특정 조건을 만족하여야 쓸 수 있다.
        - 데이터들은 0이상 이여야 하며 작은 데이터와 큰 데이터의 차이가 극심하게 차이가 나면 성능이 매우 떨어져 쓸 수 없다.(보통 1,000,000 이 넘지 않을 때 효율적)
        - 일반 정렬들과 달리 데이터들을 교환하는 정렬 알고리즘이 아니며 데이터들의 존재 유무로 정렬한다.
    - 시간 복잡도
     - 최악: O(N + K)
