# 📖 Ebook2Pdf

전자책을 자동 캡처하여 PDF로 변환하는 도구

## 📌 소개

Ebook2Pdf는 키보드 자동화와 화면 캡처 기능을 사용하여 **eBook**을 하나의 **PDF** 파일로 변환하는 Python 스크립트입니다.

📌 기능

1. ✅ 지정한 영역을 캡처하여 PNG 파일로 저장

2. ✅ 자동으로 다음 페이지로 이동
   - 본 코드에서는 키보드 우클릭(->) 을 통하여 페이지 이동을 가정

3. ✅ 캡처된 이미지를 PDF로 변환



## ⚡ 설치 및 실행 방법

1️⃣ 환경 설정

Python 3.11버전을 사용하였습니다. 아래 명령어로 필요한 라이브러리를 설치하세요.
~~~bash
pip install requirements.txt
~~~

2️⃣ 실행 방법

필요한 args를 작성해주세요

~~~python
if __name__ == "__main__":
    book_name = "Test"          # 저장될 폴더 및 PDF 이름
    total_page = 100            # 캡처할 총 페이지 수
    bbox = (795, 0, 1765, 1440) # 캡처할 화면 영역 (좌표 : left, top, right, bottom)
    

    k2p = Ebook2Pdf(book_name)
    k2p.work(total_page, bbox)
~~~

## 🚀 실행 예제

pdf로 변환할 ebook을 화면에 띄우고 다음 명령어를 실행합니다.

~~~bash
python main.py
~~~