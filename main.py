from pynput.keyboard import Controller, Key
from PIL.ImageGrab import grab
from PIL import Image
import random
import time, os


class Ebook2Pdf:
    def __init__(self, book_name: str) -> None:
        """
        Args:
            book_name (str): 책 이름
        """
        self.book_name = book_name
        self.keyboard = Controller()

    def make_folder(self) -> None:
        """책 이름의 폴더를 생성"""
        if not os.path.exists(self.book_name):
            os.mkdir(self.book_name)

    def screen_capture(self, bbox: tuple[int], name: str) -> None:
        """bbox 정보를 바탕으로 화면은 캡처하고 책 이름 폴더에 name 이름으로 화면 저장

        Args:
            bbox (tuple[int]): left, top, right, bottom의 화면 위치 정보
            name (str): 캡처한 스크린을 저장할 파일명
        """
        screenshot = grab(bbox)
        screenshot.save(name)

    def next_page(self) -> None:
        """오른쪽 방향키를 누름으로써 ebook 다음페이지 이동"""
        self.keyboard.press(Key.right)
        time.sleep(random.uniform(0.25, 0.75))
        self.keyboard.release(Key.right)

    def png2pdf(self, total_page: int) -> None:
        """캡처하여 변환된 png 파일을 pdf로 변환

        Args:
            total_page (int): 캡처를 수행한 총 페이지수
        """

        output_pdf = f"{self.book_name}.pdf"
        image_list = [Image.open(os.path.join(self.book_name, f"{i}.png")).convert("RGB") for i in range(total_page)]
        image_list[0].save(output_pdf, save_all=True, append_images=image_list[1:])
        print(f"✅ PDF 변환 완료: {output_pdf}")

    def work(self, total_page: int, bbox: tuple[int]) -> None:
        """3초의 대기시간 이후 total_page 수만큼 (book_name 폴더에 화면을 캡처하여 저장 후 다음페이지로 이동)

        Args:
            total_page (int): 캡처를 수행해야할 총 페이지수
            bbox (tuple[int]): left, top, right, bottom의 화면 위치 정보
        """
        self.make_folder()
        time.sleep(3)
        for idx in range(total_page):
            self.screen_capture(bbox, os.path.join(self.book_name, f"{idx}.png"))
            self.next_page()
            time.sleep(random.uniform(1.5, 3))
        self.png2pdf(total_page)


if __name__ == "__main__":
    book_name = "Test"
    total_page = 100
    bbox = (795, 0, 1765, 1440)

    k2p = Ebook2Pdf(book_name)
    k2p.work(total_page, bbox)
