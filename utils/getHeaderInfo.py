from flask import request
import json

def getHeaderInfo(request):
    client_IP = request.remote_addr
    host = request.headers.get('Host')
    user_agent = request.headers.get('User-Agent')
    accept = request.headers.get('Accept')
    data = {"Client IP": client_IP, "Host": host, "User-Agent": user_agent, "Accept": accept}

    return json.dumps(data)