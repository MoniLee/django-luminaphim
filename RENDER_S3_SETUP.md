# Hướng dẫn: Sửa lỗi ảnh không hiển thị trên Render (Cloudinary)

## 🔍 Nguyên nhân vấn đề

Render sử dụng **hệ thống file tạm thời (ephemeral filesystem)**. Điều này có nghĩa:
- Mỗi khi ứng dụng khởi động lại hoặc redeploy, TẤT CẢ các file được lưu trên disk sẽ **bị xóa**
- Các ảnh movie poster được lưu trong `static/media/` sẽ biến mất
- Đó là lý do vì sao ảnh không hiển thị

## ✅ Giải pháp: Sử dụng Cloudinary

Chúng ta sẽ lưu ảnh trên Cloudinary (lưu trữ đám mây miễn phí). Các bước:

### 1️⃣ Đăng ký Cloudinary (Miễn Phí)

1. Truy cập [https://cloudinary.com](https://cloudinary.com)
2. Click "Sign up for free"
3. Tạo tài khoản (email, password)
4. Xác nhận email
5. Chọn "Media and Bin Management" khi được hỏi

### 2️⃣ Lấy Cloudinary Credentials

Sau khi đăng nhập:

1. Vào **Dashboard** (trang chủ)
2. Cuộn xuống, bạn sẽ thấy **"API Environment variable"**
3. Copy giá trị (nó sẽ như này):
```
cloudinary://123456789:abcdefg_XXXXX@abc123xyz
```

**Tách thông tin từ URL trên:**
- `CLOUDINARY_URL` = cả chuỗi: `cloudinary://123456789:abcdefg_XXXXX@abc123xyz`
- `CLOUDINARY_NAME` = phần sau `@`: `abc123xyz`
- `CLOUDINARY_API_KEY` = phần đầu (trước `:`): `123456789`
- `CLOUDINARY_API_SECRET` = phần giữa (sau `:`): `abcdefg_XXXXX`

### 3️⃣ Thêm Environment Variables trên Render

Trên **Render Dashboard**:

1. Vào service của bạn
2. Chọn **"Environment"**
3. Thêm các biến sau:

```
CLOUDINARY_URL=cloudinary://123456789:abcdefg_XXXXX@abc123xyz
CLOUDINARY_NAME=abc123xyz
CLOUDINARY_API_KEY=123456789
CLOUDINARY_API_SECRET=abcdefg_XXXXX
```

*(Thay bằng giá trị thực tế từ Cloudinary Dashboard)*

4. Click **"Save"**
5. Render sẽ tự động redeploy

### 4️⃣ Deploy

```bash
# Commit và push
git add .
git commit -m "Configure Cloudinary for media storage on Render"
git push
```

Django sẽ tự động sử dụng Cloudinary để lưu ảnh! 🎉

### 5️⃣ Upload lại ảnh cũ (tuỳ chọn)

Nếu muốn ảnh cũ cũng hiển thị:

1. Trong Django admin: `/admin`
2. Chỉnh sửa từng movie/series
3. Upload lại ảnh poster
4. Ảnh sẽ tự động lưu vào Cloudinary

## 📝 Kiểm Tra

Sau khi deploy:

1. Truy cập trang web của bạn
2. Mở DevTools (F12)
3. Tab **Network**
4. Tải trang
5. Ảnh sẽ hiển thị URLs như: `https://res.cloudinary.com/abc123xyz/image/upload/...`

✅ Nếu thấy URL từ Cloudinary → **Thành công!**

## 💰 Chi phí

- **Miễn phí** cho tối đa 25 GB/tháng (đủ cho 99% web project)
- Hình ảnh được nén tự động (giảm dung lượng ~50%)
- Không cần lo về chi phí

## 🆘 Troubleshooting

### Ảnh vẫn không hiển thị?
- Kiểm tra Render logs: xem có error không
- Kiểm tra environment variables có đúng không
- Kiểm tra Cloudinary Dashboard - đã upload được chưa?

### "Unauthorized" error?
- Copy lại credentials từ Cloudinary (có thể sai)
- Lưu ý: bắt buộc phải có `CLOUDINARY_URL`

### Ảnh hiển thị chậm?
- Cloudinary sử dụng CDN, có thể do mạng
- Đợi 5-10 thử lại

---

## 🎯 Tóm tắt (Quick Reference)

| Bước | Hành động |
|------|----------|
| 1 | Đăng ký Cloudinary miễn phí |
| 2 | Copy `CLOUDINARY_URL` từ Dashboard |
| 3 | Thêm environment variables vào Render |
| 4 | Commit & Push |
| 5 | Render redeploy tự động ✅ |

**Xong! Ảnh sẽ hiển thị ngay lập tức! 🚀**

