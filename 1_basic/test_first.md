# 19 - 05 - 27  기초 설치 및 사용법 학습

## markdown 작성하기

### 제목 작성

제목은, Semantic하게 작성한다.

### 나열(리스트 )작성하기

#### 순서가있는 리스트

1. WeMakeO app 을 받는다.
2. 회원가입한다
3. W카페를 찾는다.
4. 커피를 주문한다.
5. 알림이 오면 픽업하러 간다....

#### 순서가 없는 리스트

* 파이썬 설치하기
  * 3.7
  * 3.6

* 타이포라 설치하기

* Git 설치하기

   

### 일반 문단 작성하기

오늘 점심은 무엇일까요?

### 코드 블럭 작성하기

터미널에서 `Python -e` 이라고 입력하면, **코드가 실행**됩니다.

```python
def index():
	return 'hi'
	
def create():
    save()
```

### 설정 단축키

ctrl + ,

### 수식 작성하기

 ctrl + shift + m


$$
f(X) =
$$



### table 생성

ctrl + t

| title | content | decs       | a    | b    | c     | e    |
| ----- | ------- | ---------- | ---- | ---- | ----- | ---- |
| row를 | 추가    | 하고싶으면 | ctrl | +    | enter |      |
|       |         |            |      |      |       |      |

## CLI - terminer 명령어 학습

```sh
$ touch a.txt # a.txt 를 생성한다.
$ mkdir test # test 폴더/디렉토리를 생성한다. Make DIRectory
$ cd test # test 디렉토리로 이동한다. Change DIRectory
$ cd .. # 상위 디렉토리로 이동한다.
$ cd or cd ~ # home 디렉토리로 이동한다.
$ cd - # 뒤로가기.
$ cd / # root(최상단) 디렉토리로 이동한다.
$ rm a.txt # a.txt를 삭제한다. ReMove
$ rm -r test/ # test 디렉토리를 삭제한다.
$ ls # LiSt 현재 디렉토리 안의 목록 (파일/디렉토리)을 표시한다.
$ pwd # 현재 내가 위치한 디렉토리를 표시한다. Present Working Diretory.
```

### git 기초명령

```sh
$ git init # 관리자 추가 - #pwd에서 git으로 버전관리 시작! (.git/을 만든다.)
$ git remote add origin <remote url> # 드라이브 등록
## 여기 까지는 한번만 ##
$ git add . # 내 위치(.) 를 전체 등록 (사진 찍을 준비)
$ git commit -m 'MESSAGE'# 사진찰칵 + 메시지
## 계속 반복! add & commit ##
$ git push origin master # 드라이브 백업
```

