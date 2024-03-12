from flask import Flask, render_template
import socket
import platform

app = Flask(__name__)

@app.route('/')
def server_info():
    hostname = socket.gethostname()
    ip_address = socket.gethostbyname(hostname)
    os_info = platform.platform()

    return render_template('index.html', hostname=hostname, ip_address=ip_address, os_info=os_info)

if __name__ == '__main__':
    app.run(debug=True,host="0.0.0.0",port="80")