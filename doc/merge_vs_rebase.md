# merge와 rebase의 차디

## `git merge`

### 기능
- 두 브랜치의 커밋 기록을 **그대로 유지**하면서 병합
- 병합 지점에 새로운 **merge commit**이 생성됨

### 예시
```bash
git checkout main
git merge feature
```
> `main` 브랜치에 `feature` 브랜치를 병합하고, merge 커밋 생성

### 장점
- 이력이 **명확하게 보존**
- 누가 언제 어떤 브랜치를 병합했는지 기록됨
- 협업자 간의 이력 충돌이 적음

---

## `git rebase`

![](https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdna%2FcofZo0%2FbtqBkOJybm6%2FAAAAAAAAAAAAAAAAAAAAAEBWPFdm8E5PpeHrf6lf0R5OD39kfURp0ZCBJ5ken3sG%2Fimg.png%3Fcredential%3DyqXZFxpELC7KVnFOS48ylbz2pIh7yKj8%26expires%3D1753973999%26allow_ip%3D%26allow_referer%3D%26signature%3DiN1tlWGmAMZCir2Yk9phVhR6Qbg%253D)
### 기능
- 현재 브랜치를 기준 브랜치 위로 **재배치**
- 커밋 이력이 마치 **직선처럼 깔끔하게 정리**

### 주의사항
- 커밋의 **해시가 변경**되며, 새로운 커밋으로 다시 작성됨
- 이미 **공유된 브랜치에서 사용 시 충돌 및 혼란** 발생 가능

---

## 협업 시 `merge`를 추천하는 이유

| 항목 | `merge` | `rebase` |
|------|---------|----------|
| 커밋 이력 유지 | O (원본 커밋 유지 + 병합 커밋 생성) | X (커밋 재작성) |
| 협업 안정성 | 높음 | 낮음 (충돌 및 재작성 위험) |
| 히스토리 이해 | 병합 흐름 추적 용이 | 이력은 깔끔하지만 맥락 파악 어려움 |
| 실수 복구 용이성 | 높음 (기록 명확) | 낮음 (이력 변경됨) |
