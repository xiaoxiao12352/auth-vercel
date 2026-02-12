from http.server import BaseHTTPRequestHandler
import json

# 授权机器码列表
AUTHORIZED_MIDS = [
    "d41d8cd98f00b204e9800998ecf8427e",
    "5d41402abc4b2a76b9719d911017c592"
]

class handler(BaseHTTPRequestHandler):
    def do_POST(self):
        try:
            # 读取请求数据
            content_length = int(self.headers['Content-Length'])
            post_data = self.rfile.read(content_length)
            data = json.loads(post_data)
            mid = data.get('mid', '')
            
            # 验证机器码
            if mid in AUTHORIZED_MIDS:
                response = {"code": 0, "msg": "授权通过"}
            else:
                response = {"code": 1, "msg": "未授权"}
                
        except Exception as e:
            response = {"code": 1, "msg": f"错误: {str(e)}"}
        
        # 发送响应
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        self.wfile.write(json.dumps(response).encode('utf-8'))
    
    def do_GET(self):
        # 允许 GET 请求测试
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        self.wfile.write(json.dumps({
            "status": "online",
            "endpoint": "/api/check",
            "method": "POST"
        }).encode('utf-8'))
