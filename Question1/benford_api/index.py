import tornado.web
import tornado.ioloop
import os
import io
import pandas as pd


class uploadRequestHandler(tornado.web.RequestHandler):
    async def post(self):
        input_file = self.request.files['input_file'][0]
        original_fname = input_file['filename']
        extension = os.path.splitext(original_fname)[1]
        body = input_file['body']
        print(extension)
        dataset = pd.read_csv(io.BytesIO(body), sep='\t')
        print(dataset.head())


class staticRequestHandler(tornado.web.RequestHandler):
    def get(self):
        self.render(os.path.join(dirname, 'static/index.html'))


if __name__ == '__main__':
    dirname = os.path.dirname(__file__)
    PORT = 8881
    app = tornado.web.Application([
        (r"/", staticRequestHandler),
        (r"/upload", uploadRequestHandler)
    ])

    app.listen(PORT)
    print(f"Tornado listening on port {PORT}")
    tornado.ioloop.IOLoop.current().start()
