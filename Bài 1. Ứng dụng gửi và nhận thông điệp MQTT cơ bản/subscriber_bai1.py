from datetime import datetime
import paho.mqtt.client as mqtt

# ==========================================================
# CẤU HÌNH MQTT BROKER
# ==========================================================
BROKER = "broker.hivemq.com"
PORT = 1883
TOPIC = "iot/lab/message"

# Hàm callback khi kết nối thành công tới broker
def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print(f"-> Kết nối thành công tới MQTT Broker '{BROKER}'!")
        # Đăng ký lắng nghe topic
        client.subscribe(TOPIC)
        print(f"-> Đã subscribe topic: '{TOPIC}'")
        print("Đang chờ nhận thông điệp... (Nhấn Ctrl+C để dừng chương trình)")
        print("=" * 60)
    else:
        print(f"[ERROR] Kết nối thất bại, mã lỗi (rc): {rc}")

# Hàm callback khi nhận được thông điệp từ broker
def on_message(client, userdata, msg):
    # Lấy thời điểm nhận thông điệp
    receive_time = datetime.now().strftime("%H:%M:%S")
    # Giải mã payload từ bytes sang utf-8
    try:
        payload = msg.payload.decode("utf-8")
    except UnicodeDecodeError:
        payload = str(msg.payload)

    # Hiển thị đúng định dạng yêu cầu đầu ra của đề bài
    print("Nhan duoc message:")
    print(f"Topic: {msg.topic}")
    print(f"Payload: {payload}")
    print(f"Time: {receive_time}")
    print("-" * 60)

# Khởi tạo MQTT Client (hỗ trợ tương thích cả paho-mqtt phiên bản 1.x và 2.x)
if hasattr(mqtt, "CallbackAPIVersion"):
    client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION1)
else:
    client = mqtt.Client()

# Gán các hàm callback
client.on_connect = on_connect
client.on_message = on_message

print("=" * 60)
print("CHƯƠNG TRÌNH SUBSCRIBER - BÀI 1: LẮNG NGHE THÔNG ĐIỆP MQTT")
print(f"Broker: {BROKER}:{PORT}")
print(f"Lắng nghe topic: {TOPIC}")
print("=" * 60)

try:
    # Kết nối tới Broker
    print(f"Đang kết nối tới broker {BROKER}...")
    client.connect(BROKER, PORT, keepalive=60)

    # Duy trì vòng lặp lắng nghe liên tục đến khi người dùng nhấn Ctrl+C
    client.loop_forever()

except KeyboardInterrupt:
    print("\n[INFO] Đã nhận tín hiệu dừng từ người dùng (Ctrl+C).")
except Exception as e:
    print(f"\n[ERROR] Đã xảy ra lỗi: {e}")
finally:
    print("Đang ngắt kết nối với MQTT Broker...")
    client.disconnect()
    print("Đã ngắt kết nối an toàn. Kết thúc chương trình Subscriber.")
