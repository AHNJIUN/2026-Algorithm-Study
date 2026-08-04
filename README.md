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
프로그래머스에서 문제를 풀고 통과하면 코드와 문제 요약이 **본인 개인 저장소에 자동 커밋**되고,
개인 저장소의 GitHub Actions가 유형별로 분류한 뒤 팀 저장소로 자동 전송함.
 
> 문제 풀기 → 개인 저장소에 자동 커밋 → 유형별 자동 분류 → 팀 저장소로 자동 전송

백준허브는 **본인 계정 소유의 저장소**에만 연동 가능함.
팀 저장소(Organization 소유)나 fork에는 자동 커밋이 되지 않아서,
각자 개인 저장소를 중간 다리로 쓰는 구조임.
 
#### **1. 개인 저장소 생성**
 
1. GitHub 우측 상단 `+` → `New repository`
2. 이름은 자유 (예: `algorithm-study`). **Private 가능**
3. `Add a README file` 체크 후 생성 (빈 저장소면 백준허브 첫 푸시가 실패할 수 있음)

#### **2. 개인 저장소 Actions 쓰기 권한 켜기**
 
1. **개인 저장소** → `Settings` → `Actions` → `General`
2. 맨 아래 **Workflow permissions** 에서 **`Read and write permissions`** 선택 → `Save`

#### **3. 백준허브 설치 및 연동**
 
1. 크롬 웹스토어에서 [백준허브](https://chromewebstore.google.com/detail/ccammcjdkpgjmcpijpahlehmapgmphmk) 설치
2. 확장 팝업 → `Authenticate with GitHub` → 인증
3. `내 저장소 연결하기` 선택 → `플랫폼별로 정리` 선택 → **1번에서 만든 개인 저장소 이름** 입력
4. 하단 `저장 경로 템플릿` 펼치기
5. **프로그래머스** 칸에 아래 내용을 입력하고 `저장`

```
    Programmers/${level}/${id}. ${title}
```
 
- **전원 동일하게 입력함. 본인 이름을 넣지 않음.**
  (이름은 다음 단계의 전송 스크립트가 자동으로 붙여줌.)
- `${level}`, `${id}`, `${title}` 은 **그대로** 입력. 백준허브가 알아서 치환함.

#### **4. 팀 저장소 접근 토큰 발급**
 
1. GitHub 우측 상단 프로필 → `Settings` → 좌측 맨 아래 `Developer settings`
2. `Personal access tokens` → `Fine-grained tokens` → `Generate new token`
3. 아래와 같이 설정 후 생성
    - Token name: 자유 (예: `algo-study-sync`)
    - **Resource owner: `TeamAlgoco`** ← 본인 계정이 아니라 Organization 선택. 여기가 제일 중요함
    - Expiration: 스터디 종료 이후 날짜로 설정
    - Repository access: `Only select repositories` → `2026-Algorithm-Study`
    - Permissions → Repository permissions → **`Contents`: `Read and write`**
4. 생성된 토큰(`github_pat_...`)을 복사해둠.
5. Resource owner를 Organization으로 선택하면 토큰이 **승인 대기** 상태일 수 있음.
   메인 관리자([@sdoubleoj](https://github.com/sdoubleoj))에게 승인 요청하기

#### **5. 개인 저장소에 토큰 등록**
 
1. **개인 저장소** → `Settings` → `Secrets and variables` → `Actions`
2. `New repository secret` 클릭
3. Name: `TEAM_REPO_PAT` / Secret: 3번에서 복사한 토큰 → `Add secret`

#### **6. 개인 저장소에 자동 분류 및 전송 워크플로우 추가**
 
1. **개인 저장소** Code 탭 → `Add file` → `Create new file`
2. 파일 경로에 `.github/workflows/classify-and-sync.yml` 입력 (슬래시 입력 시 폴더 자동 생성)
3. 아래 내용을 통째로 붙여넣되, **`MY_NAME` 값만 본인 영문 이름으로 수정**
4. `Commit changes`

```yaml
name: Classify and sync

permissions:
  contents: write

env:
  MY_NAME: sujeong   # ⬅️ 본인 영문 이름으로 수정 (팀 저장소 폴더명으로 사용됨)

on:
  push:
    branches: [main]
    paths: ['Programmers/**']

concurrency:
  group: classify-and-sync
  cancel-in-progress: false

jobs:
  classify-and-sync:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
        with: { path: solo, fetch-depth: 2 }

      - uses: actions/setup-python@v5
        with:
          python-version: '3.x'

      - name: Classify by category
        run: |
          cd solo
          python - << 'EOF'
          import os, re, shutil
          BASE = 'Programmers'
          LEVEL = re.compile(r'^\d+$|^unrated$', re.IGNORECASE)
          CATEGORY = re.compile(r'코딩테스트\s*연습\s*>\s*([^>\n]+)')
          def sanitize(name):
              return name.strip().replace('/', '-').replace('\\', '-')
          if not os.path.isdir(BASE):
              print(f'{BASE} 폴더가 없습니다.'); raise SystemExit(0)
          moved = 0
          for level in os.listdir(BASE):
              level_path = os.path.join(BASE, level)
              if not os.path.isdir(level_path) or not LEVEL.match(level):
                  continue
              for problem in os.listdir(level_path):
                  problem_path = os.path.join(level_path, problem)
                  if not os.path.isdir(problem_path):
                      continue
                  category = 'Unclassified'
                  readme = os.path.join(problem_path, 'README.md')
                  if os.path.exists(readme):
                      with open(readme, encoding='utf-8') as f:
                          m = CATEGORY.search(f.read())
                      if m:
                          category = sanitize(m.group(1))
                  dest = os.path.join(BASE, category, problem)
                  os.makedirs(os.path.dirname(dest), exist_ok=True)
                  if os.path.exists(dest):
                      shutil.rmtree(dest)
                  print(f'이동: {problem_path} -> {dest}')
                  shutil.move(problem_path, dest)
                  moved += 1
              if os.path.isdir(level_path) and not os.listdir(level_path):
                  os.rmdir(level_path)
          print(f'총 {moved}개 문제 분류 완료')
          EOF

      - name: Commit classification to personal repo
        run: |
          cd solo
          git config user.name  "github-actions[bot]"
          git config user.email "github-actions[bot]@users.noreply.github.com"
          git add -A
          if ! git diff --staged --quiet; then
            git commit -m "chore: 프로그래머스 문제 자동 분류 완료 [skip ci]"
            git pull --rebase origin main
            git push origin main
          else
            echo "분류 변경 사항이 없습니다."
          fi

      - uses: actions/checkout@v4
        with:
          repository: TeamAlgoco/2026-Algorithm-Study
          token: ${{ secrets.TEAM_REPO_PAT }}
          path: team

      - name: Copy solutions
        run: |
          mkdir -p "team/Programmers/${MY_NAME}"
          rsync -a --exclude '.git' solo/Programmers/ "team/Programmers/${MY_NAME}/"

      - name: Commit and push to team repo
        run: |
          CHANGED=$(cd solo && git log --diff-filter=A --name-only --pretty="" -5 -- 'Programmers/**' \
                    | grep -v 'README.md' | head -1)
          ID=$(echo "$CHANGED"    | sed -n 's#.*/\([0-9]*\)\. \([^/]*\)/.*#\1#p')
          TITLE=$(echo "$CHANGED" | sed -n 's#.*/\([0-9]*\)\. \([^/]*\)/.*#\2#p')
          cd team
          git config user.name  "${{ github.actor }}"
          git config user.email "${{ github.actor }}@users.noreply.github.com"
          git add -A
          git diff --staged --quiet && { echo "변경 없음"; exit 0; }
          git commit -m "[Programmers-${ID:-0000}] ${TITLE:-solution}"
          git pull --rebase origin main
          git push origin main
```

#### **7. 동작 확인**
 
프로그래머스에서 문제 하나를 풀어 제출한 뒤, 순서대로 확인:
 
1. **개인 저장소** Code 탭에 `Programmers/{유형}/{문제번호}. {문제명}/` 생성됨
   (백준허브가 올린 직후엔 `Programmers/{레벨}/...` 였다가 잠시 후 유형 폴더로 정리됨)
2. **개인 저장소** Actions 탭에서 `Classify and sync` 초록불
3. **팀 저장소**에 `[Programmers-문제번호] 문제명` 커밋 추가됨
4. 팀 저장소 Code 탭에 `Programmers/{내이름}/{유형}/{문제번호}. {문제명}/` 생성 → 성공!

#### **주의 사항**
 
- 저장 경로 템플릿(3-5번)에 **이름을 넣지 말 것**. 이름은 `classify-and-sync.yml`의 `MY_NAME` 한 곳에서만 지정함.
- Actions가 `exit code 128` 로 실패하면 **2번(쓰기 권한)** 설정을 빠뜨린 것.
- 템플릿은 브라우저에 저장되는 값임. **PC나 크롬 프로필이 바뀌면 다시 설정**해야 함.
- 팀 저장소를 clone 할 필요 없음. 모든 전송은 자동임.
- 토큰이 만료되면 전송이 실패함(개인 저장소 Actions에 빨간불).
  4~5번 절차로 재발급해서 시크릿 값만 교체하면 됨.
- `classify-and-sync.yml` 수정 커밋으로는 워크플로우가 실행되지 않음(`Programmers/` 변경에만 반응).
  수정 후에는 Actions 탭에서 `Re-run jobs` 하거나 문제를 새로 제출해서 확인.

> 백준허브 연동 및 자동 분류 워크플로우는 [@SamK5678](https://github.com/SamK5678) 님이 구축해주셨습니다🥹

# 스터디 규칙

---

#### **문제 풀이**

1. 1일 1문풀
2. 주마다 5문제씩 선정해서 문제 풀이를 진행함. 회의 시간에는 각자 1문제 풀이 설명.
    1. 개념+알고리즘+풀이 방식 자세하게 설명하기.
    2. 만약 상대가 이해 못하면 이해할 때까지 설명해야 함.
3. 깃허브에 올라온 서로의 코드에 리뷰를 진행함.
    1. 팀 저장소에서 상대방의 커밋 또는 파일에 코멘트를 달아 리뷰함.
    2. 서로에 대한 코드 리뷰는 금요일까지 완료하기.
4. 코드 리뷰 받은 것에 대해서는 다음 회의 전까지 수정해서 다시 깃허브에 올리기.
   (같은 문제를 다시 제출하면 자동으로 최신 코드로 교체됨)

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

## **Commit Message 규칙**

---

- [Programmers-문제번호] 문제명
- 자동 전송되는 커밋은 위 형식으로 자동 생성됨.
  직접 커밋할 일이 있을 때(README 수정 등)만 신경 쓰면 됨.

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
