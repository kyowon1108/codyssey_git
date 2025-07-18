# Flask vs Gunicorn의 차이점 및 배포 시 Gunicorn 사용 이유

## Flask와 Gunicorn의 차이

| 항목          | Flask                            | Gunicorn                                    |
|---------------|----------------------------------|---------------------------------------------|
| 역할          | Python 기반 웹 프레임워크        | WSGI(Web Server Gateway Interface) 서버     |
| 주요 기능     | 라우팅, 요청 처리, 개발 서버 제공 | Flask 앱을 WSGI 규격에 맞춰 실행하는 서버  |
| 실행 목적     | 개발 및 테스트 용도               | 운영 환경에서 안정적인 서비스 제공 목적    |
| 동시 처리     | 기본적으로 단일 스레드 처리       | 다중 워커(프로세스)로 동시 요청 처리 가능   |
| 사용 방식     | `python main.py` 또는 `flask run` | `gunicorn main:app`                         |

## Gunicorn을 사용하는 이유 (배포 환경)

- **생산 환경용 서버**: Flask의 기본 개발 서버는 가볍지만 성능이나 안정성 면에서 실환경 배포에 적합하지 않음.
- **멀티 프로세싱**: Gunicorn은 여러 워커를 사용하여 다수의 요청을 동시에 처리 가능.
- **WSGI 서버**: Flask는 WSGI(web server gateway interface) 앱이기 때문에 Gunicorn 같은 WSGI 서버로 실행하는 것이 적합.
- **보안 및 안정성**: Gunicorn은 더 나은 에러 처리와 연결 관리, 보안 측면에서 우수함.

---

# .dockerignore 파일의 역할과 항목별 이유

## .dockerignore

`.dockerignore` 파일은 Docker가 이미지를 빌드할 때, **불필요하거나 민감한 파일/폴더**를 **이미지에 포함하지 않도록 제외**하는 데 사용됨.

- Docker 이미지의 크기 감소
- 빌드 속도 향상
- 민감 정보 보호

## 각 항목을 추가한 이유

| 항목             | 제외 이유 |
|------------------|-----------|
| `.git`           | Git 버전 관리 관련 폴더로, 컨테이너에는 불필요하고 이미지 크기만 키움 |
| `.gitignore`     | Git 무시 설정 파일로, Docker 빌드에는 필요 없음 |
| `.dockerignore`  | 자기 자신이므로 포함할 필요 없음 |
| `Dockerfile`     | 이미지를 만들기 위한 설정 파일 |

---