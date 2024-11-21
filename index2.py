import requests
from bs4 import BeautifulSoup

def extract_email(url):
    """Hàm trích xuất email từ một URL LinkedIn"""

    try:
        response = requests.get(url)
        response.raise_for_status()  # Kiểm tra xem có lỗi xảy ra không

        soup = BeautifulSoup(response.text, 'html.parser')

        # Tìm tất cả các thẻ <a> có thuộc tính href bắt đầu bằng "mailto:"
        email_elements = soup.find_all('a', href=lambda href: href and href.startswith('mailto:'))

        if email_elements:
            email = email_elements[0].get('href')[7:]  # Loại bỏ "mailto:"
            print("Email:", email)
        else:
            print("Không tìm thấy email.")

    except requests.exceptions.RequestException as e:
        print(f"Lỗi khi truy cập URL: {e}")

# Nhập URL LinkedIn
url = input("Nhập URL LinkedIn: ")

extract_email(url)