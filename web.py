from http.server import HTTPServer,SimpleHTTPRequestHandler

class MyFirstHTTPRequestHandler(SimpleHTTPRequestHandler):

	def do_GET(self):	
		body = '<html><body>HELLO WORLD!</body></html>'
encode('utf8')
	self.send_response(200)
	self.send_header('Content-type','text/html;charset=utf-8')
	self.send_header('content-length',len(body))
	self.end_headers()
	self.wfile.write(body)

if __name__ == '__main__':
	httpd = HTTPServer(('localhost',8000),MyFirstHTTPRequestHandler)
	print('Serving HTTP on localhost port 8000')
	http.serve_forever()                       
