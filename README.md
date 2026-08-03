# 2026-Algorithm-Study

- 기간: 2026.08.04(화) ~ 2026.10.12(일) (총 10주)
- 정기 회의: 토요일 20시 비대면
- 플랫폼: 프로그래머스
- 언어: 각자 알아서
- 학습 소스: 각자 알아서
    - 참고
        - [이코테](https://github.com/ndb796/python-for-coding-test)
        - [큰돌 아저씨 인프런 강의](https://www.inflearn.com/course/10%EC%A3%BC%EC%99%84%EC%84%B1-%EC%BD%94%EB%94%A9%ED%85%8C%EC%8A%A4%ED%8A%B8-%ED%81%B0%EB%8F%8C?cid=326485&srsltid=AfmBOopuYg2CWVWd8DDa_f46872myZxhjez9Nz--P0kaYsh_8p4Z0hah)

# '백준허브' 세팅 (최초 1회 필수)
 
---
 
이 저장소는 **백준허브(BaekjoonHub)** 크롬 확장으로 풀이를 자동 업로드함.
프로그래머스에서 문제를 풀고 통과하면 코드와 문제 요약이 **내 fork에 자동 커밋**되고,
GitHub Actions가 유형별로 폴더를 정리해줌.
 
> 문제 풀기 → 내 fork에 자동 커밋 → 자동 분류 → 주 1회 PR → 리뷰 → main 머지

백준허브는 **본인 계정 소유의 저장소**에만 연동할 수 있어서, 팀 저장소에 직접 연결되지 않음.
그래서 각자 fork를 하나씩 만들어 쓰는 구조.
 
#### **1. 저장소 Fork**
 
이 저장소 페이지 우측 상단의 **Fork** 버튼 클릭.
본인 계정에 `{본인_아이디}/2026-Algorithm-Study` 생성.
 
#### **2. fork에서 Actions 활성화**
 
fork한 저장소의 **Actions** 탭으로 이동해
`I understand my workflows, go ahead and enable them` 버튼을 한 번 눌러줌.
이걸 안 하면 자동 분류가 동작하지 않음.
 
#### **3. 백준허브 설치 및 연동**
 
1. 크롬 웹스토어에서 [백준허브](https://chromewebstore.google.com/detail/ccammcjdkpgjmcpijpahlehmapgmphmk) 설치
2. 확장 팝업 → `Authenticate with GitHub` → 인증
3. `내 저장소 연결하기` 선택 → '플랫폼별로 정리' 선택 -> `2026-Algorithm-Study` 입력(본인 fork가 연결됨)
4. 하단 `저장 경로 템플릿` 펼치기
5. **프로그래머스** 칸에 아래 내용을 입력하고 `저장`

```
    Programmers/{본인_영문_이름}/${level}/${id}. ${title}
```
 
- `{본인_영문_이름}` 부분만 자기 이름으로 바꿈. (예: `Programmers/sujeong/...`)
- `${level}`, `${id}`, `${title}` 은 **그대로** 입력. 백준허브가 알아서 치환함.
 
6. 프로그래머스에서 문제 하나를 풀어 제출한 뒤,
내 fork의 **Actions** 탭에서 `Auto Classify Programmers Problems` 실행이 초록불인지 확인하기.
Code 탭에 `Programmers/{이름}/{유형}/{문제번호}. {문제명}/` 이 생겼으면 성공.

#### **4. 팀 저장소에 올리기 (주 1회)**
 
1. 내 fork 페이지에서 `Contribute` → `Open pull request`
2. base 저장소가 `TeamAlgoco/2026-Algorithm-Study` 의 `main` 인지 확인
3. PR 제목은 아래 컨벤션에 맞춰 작성 → `Create pull request`
4. 리뷰 후 머지되면, fork 페이지의 **`Sync fork`** 버튼으로 최신 main을 내 fork에 반영

#### **주의 사항**
 
- 3.5번 템플릿 설정을 빠뜨리면 자동 분류가 되지 않고 Actions 로그에 경고가 남음.
  파일이 엉뚱한 곳에 있다면 이 설정부터 확인.
- 템플릿은 브라우저에 저장되는 값임. **PC나 크롬 프로필이 바뀌면 다시 설정**해야 함.
- 저장소를 clone 할 필요 없음. 백준허브는 GitHub API로 직접 푸시함.
- 자동 분류 워크플로우는 `.github/workflows/classify-programmers.yml` 에 있음.
  건드리면 전원의 자동화가 깨지니 수정이 필요하면 논의 요청 바람.

> 백준허브 연동 및 자동 분류 워크플로우는 [@SamK5678](https://github.com/SamK5678) 님이 구축해주셨습니다🥹

# 스터디 규칙

---

#### **문제 풀이**

1. 1일 1문풀
2. 주마다 5문제씩 선정해서 문제 풀이를 진행함. 회의 시간에는 각자 1문제 풀이 설명.
    1. 개념+알고리즘+풀이 방식 자세하게 설명하기.
    2. 만약 상대가 이해 못하면 이해할 때까지 설명해야 함.
3. 깃허브 활용해서 Pull Request로 코드 리뷰 진행함.
    1. 주 1회, 본인 fork에서 팀 저장소로 PR을 올림.
    2. 서로에 대한 코드 리뷰는 금요일까지 완료하기.
    3. 반드시 코드 리뷰 후에 main branch로 merge.
4. 코드 리뷰 받은 것에 대해서는 다음 회의 전까지 수정해서 다시 깃허브에 올리기.

#### **설명 방식**

1. 적용 알고리즘 개념 간단하게 설명하기
2. 문제 풀이를 위한 접근 방식(or 개념) 설명
3. 기본 코드에 대한 설명
4. 추가적으로 개선한 코드에 대한 설명
5. 시간 복잡도, 공간 복잡도 계산 (어려우면 실행 시간 캡처로 대체)
6. 사용 라이브러리 정리
7. 기타(문제 풀이에 어려웠던 점, 구현하고자 했는데 실패한 방식)

#### **진행 방식**

- 만약 주차에 해당하는 문제 풀이가 미완료 시, 회의 당일에 직접 문제 풀이 진행해야 함.
- 끝날 때까지 회의는 끝나지 않음.…

## **PR 규칙 및 Commit Message 규칙**

---

#### **Pull Request**

- [Programmers-폴더명] 이름

#### **Commit Message**

- [Programmers-문제번호] 문제명
- 백준허브가 올리는 커밋 메시지는 자동 생성되므로 이 규칙의 대상이 아님.
  직접 커밋할 때만 위 형식을 지킴.

## **파일 및 폴더 구조**

---

#### **프로그래머스**

- Programmers/각자이름/유형/문제번호. 문제명/문제명.확장자

```
Programmers/
└── sujeong/
    └── 스택-큐/
        └── 42586. 기능개발/
            ├── 기능개발.py
            └── README.md      # 문제 설명·성능 요약 (백준허브 자동 생성)
```

- `유형` 폴더는 프로그래머스의 문제 분류를 기준으로 자동 생성됨.
  경로에 쓸 수 없는 `/` 는 `-` 로 치환. (`스택/큐` → `스택-큐`)
- 분류를 찾지 못한 문제는 `Unclassified` 폴더로 들어감.

## **일정표**

---

| 주차 | 기간 | 폴더명/문제1 | 폴더명/문제2 | 폴더명/문제3 | 폴더명/문제4 | 폴더명/문제5 |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | 08/04 ~ 08/07 | [stack_queue/기능개발](https://school.programmers.co.kr/learn/courses/30/lessons/42586) | [dfs_bfs/게입 맵 최단거리](https://school.programmers.co.kr/learn/courses/30/lessons/1844) | [sort/가장 큰 수](https://school.programmers.co.kr/learn/courses/30/lessons/42746) | [dfs_bfs/타겟넘버](https://school.programmers.co.kr/learn/courses/30/lessons/43165) |  |
| 2 | 08/10 ~ 08/14 |  |  |  |  |  |
| 3 | 08/17 ~ 08/21 |  |  |  |  |  |
| 4 | 08/24 ~ 08/28 |  |  |  |  |  |
| 5 | 08/31 ~ 09/04 |  |  |  |  |  |
| 6 | 09/07 ~ 09/11 |  |  |  |  |  |
| 7 | 09/14 ~ 09/18 |  |  |  |  |  |
| 8 | 09/21 ~ 09/25 |  |  |  |  |  |
| 9 | 09/28 ~ 10/02 |  |  |  |  |  |
| 10 | 10/05 ~ 10/09 |  |  |  |  |  |

> 일정표의 `폴더명`은 문제 선정용 표기.
> 실제 저장소 폴더는 프로그래머스 분류를 따라 한글로 자동 생성됨.
