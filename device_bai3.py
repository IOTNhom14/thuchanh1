import json
import paho.mqtt.client as mqtt

# Cấu hình MQTT Broker
BROKER = "broker.hivemq.com"
PORT = 1883

# Định nghĩa Topic
TOPIC_CMD = "iot/lab/light01/cmd"
TOPIC_STATUS = "iot/lab/light01/status"

# Trạng thái ban đầu của đèn
device_id = "light01"
device_status = "OFF"


def on_connect(client, userdata, flags, rc):
  print(f"Thiết bị {device_id} đã kết nối tới Broker với mã code: {rc}")
  # Lắng nghe topic điều khiển từ Controller
  client.subscribe(TOPIC_CMD)
  print(f"Đang lắng nghe topic: {TOPIC_CMD}")


def on_message(client, userdata, msg):
  global device_status
  command = msg.payload.decode("utf-8").strip()
  print(f"\nNhận được lệnh '{command}' từ topic: {msg.topic}")

  # Xử lý lệnh điều khiển
  if command == "ON":
    device_status = "ON"
    print("-> Trạng thái đèn: ĐÃ BẬT (ON)")
  elif command == "OFF":
    device_status = "OFF"
    print("-> Trạng thái đèn: ĐÃ TẮT (OFF)")
  else:
    print("-> Cảnh báo: Lệnh không hợp lệ!")
    return

  # Tạo payload trạng thái dưới dạng JSON
  payload = {"device_id": device_id, "status": device_status}
  payload_json = json.dumps(payload)

  # Gửi trạng thái mới phản hồi lại lên topic status
  client.publish(TOPIC_STATUS, payload_json)
  print(f"Đã gửi phản hồi trạng thái lên topic {TOPIC_STATUS}: {payload_json}")

# Khởi tạo MQTT Client
client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

# Kết nối đến Broker
client.connect(BROKER, PORT, 60)

# Chạy vòng lặp nền để lắng nghe tin nhắn không đồng bộ
client.loop_start()

try:
  print(f"Thiết bị {device_id} đang hoạt động. Nhấn Ctrl+C để thoát.")
  while True:
    pass
except KeyboardInterrupt:
  print("\nĐang ngắt kết nối thiết bị...")
  client.loop_stop()
  client.disconnect()