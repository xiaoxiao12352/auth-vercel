from http.server import BaseHTTPRequestHandler
import json
import os

# 这里存放你授权的机器码列表（白名单）
AUTHORIZED_MIDS = [
    "d41d8cd98f00b204e9800998ecf8427e",  # 示例机器码1
    "5d41402abc4b2a76b9719d911017c592",  # 示例机器码2
    # 添加更多机器码...
]

class handler(BaseHTTPRequestHandler):
    def do_POST(self):
        # 设置响应头
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()

        # 解析请求体
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length)
        
        try:
            data = json.loads(post_data)
            mid = data.get('mid', '')
            
            # 验证逻辑
            if mid in AUTHORIZED_MIDS:
                response = {"code": 0, "msg": "授权通过"}
            else:
                response = {"code": 1, "msg": "未授权"}
                
        except Exception as e:
            response = {"code": 1, "msg": f"请求解析错误: {str(e)}"}
        
        # 返回 JSON 响应
        self.wfile.write(json.dumps(response).encode())
        return
