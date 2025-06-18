import socket

IP = "127.0.0.1"
PORT = 5683

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((IP, PORT))

print(f"✅ Listening for UDP sensor data on {IP}:{PORT}...\n")

try:
    while True:
        data, addr = sock.recvfrom(1024)
        print(f"📥 Received from {addr}: {data.decode()}")

except KeyboardInterrupt:
    print("🔴 Server stopped.")
    sock.close()
