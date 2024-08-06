import pandas as pd
import requests
import json
import time
import base64
import requests

# 账户和密码
username = ''
password = ''

# 合并为字符串
credentials = f'{username}:{password}'

# 进行 Base64 编码
encoded_credentials = base64.b64encode(credentials.encode('utf-8')).decode('utf-8')
#print(encoded_credentials)
# 读取 Excel 文件
file_path = "D:\\devices.xlsx"  # 注意双反斜杠或使用原始字符串
df = pd.read_excel(file_path)

# API 配置
api_url = 'https://as802.awmdm.com/API/mdm/devices/commands'
headers = {
    'Content-Type': 'application/json',
    'Accept': 'application/json',
    'Authorization': f'Basic {encoded_credentials}',  # 替换为你的实际 Authorization
    'aw-tenant-code': ''  # 替换为你的实际 aw-tenant-code
}

# 遍历 DataFrame 的每一行
for index, row in df.iterrows():
    serial_number = row['SerialNumber']  # 假设 A 列是 SerialNumber
    device_name = row['DeviceName']  # 假设 B 列是 DeviceName
    command_xml1 = f"""
    <dict>
        <key>Queries</key>
        <array>
            <string>DeviceName</string>
            <string>ModelName</string>
            <string>Model</string>
            <string>ProductName</string>
            <string>SerialNumber</string>
        </array>
        <key>RequestType</key>
        <string>DeviceInformation</string>
    </dict>
    """
    data1 = {"CommandXml": command_xml1}
    
    # 构建 URL
    request_url1 = f'{api_url}?searchby=Serialnumber&id={serial_number}&command=SyncDevice'
    
    # 发送 POST 请求
    response1 = requests.post(request_url1, headers=headers, data=json.dumps(data1))
    
    # 检查响应状态
    if 200 <= response1.status_code < 300:
        print(f"Successfully sync device with serial number {serial_number}.")
    else:
        print(f"Failed to sync device information with serial number {serial_number}. Status code: {response.status_code}")
        print(f"Response: {response.text}")
    # 构建请求数据
    command_xml = f"""
    <dict>
        <key>RequestType</key>
        <string>Settings</string>
        <key>Settings</key>
        <array>
            <dict>
                <key>DeviceName</key>
                <string>{device_name}</string>
                <key>Item</key>
                <string>DeviceName</string>
            </dict>
        </array>
    </dict>
    """
    data = {"CommandXml": command_xml}
    
    # 构建 URL
    request_url = f'{api_url}?searchby=Serialnumber&id={serial_number}&command=CustomMdmCommand'
    
    # 发送 POST 请求
    response = requests.post(request_url, headers=headers, data=json.dumps(data))
    
    # 检查响应状态
    if 200 <= response.status_code < 300:
        print(f"Successfully updated device with serial number {serial_number}.")
    else:
        print(f"Failed to update device with serial number {serial_number}. Status code: {response.status_code}")
        print(f"Response: {response.text}")
    print("等待 5 秒钟...")
    time.sleep(5)  # 等待 5 秒钟
    print("5 秒钟已过，继续执行下一步操作。")
    command_xml2 = f"""
    <dict>
        <key>Queries</key>
        <array>
            <string>DeviceName</string>
            <string>ModelName</string>
            <string>Model</string>
            <string>ProductName</string>
            <string>SerialNumber</string>
        </array>
        <key>RequestType</key>
        <string>DeviceInformation</string>
    </dict>
    """
    data2 = {"CommandXml": command_xml2}
    
    # 构建 URL
    request_url2 = f'{api_url}?searchby=Serialnumber&id={serial_number}&command=DeviceQuery'
    
    # 发送 POST 请求
    response2 = requests.post(request_url2, headers=headers, data=json.dumps(data2))
    
    # 检查响应状态
    if 200 <= response2.status_code < 300:
        print(f"Successfully query device with serial number {serial_number}.")
    else:
        print(f"Failed to query device information with serial number {serial_number}. Status code: {response.status_code}")
        print(f"Response: {response.text}")
