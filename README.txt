BÁO CÁO THỰC HÀNH BUỔI 1: LẬP TRÌNH PYTHON VỚI GIAO THỨC MQTT

1. BROKER SỬ DỤNG:
- Public Broker: broker.hivemq.com
- Port: 1883

2. CÁCH CHẠY TỪNG CHƯƠNG TRÌNH:

Bài 1: Gửi và nhận thông điệp cơ bản
- Chạy Subscriber: python3 "Bài 1. Ứng dụng gửi và nhận thông điệp MQTT cơ bản/subscriber_bai1.py"
- Chạy Publisher: python3 "Bài 1. Ứng dụng gửi và nhận thông điệp MQTT cơ bản/publisher_bai1.py"

Bài 2: Cảm biến nhiệt độ và độ ẩm
- Chạy Monitoring: python3 "Bài 2. Mô phỏng cảm biến nhiệt độ và độ ẩm bằng MQTT/monitor_subscriber_bai2.py"
- Chạy Sensor: `python3 "Bài 2. Mô phỏng cảm biến nhiệt độ và độ ẩm bằng MQTT/sensor_publisher_bai2.py"`

Bài 3: Điều khiển đèn thông minh
- Chạy Thiết bị: python3 "Bài 3. Mô phỏng hệ thống điều khiển đèn thông minh qua MQTT/device_bai3.py"
- Chạy Controller: python3 "Bài 3. Mô phỏng hệ thống điều khiển đèn thông minh qua MQTT/controller_bai3.py"

3. KẾT QUẢ ĐẠT ĐƯỢC:
- Kết nối thành công tới broker.hivemq.com.
- Bài 1: Gửi/nhận thông điệp chứa thông tin sinh viên, mã sinh viên và lời chào đúng định dạng.
- Bài 2: Mô phỏng cảm biến gửi định kỳ JSON chu kỳ 3s, giám sát và cảnh báo ngưỡng thành công.
- Bài 3: Điều khiển 2 chiều giữa Controller và Thiết bị thông qua MQTT topic cmd và status.
