import http.server
import socketserver
import logging
import sys

from runcmd.runcmd import run_cmd

PORT = 8080
IP = "127.0.0.1"
LOG_FILE = "logs/server_logs.log"

class MyHandler(http.server.SimpleHTTPRequestHandler):

    def handle_error(self, code, message):

        error_message = f"Error {code}: {message}"
        self.send_response(code)
        self.send_header("Content-type", "text/plain; charset=utf-8")
        self.end_headers()
        self.wfile.write(error_message.encode('utf-8'))

logging.basicConfig(

    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[
        logging.FileHandler(LOG_FILE),
        logging.StreamHandler(sys.stdout)
    ]
)

try:

    with socketserver.TCPServer((IP, PORT), MyHandler) as httpd:

        logging.info("http://127.0.0.1:8080")
        logging.info(f"Server launched in {IP}:{PORT}")
        logging.info("Access log and server messages are being recorded in 'server_logs.log'")
        httpd.serve_forever()

        run_cmd("sudo killall tor")
        run_cmd("sudo tor")

except KeyboardInterrupt:

    logging.info("\nServer terminated by user.")

except Exception as e:

    logging.error(f"Error: {e}")
