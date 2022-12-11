import io
from flask import Response, Flask, request
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
import numpy as np
import matplotlib.pyplot as plt

plt.rcParams["figure.figsize"] = [7.50, 3.50]
plt.rcParams["figure.autolayout"] = True

app = Flask(__name__)


@app.route('/print-plot')
def plot_png():
    a = request.args.get('a', default=0)
    b = request.args.get('b', default=0)
    c = request.args.get('c', default=0)
    x_min = request.args.get('x_min', default=-10)
    x_max = request.args.get('x_max', default=10)
    y_min = request.args.get('y_min', default=-10)
    y_max = request.args.get('y_max', default=10)

    x = np.linspace(float(x_min), float(x_max))
    y = float(a) * x ** 2 + float(b) * x + float(c)
    fig, ax = plt.subplots()
    ax.set_title("Quadratic Equation Function")
    plt.ylim([y_min, y_max])
    ax.plot(x, y)

    output = io.BytesIO()
    FigureCanvas(fig).print_png(output)
    return Response(output.getvalue(), mimetype='image/png')


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')
