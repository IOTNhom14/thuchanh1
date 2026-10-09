import paho.mqtt.client as mqtt
import json

# Cấu hình MQTT Broker
BROKER = "broker.hivemq.com"
PORT = 1883
TOPIC = "iot/lab/sensor01/data"

# Hàm callback khi kết nối thành công tới broker
def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Kết nối thành công tới MQTT Broker!")
        # Đăng ký lắng nghe topic
        client.subscribe(TOPIC)
        print(f"Đang chờ dữ liệu từ topic: {TOPIC}...\n")
        print("-" * 30)
    else:
        print(f"Kết nối thất bại, mã lỗi: {rc}")

# Hàm callback khi nhận được thông điệp từ broker
def on_message(client, userdata, msg):
    try:
        # Giải mã payload nhận được từ định dạng bytes sang string và load vào JSON
        payload_str = msg.payload.decode('utf-8')
        data = json.loads(payload_str)
        
        # Lấy dữ liệu từ JSON
        device_id = data.get("device_id", "Unknown")
        temperature = data.get("temperature", 0.0)
        humidity = data.get("humidity", 0.0)
        
        # In dữ liệu ra màn hình
        print(f"Device: {device_id}")
        print(f"Temperature: {temperature} C")
        print(f"Humidity: {humidity} %")
        
        # Kiểm tra và in cảnh báo
        if temperature > 35:
            print("CANH BAO: Nhiet do cao")
        if humidity < 40:
            print("CANH BAO: Do am thap")
            
        print("-" * 30)
        
    except json.JSONDecodeError:
        print("Lỗi: Không thể phân tích cú pháp JSON.")
    except Exception as e:
        print(f"Có lỗi xảy ra: {e}")

# Khởi tạo MQTT Client
client = mqtt.Client()

# Gán các hàm callback
client.on_connect = on_connect
client.on_message = on_message

# Kết nối tới Broker
client.connect(BROKER, PORT)

# Lặp vô hạn để duy trì kết nối và lắng nghe tin nhắn
try:
    client.loop_forever()
except KeyboardInterrupt:
    print("\nĐã dừng chương trình Subscriber.")
    client.disconnect()