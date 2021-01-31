from tornado import web, iostream, gen, ioloop
import os
import io
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from base64 import b64encode


class benfordRequestHandler(web.RequestHandler):
    def get(self):
        self.render('index.html', plot=None)

    async def post(self):
        def extract_first_digit(number):
            string = str(number)
            first_char = string[0]
            first_digit = int(first_char)
            return first_digit

        input_file = self.request.files['input_file'][0]
        original_fname = input_file['filename']
        extension = os.path.splitext(original_fname)[1]
        body = input_file['body']
        print(extension)
        dataset = pd.read_csv(io.BytesIO(body), sep='\t')
        target_col = dataset['7_2009']
        target_col = target_col.transform(extract_first_digit, axis=0)
        target_col = target_col.value_counts(normalize=True)

        ax = sns.barplot(
            x=target_col.index, y=target_col)

        stream = io.BytesIO()
        plot = ax.get_figure()
        plot.savefig(stream, format="png")
        stream.seek(0)
        plot = b64encode(stream.read())
        plot_src = 'data:image/png;base64,' + plot.decode('utf-8')

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
