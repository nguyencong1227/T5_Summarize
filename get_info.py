import requests
from bs4 import BeautifulSoup
import csv
import pandas as pd
from time import sleep
for i in range(223, 258):

    # Đọc các đường link từ file CSV
    with open(f"./output_files/output_{i}.csv", "r") as file:
        links = [line.strip() for line in file]

    # Tạo danh sách để lưu thông tin
    data = []
    k=1
    for link in links:
        # Gửi yêu cầu GET đến trang web
        response = requests.get(link)

        # Kiểm tra xem yêu cầu có thành công không (status code 200)
        if response.status_code == 200:
            # Sử dụng BeautifulSoup để parse nội dung trang web
            soup = BeautifulSoup(response.content, "html.parser")

            # Lấy số điện thoại
            phone_number = soup.find("input", {"id": "search-input"})["value"]

            # Lấy tên và địa chỉ
            name = soup.find("span", itemprop="name").get_text(strip=True)
            address_street = soup.find("span", itemprop="streetAddress").get_text(strip=True)
            address_locality = soup.find("span", itemprop="addressLocality").get_text(strip=True)
            address_region = soup.find("span", itemprop="addressRegion").get_text(strip=True)
            postal_code = soup.find("span", itemprop="postalCode").get_text(strip=True)

            # Kết hợp thông tin địa chỉ
            full_address = f"{address_street}, {address_locality}, {address_region} {postal_code}"

            # Thêm thông tin vào danh sách
            data.append({"Tên": name, "Địa chỉ": full_address, "Số điện thoại": phone_number})

            # Thêm thời gian delay giữa các yêu cầu để tránh bị chặn
 #           sleep(1)
            print(f'done: {k}')
            k = k+1
        else:
            print(f"Failed to retrieve the page {link}. Status code: {response.status_code}")

    # Tạo DataFrame từ danh sách thông tin
    df = pd.DataFrame(data)

    # Lưu vào file Excel
    df.to_excel(f"output_info{i}.xlsx", index=False)

    print("Crawling and saving completed.")
