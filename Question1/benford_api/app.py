from tornado import web, iostream, gen, ioloop
import os
from benford_plot.benford_plot import get_benford_column, get_benford_plot_src_str


class benfordRequestHandler(web.RequestHandler):
    def get(self):
        self.render('index.html', plot=None)

    def post(self):
        input_file = self.request.files['input_file'][0]
        body = input_file['body']
        benford_col = get_benford_column(body)
        plot_src = get_benford_plot_src_str(benford_col)

        self.render('index.html', plot=plot_src)


def main():
    settings = {
        "template_path": os.path.join(os.path.dirname(__file__), "templates"),
        "static_path": os.path.join(os.path.dirname(__file__), "static"),
        "debug": True
    }
    PORT = 8881
    app = web.Application(
        [
            (r"/", benfordRequestHandler),
        ], **settings
    )
    app.listen(PORT)
    print(f"Tornado listening on port {PORT}")
    ioloop.IOLoop.current().start()


if __name__ == '__main__':
    main()
