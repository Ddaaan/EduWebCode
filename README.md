# 전라남도 교육청 설문조사 홈페이지 구축
학생, 학부모, 교직원에 대한 설문조사를 제공하고 관리자가 관리 가능한 웹사이트

  
## 📌기능
< 학생, 학부모, 교직원 >
- 학교 민주주의 관련 이론 제공
- 학생, 학부모, 교직원 별 설문조사
- 공지사항 / 자료실 게시글 조회
- 게시글에 첨부된 파일 다운로드 가능

<br>

< 관리자 (학교별, 지역청별, 본청) >
- 관리자 로그인 기능
- 비밀번호 변경 기능
- 공지사항 / 자료실 게시글 작성
- 게시글 업로드 시 파일 업로드 가능
- 학교별, 지역별, 학교급별 통계 조회 가능
- 문항별, 파트별 통계 조회 가능
- 통계 파일 다운로드 가능

  
## 📌개발환경
Language : Python 3.11.9


Framework : Django


Database : MySQL


Server : Ubuntu + Nginx


## 📌파일구조
/main/templates/~.html : Frontend HTML templates


/main/static/main/css : CSS styles


/main/static/main/js : JavaScript logic


/main/views.py : Backend logic (Python)


/main/urls.py : URL configuration


/main/models.py : Database Architecture


## 📌로직설명
설문조사 결과 저장 : 설문조사를 완료하면 엑셀파일에 결과값이 저장되는 형식 (개개인별 응답 모두 저장 / 학교별 응답 합산 저장)


설문조사 결과파일 다운로드 : 관리자가 파일을 다운로드하면 학생, 학부모, 교직원의 응답 파일이 ZIP 파일 형태로 다운로드


설문조사 결과 통계 보기 : 관리자가 선택한 조건에 해당하는 결과값들을 엑셀파일에서 찾아 통계화시키는 형식
