import requests
from bs4 import BeautifulSoup
import csv
from time import sleep

# Define the list of (a, b) pairs
url_info_list = [
    ("https://www.411reverselookup.ca/People/AB/Calgary/Phone/403-255/", 488),
    ("https://www.411reverselookup.ca/People/AB/Calgary/Phone/403-256/", 712),
    
]

output_csv = "output_links.csv"  # Tên file CSV đầu ra

for a, b in url_info_list:
    number_of_pages = b

    # Mở file CSV để ghi (mở ở chế độ append 'a' thay vì write 'w')
    with open(output_csv, mode='a', newline='') as csv_file:
        # Khởi tạo đối tượng csv.writer
        csv_writer = csv.writer(csv_file)

        # Loại bỏ dòng này nếu bạn không muốn ghi header mỗi lần
        # csv_writer.writerow(['Link'])

        for page_num in range(1, number_of_pages + 1):
            url = f'{a}page_{page_num}/'  # Thay đổi URL

            # 
            # Gửi yêu cầu GET đến trang web
            response = requests.get(url)

            # Kiểm tra xem yêu cầu có thành công không (status code 200)
            if response.status_code == 200:
                # Sử dụng BeautifulSoup để parse nội dung trang web
                soup = BeautifulSoup(response.content, "html.parser")

                # Lấy tất cả các phần tử 'a' với class 'rsslink-m cats-head phone-link'
                link_elements = soup.find_all('a', class_='rsslink-m cats-head phone-link')

                # Extract the links from the 'href' attributes
                links = [link.get('href') for link in link_elements]

                # Ghi các đường link vào file CSV
                for link in links:
                    csv_writer.writerow([link])

                # Thêm một khoảng thời gian delay giữa các yêu cầu để tránh bị chặn
                print(f"done: {page_num} :))")
                sleep(1)
            else:
                print(f"Failed to retrieve the page {page_num}. Status code: {response.status_code}")

            # Thêm thời gian delay giữa các trang để tránh bị chặn
            sleep(1)

    print(f"Crawling completed for {a}. Links are appended to {output_csv}")
