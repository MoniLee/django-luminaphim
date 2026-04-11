# Hướng Dẫn Sử Dụng Chế Độ Tối/Sáng (Dark/Light Theme)

## 📋 Tổng Quan

Tính năng chế độ tối/sáng đã được thực hiện cho ứng dụng Django LuminaPhim. Người dùng có thể chuyển đổi giữa hai chế độ giao diện:
- **Chế độ Tối (Dark Mode)**: Giao diện tối, tốt cho việc sử dụng vào ban đêm
- **Chế độ Sáng (Light Mode)**: Giao diện sáng, thuận tiện cho việc sử dụng vào ban ngày

## 🎯 Tính Năng Chính

### 1. **Nút Chuyển Đổi (Toggle Button)**
- Vị trí: Thanh điều hướng (header/navbar), bên cạnh nút tìm kiếm
- Biểu tượng: 🌙 (Chế độ tối) / ☀️ (Chế độ sáng)
- Hoạt động: Click vào nút để chuyển đổi giữa hai chế độ

### 2. **Lưu Tùy Chọn**
- Tùy chọn giao diện được lưu trữ trong **LocalStorage** của trình duyệt
- Khi người dùng quay lại trang web, chế độ đã chọn sẽ được tự động áp dụng
- Mỗi thiết bị/trình duyệt có tùy chọn riêng

### 3. **Phát Hiện Tùy Chọn Hệ Thống**
- Nếu người dùng chưa bao giờ chọn một chế độ, ứng dụng sẽ tự động phát hiện cơ chế tối/sáng của hệ thống
- Thích ứng tự động với cài đặt cơ chế tối/sáng của hệ điều hành

### 4. **Chuyển Đổi Mượt Mà (Smooth Transition)**
- Tất cả các màu sắc chuyển đổi với hiệu ứng mượt mà (0.3 giây)
- Không có sự nhấp nháy hoặc chuyển đổi đột ngột

## 📁 Cấu Trúc Tập Tin

### Các tập tin đã thêm:

1. **`static/css/dark-light-theme.css`** (14.9 KB)
   - CSS Variables cho cả hai chế độ tối và sáng
   - Định nghĩa màu sắc cho mọi phần tử giao diện
   - Xử lý chuyển đổi mượt mà

2. **`static/js/theme-toggle.js`** (2.2 KB)
   - JavaScript để xử lý chuyển đổi chế độ
   - Quản lý LocalStorage
   - Phát hiện tùy chọn hệ thống

3. **`templates/main.html`** (cập nhật)
   - Thêm link tới `dark-light-theme.css`
   - Thêm script `theme-toggle.js`

4. **`templates/navbar.html`** (cập nhật)
   - Thêm nút toggle vào header actions

## 🎨 Các Màu Sắc

### Chế độ Tối (Dark Mode)
```
Nền chính: #131720
Nền phụ: #151f30
Văn bản chính: #e0e0e0
Màu nhấn: #2f80ed
```

### Chế độ Sáng (Light Mode)
```
Nền chính: #ffffff
Nền phụ: #f8f9fa
Văn bản chính: #1a1a1a
Màu nhấn: #2f80ed (không đổi)
```

## 🔧 Cách Hoạt Động

### 1. **JavaScript Initialization** (`theme-toggle.js`)
```javascript
// Khi trang tải
1. Kiểm tra LocalStorage để tìm tùy chọn đã lưu
2. Nếu không có, phát hiện cơ chế hệ thống
3. Áp dụng chế độ thích hợp
4. Cập nhật giao diện nút toggle
```

### 2. **CSS Variables** (`dark-light-theme.css`)
```css
/* Định nghĩa các biến cho chế độ tối */
:root {
  --bg-primary: #131720;
  --text-primary: #e0e0e0;
  /* ... */
}

/* Ghi đè biến cho chế độ sáng */
body.light-mode {
  --bg-primary: #ffffff;
  --text-primary: #1a1a1a;
  /* ... */
}
```

### 3. **HTML Structure**
```html
<button class="theme-toggle dark-mode" type="button">
  <span class="theme-toggle-icon"></span>
</button>
```

## 🚀 Cách Sử Dụng

### Cho Người Dùng
1. Tìm nút toggle giao diện (🌙 hoặc ☀️) trên thanh điều hướng
2. Click vào nút để chuyển đổi chế độ
3. Tùy chọn sẽ được tự động lưu

### Cho Developer
Nếu muốn mở rộng tính năng:

1. **Thêm phần tử mới mà cần theme**
   ```css
   .my-element {
     background-color: var(--bg-primary);
     color: var(--text-primary);
   }
   ```

2. **Tùy chỉnh màu sắc**
   - Sửa đổi CSS Variables trong `dark-light-theme.css`
   - Thêm rules mới cho phần tử cụ thể

## 🐛 Khắc Phục Sự Cố

### Giao diện không thay đổi
- Xóa cache của trình duyệt (Ctrl + Shift + Delete)
- Xóa LocalStorage nếu cần (F12 > Application > LocalStorage)

### Chế độ không lưu
- Kiểm tra nếu trình duyệt cho phép LocalStorage
- Đảm bảo `theme-toggle.js` được tải đúng

### Icon không hiển thị
- Đảm bảo hỗ trợ emoji trong trình duyệt
- Kiểm tra font chữ: `'Inter', sans-serif` được tải

## 💾 LocalStorage Keys

Dữ liệu được lưu với key:
```
theme-preference: "dark" hoặc "light"
```

Để xóa tùy chọn trong console:
```javascript
localStorage.removeItem('theme-preference');
```

## 📱 Hỗ Trợ Trình Duyệt

Được hỗ trợ đầy đủ trên:
- Chrome/Edge 90+
- Firefox 88+
- Safari 14+
- Opera 76+

## 🎓 Lưu Ý

- Chế độ được lưu **per device/browser**, không liên kết với tài khoản người dùng
- Nếu cần lưu tùy chọn theo tài khoản, cần lưu vào database
- Tất cả phần tử giao diện sẽ tự động áp dụng CSS Variables

## 📚 Tài Nguyên Bổ Sung

- [CSS Variables Documentation](https://developer.mozilla.org/en-US/docs/Web/CSS/--*)
- [LocalStorage API](https://developer.mozilla.org/en-US/docs/Web/API/Window/localStorage)
- [prefers-color-scheme Media Query](https://developer.mozilla.org/en-US/docs/Web/CSS/@media/prefers-color-scheme)

---

**Phiên bản**: 1.0  
**Ngày tạo**: 2026-04-11  
**Tác giả**: GitHub Copilot
