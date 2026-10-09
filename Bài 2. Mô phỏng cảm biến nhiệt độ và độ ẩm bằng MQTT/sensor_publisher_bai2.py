import paho.mqtt.client as mqtt
import time
import json
import random

# Cấu hình MQTT Broker
BROKER = "broker.hivemq.com"
PORT = 1883
TOPIC = "iot/lab/sensor01/data"

# Khởi tạo MQTT Client
client = mqtt.Client()

# Kết nối tới Broker
client.connect(BROKER, PORT)
print(f"Đã kết nối tới broker {BROKER}")
print("Bắt đầu gửi dữ liệu cảm biến (Nhấn Ctrl+C để dừng)...")

try:
    while True:
        # Sinh ngẫu nhiên giá trị nhiệt độ (20.0 đến 40.0) và độ ẩm (30.0 đến 80.0)
        temp = round(random.uniform(20.0, 40.0), 1)
        hum = round(random.uniform(30.0, 80.0), 1)
        
        # Tạo payload dưới dạng Dictionary
        payload_dict = {
            "device_id": "sensor01",
            "temperature": temp,
            "humidity": hum
        }
        
        # Chuyển đổi Dictionary sang chuỗi JSON
        payload_json = json.dumps(payload_dict)
        
        # Publish dữ liệu lên topic
        client.publish(TOPIC, payload_json)
        print(f"Đã gửi lên topic '{TOPIC}': {payload_json}")
        
        # Dừng 3 giây trước khi gửi tiếp
        time.sleep(3)
        
except KeyboardInterrupt:
    print("\nĐã dừng chương trình Publisher.")
    client.disconnect()