# DockerHub를 사용하는 이유와 Container Registry 종류

## DockerHub를 사용하는 이유

1. **중앙화된 이미지 저장소**
   - Docker 이미지를 중앙에서 관리하고 배포할 수 있는 가장 널리 사용되는 플랫폼입니다.

2. **배포 및 협업 용이**
   - 공개 저장소를 통해 누구나 접근 가능한 이미지 공유 가능
   - 팀 프로젝트, DevOps 파이프라인에서 손쉽게 통합

3. **CI/CD와 연동**
   - GitHub Actions, GitLab CI, Jenkins 등 다양한 도구와 쉽게 연동

4. **무료 플랜 제공**
   - 개인 개발자 및 소규모 프로젝트에도 적합한 무료 사용 가능

5. **자동 빌드 지원**
   - GitHub에 연동하여 Dockerfile 기반 자동 빌드 가능

---

## Container Registry 종류 (3가지)

| 이름              | 설명                                                                 | 대표 특징                        |
|-------------------|----------------------------------------------------------------------|----------------------------------|
| **DockerHub**     | Docker 공식 이미지 저장소로, 전 세계적으로 가장 널리 사용됨         | 쉬운 접근성, 자동 빌드, 커뮤니티 |
| **GitHub Container Registry** | GitHub의 패키지 레지스트리로, GitHub 리포지토리와 연동 용이 | GitHub Actions와 통합            |
| **Amazon ECR (Elastic Container Registry)** | AWS에서 제공하는 고성능 프라이빗 레지스트리 | IAM 기반 인증, EC2/EKS 통합     |

---
