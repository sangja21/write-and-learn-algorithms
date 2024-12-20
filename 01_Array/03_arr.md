# 1.3 두 수의 합 찾기

## **문제 설명**
주어진 정수형 배열에서 두 숫자를 선택하여 더한 값이 **특정 목표값(Target)**을 만들 때, 선택한 두 숫자가 있는 **배열의 인덱스**를 반환하는 프로그램을 작성하시오.

- **제약 조건**  
  1. 입력 배열에는 **정확히 하나의 정답**이 존재합니다.
  2. 같은 요소의 값을 **중복해서 사용할 수 없습니다**.

---

## **입력값**
- `num = [2, 7, 10, 19]`
- `target = 9`

---

## **출력값**
- `[0, 1]`

---

## **예제 설명**
입력 배열 `num`에서 2와 7을 선택하면, 두 수의 합은 목표값 9와 일치합니다. 따라서 2와 7의 인덱스 `[0, 1]`을 반환합니다.

---
## 접근방법

**제한사항(Constraints)**
1. 정수형 배열
2. 두 수의 합이 정수형을 초과할 수 있는가?
 - 문제에 언급이 없다.
 3. 두 수의 합의 값이 배열 내에 무조건 존재하는가?
 - 무조건 정확히 하나의 해결책이 존재한다.
 4. 중복된 요소의 값을 2번 이상 사용하여 결괏값을 만들어서는 안된다.

 **아이디어(Ideas)**
 1. 배열의 모든 요소의 조합을 찾는다.
 - 루프는 i=0 ~ n, j = i + 1 ~n 으로 2 중 루프를 구성한다.
 - 1번째 루프(n 번), 2번째 루프는 (n-1)을 기준으로 n*(n-1)로 계산하자.
 2. 해당 조합으로 목푯값(target)과 비교하여 같다면
 - 해당 루프를 종료하고 각 값을 가진 인덱스를 반환한다.

시간복잡도 : O(n^2)
공간복잡도 : O(1)

``` python
for i in range(0, len(nums)):
  for j in range(i+1, len(nums)):
    if(nums[i] + nums[j]) is target:
      return[i, j]
```

**아이디어(Ideas)**
1. 해시 테이블을 구성한다.
- 키값으로는 배열의 요소, 값으로는 요소의 인덱스로 구성
2. 각 요소를 순회하면서,
- 목푯값 - 현재 요소 = 다른 요소
- 해시 테이블에서 다른 요소의 값을 찾는다.
- 만약 다른 요소가 해시 테이블에 있다면, 현재 요소의 인덱스와 해시 테이블의 값(인덱스)을 반환한다.
- 다른 요소가 없다면, 현재 요소를 해시 테이블의 키값으로 넣고 인덱스를 해시 테이블의 값 항목으로 추가한다.
