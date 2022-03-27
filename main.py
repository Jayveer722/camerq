from vidstream import CameraClient
from vidstream import StreamingServer

import threading
import time

receving = StreamingServer('192.168.1.5', 9999)
sending = CameraClient('192.168.1.4', 9999)

t1 = threading.Thread(target=receving.start_server)
t1.start()

time.sleep(2)

t2 = threading.Thread(target=sending.start_stream)
t2.start()

while input("") != "STOP":
    continue

receving.stop_server()
sending.stop_stream()
