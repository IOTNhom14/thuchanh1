import paho.mqtt.client as mqtt

# Cấu hình mqtt broker
BROKER = "broker.hivemq.com"
PORT = 1883

# Định nghĩa Topic
TOPIC_CMD = "iot/lab/light01/cmd"
TOPIC_STATUS = "iot/lab/light01/status"


def on_connect(client, userdata, flags, rc):
  print(f"Controller đã kết nối tới Broker với mã code: {rc}")
  # Subscribe topic trạng thái để nhận phản hồi từ thiết bị
  client.subscribe(TOPIC_STATUS)


def on_message(client, userdata, msg):
  # Nhận và hiển thị phản hồi trạng thái từ thiết bị đèn
  print(f"\n[Phản hồi từ thiết bị]")
  print(f"Trạng thái nhận được: {msg.payload.decode('utf-8')}")
  print("Nhập lệnh (ON / OFF / EXIT): ", end="", flush=True)


# Khởi tạo MQTT Client
client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

# Kết nối đến Broker
client.connect(BROKER, PORT, 60)
client.loop_start()

print("--- CHƯƠNG TRÌNH ĐIỀU KHIỂN ĐÈN (CONTROLLER APP) ---")
print("Các lệnh hỗ trợ: ON (Bật), OFF (Tắt), EXIT (Thoát chương trình)")

try:
  while True:
    cmd = input("Nhập lệnh: ").strip().upper()

    if cmd == "EXIT":
      print("Đang thoát chương trình điều khiển...")
      break
    elif cmd in ["ON", "OFF"]:
      # Publish lệnh xuống thiết bị
      client.publish(TOPIC_CMD, cmd)
      print(f"Đã gửi lệnh {cmd} tới light01")
    else:
      print("Lỗi: Lệnh không hợp lệ! Vui lòng chỉ nhập 'ON', 'OFF' hoặc 'EXIT'.")
except KeyboardInterrupt:
  pass
finally:
  client.loop_stop()
  client.disconnect()