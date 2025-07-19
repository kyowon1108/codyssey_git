# 리눅스 컨테이너 실행: Linux vs Windows vs macOS

## 리눅스 컨테이너
- **리눅스 커널을 기반으로 하는 경량 가상화 기술** 
- 가장 대표적인 예시가 Docker
---

## 운영체제별 리눅스 컨테이너 실행 차이

| 운영체제 | 실행 방식 | 커널 | 추가 요구 사항 |
|----------|-----------|------|----------------|
| **Linux** | **네이티브 실행** | 리눅스 | 없음 |
| **Windows** | 가상화 기반 실행 (WSL2 or Hyper-V) | 윈도우 커널 (리눅스 아님) | **WSL2 필요** |
| **macOS** | 가상화 기반 실행 (Apple Hypervisor) | macOS 커널 (Darwin) | **Docker Desktop 필요** |

---

## 왜 Windows에서 WSL2가 필요한가?

### Windows는 리눅스 커널이 아님
- 리눅스 컨테이너는 리눅스 커널 기능에 의존
- Windows 커널은 이를 **직접 지원하지 않음**

### 이때의 해결책 : **WSL2**
- WSL2(Windows Subsystem for Linux v2)는 **경량 리눅스 VM**을 제공
- 리눅스 컨테이너를 이 VM 위에서 실행할 수 있음

### 장점
- 기존보다 훨씬 빠른 파일 시스템 접근 속도
- 네이티브처럼 도커 실행 가능 (Docker Desktop + WSL2)

---

## Windows에서 리눅스 컨테이너 실행 구조

```text
[ Windows ]
     │
     └── Docker Desktop
           │
           └── WSL2 (리눅스 VM)
                 └── Docker Engine (리눅스 커널 기반)
                       └── 리눅스 컨테이너
