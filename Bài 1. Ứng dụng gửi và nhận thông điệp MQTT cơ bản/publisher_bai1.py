import time
from datetime import datetime
import paho.mqtt.client as mqtt

# ==========================================================
# CẤU HÌNH MQTT BROKER
# ==========================================================
BROKER = "broker.hivemq.com"
PORT = 1883
TOPIC = "iot/lab/message"

# ==========================================================
# THÔNG TIN SINH VIÊN & THÔNG ĐIỆP
# ==========================================================
STUDENT_NAME = "Nguyen Cong Hai Nam"
STUDENT_ID = "B23DCCN583"  # Bạn có thể thay đổi mã sinh viên tại đây
GREETING = "Xin chao tu client Python MQTT"

# Khởi tạo MQTT Client (hỗ trợ tương thích cả paho-mqtt phiên bản 1.x và 2.x)
if hasattr(mqtt, "CallbackAPIVersion"):
    client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION1)
else:
    client = mqtt.Client()

try:
    # Kết nối tới Broker
    print(f"Đang kết nối tới MQTT Broker: {BROKER}:{PORT}...")
    client.connect(BROKER, PORT, keepalive=60)
    print(f"-> Đã kết nối thành công tới broker {BROKER}!\n")

    print("=" * 60)
    print("CHƯƠNG TRÌNH PUBLISHER - BÀI 1: GỬI THÔNG ĐIỆP MQTT")
    print(f"Topic: {TOPIC}")
    print(f"Sinh viên: {STUDENT_NAME} - MSV: {STUDENT_ID}")
    print("Nhấn Ctrl+C để dừng chương trình bất cứ lúc nào.")
    print("=" * 60 + "\n")

    count = 1
    while True:
        # Tạo nội dung thông điệp theo đúng yêu cầu đề bài
        # Ví dụ format: "Xin chao tu client Python MQTT - B23DCCN001 - Nguyen Van A"
        payload = f"{GREETING} - {STUDENT_ID} - {STUDENT_NAME}"
        
        # Publish thông điệp lên topic
        result = client.publish(TOPIC, payload)
        now_str = datetime.now().strftime("%H:%M:%S")

        print(f"[{now_str}] Đã gửi thông điệp #{count} lên topic '{TOPIC}':")
        print(f"  Payload: {payload}")
        print("-" * 60)

        count += 1
        # Dừng 3 giây giữa các lần gửi (cho phép gửi liên tiếp nhiều thông điệp)
        time.sleep(3)

except KeyboardInterrupt:
    print("\n[INFO] Đã nhận tín hiệu dừng từ người dùng (Ctrl+C).")
except Exception as e:
    print(f"\n[ERROR] Đã xảy ra lỗi: {e}")
finally:
    print("Đang ngắt kết nối với MQTT Broker...")
    client.disconnect()
    print("Đã ngắt kết nối an toàn. Kết thúc chương trình Publisher.")
