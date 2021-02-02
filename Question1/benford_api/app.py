from tornado import web, iostream, gen, ioloop
import os
from benford_plot.benford_plot import get_benford_column, get_benford_plot_src_str, get_p_value


class benfordRequestHandler(web.RequestHandler):
    def get(self):
        self.render('index.html', plot=None, pval=None)

    def post(self):
        input_file = self.request.files['input_file'][0]
        body = input_file['body']
        benford_col = get_benford_column(body)
        p_value = round(get_p_value(
            benford_col['actual_freq'], benford_col['expected_freq']), 3)
        plot_src = get_benford_plot_src_str(benford_col)

        self.render('index.html', plot=plot_src, pval=p_value)


class iconRequestHandler(web.RequestHandler):
    def get(self):
        with open(os.path.join(os.path.dirname(__file__), "static/favicon.svg")) as favicon:
            self.write(favicon.read())


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
            (r"/favicon.ico", iconRequestHandler),
        ], **settings
    )
    app.listen(PORT)
    print(f"Tornado listening on port {PORT}")
    ioloop.IOLoop.current().start()


if __name__ == '__main__':
    main()
