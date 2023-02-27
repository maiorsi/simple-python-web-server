import http.server
import socketserver

PORT = 8080

Handler = http.server.SimpleHTTPRequestHandler

def main():
        with sockerserver.TCP(("", PORT), Handler) as httpd:
                print("Serving @ localhost PORT", PORT)

                try:
                    httpd.serve_forever()
                except KeyboardInterrupt:
                    pass
                
                httpd.server_close()

                print("Shutting down server @ localhost PORT", PORT)

if __name__ == "__main__":
    print("Starting...")

    main()

    print("Stopping...")