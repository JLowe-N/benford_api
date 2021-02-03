from tornado import web, ioloop
import os
from benford_plot.benford_plot import get_benford_column, get_benford_plot_src_str, get_p_value


class benfordRequestHandler(web.RequestHandler):
    def get(self):
        self.render('index.html', plot=None, pval=None)

    def post(self):
        # take in input_file
        input_file = self.request.files['input_file'][0]
        body = input_file['body']

        # extract needed columns
        target_col = self.get_body_argument('target_column')
        if target_col == '':
            target_col = '7_2009'
        benford_col = get_benford_column(body, target_col)

        # get results
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
        "debug": False
    }
    PORT = int(os.environ.get("PORT", 8881))  # if heroku, dynamic port assignment, default 8881
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
