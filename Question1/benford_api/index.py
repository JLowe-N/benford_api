from tornado import web, iostream, gen, ioloop
import os
import io
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


class uploadRequestHandler(web.RequestHandler):
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
        # target_col = str(target_col)[0]
        print(target_col)
        ax = sns.barplot(
            x=target_col.index, y=target_col)

        buf = io.BytesIO()
        figure = ax.get_figure()
        figure.savefig(buf, format="png")
        buf.seek(0)

        chunk_size = 1024 * 1024 * 1
        self.set_header("Content-Type", "image/png")
        while True:
            chunk = buf.read(chunk_size)
            if not chunk:
                break
            try:
                print(chunk)
                print(type(chunk))
                self.write(chunk)
                await self.flush()
            except iostream.StreamClosedError:
                break
            finally:
                del chunk
        self.finish()


class staticRequestHandler(web.RequestHandler):
    def get(self):
        self.render(os.path.join(dirname, 'static/index.html'))


if __name__ == '__main__':
    dirname = os.path.dirname(__file__)
    PORT = 8881
    app = web.Application([
        (r"/", staticRequestHandler),
        (r"/upload", uploadRequestHandler)
    ])

    app.listen(PORT)
    print(f"Tornado listening on port {PORT}")
    ioloop.IOLoop.current().start()
