from playwright.sync_api import sync_playwright

def run():
    with sync_playwright() as p:
        # Khởi tạo trình duyệt Chromium
        browser = p.chromium.launch(headless=False)  # headless=False để thấy trình duyệt
        page = browser.new_page()

        # Truy cập trang https://demoqa.com/checkbox
        page.goto("https://demoqa.com/checkbox")

        # Mở thư mục "Home" mà không cần phải check vào
        page.click('text=Home')  # Mở thư mục "Home"

        # Chọn checkbox "Desktop"
        page.check('input[type="checkbox"][value="desktop"]')  # Sử dụng selector đúng cho Desktop

        # Mở thư mục con của "Desktop"
        page.click('text=Desktop')  # Mở thư mục con của "Desktop"

        # Đảm bảo rằng checkbox con "Notes" đã được chọn
        notes_checkbox_checked = page.is_checked('input[type="checkbox"][value="notes"]')
        print("Notes Checkbox Checked:", notes_checkbox_checked)

        # Đóng trình duyệt
        browser.close()

if __name__ == "__main__":
    run()
