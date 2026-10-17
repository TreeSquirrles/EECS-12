import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
import matplotlib.figure as fig
import matplotlib.axes as mpl_ax
from matplotlib.backends.backend_pdf import PdfPages as Pdf
import math

def check_int_input(up: int | float, low: int | float, msg: str, err: str) -> int:
    """
        Takes an upper bound and lower bound and checks if user input satisfies the constraints
    """
    while True:
        try:
            n = int(input(msg))
            if n >= up or n <= low:
                raise ValueError
            return n
        except:
            print(err)

def check_even_input(up: int | float, low: int | float, msg: str, err: str) -> int:
    """
        Takes an upper and lower bound, and checks if user input satisfies the constraints, and is also even.
    """
    while True:
        try:
            n = int(input(msg))
            if n >= up or n <= low or n % 2 == 1:
                raise ValueError
            return n
        except:
            print(err)


"""
    uses list interpolation to construct a fibonacci sequence of arbitrary length num.
"""
calc_fib = lambda num: [
    a
    # note that this is technically F_-1 and F_0 because the first loop moves them over by one.
    for a, b in [(1, 0)]  # sets a = 1 and b = 0
    for _ in range(num + 1)  # sets iteration counter
    for a, b in [(b, a + b)]  # increases each by a = b, b = a + b
                              # namely, this is the recurrence formula
]

"""
    uses list interpolation to construct a Lucas sequence of arbitrary length num.
"""
calc_lucas = lambda num: [  # same logic, in one line
    a for a, b in [(-1, 2)] for _ in range(num + 1) for a, b in [(b, a + b)]
]

"""
    Golden ratio
"""
ratio: float = (1 + math.sqrt(5)) / 2


"""
    Graphing logic
"""

graph: fig.Figure
ax: mpl_ax.Axes
graph, ax = plt.subplots(figsize=(5, 5, "in"), layout="constrained")

graph.canvas.manager.window.resizable(False, False) #type: ignore


def format_graph(title:str|None=None, x_label:str|None=None, y_label:str|None=None) -> None:
    if title:
        ax.set_title(title)
    if x_label:
        ax.set_xlabel(x_label)
    if y_label:
        ax.set_ylabel(y_label)

    return

def graph_pts(length: list[float|int], pts: list[float|int], fmt: str, label: str, legend_loc: int|None = None) -> None:
    """
        Plots an array of points onto the graph with format "fmt"
        If the length of the array is less than "length", then will copy the
        last element of pts until pts has reached length "length"
    """
    if len(pts) < len(length):
        pts = pts + [pts[len(pts)-1] for _ in range(len(length) - len(pts))]
    ax.plot(length, pts, fmt, label=label)
    if legend_loc:
        ax.legend(loc=legend_loc)

def show_graph() -> None:
    plt.show(block=True)

#Critically, showing the graph deletes the graph!
def save_graph(out: Pdf, f: fig.Figure) -> None:
    out.savefig(f)

def clear_graph() -> None:
    global graph, ax
    plt.close(graph)
    graph, ax = plt.subplots(figsize=(5, 5, "in"), layout="constrained")
    graph.canvas.manager.window.resizable(False, False) #type: ignore

def main():
    """
        Main logic
    """
    n = check_int_input(
        math.inf, 2, "Enter an integer N (N > 2): ", "Please follow prompt"
    )

    k = check_even_input(
        n,
        1,
        "Enter an even integer K (2 <= K < N): ",
        "Please follow prompt",
    )

    fib_a: list[int] = calc_fib(n + k)
    luc_a: list[int] = calc_lucas(n)

    print(f"Lucas series (up to N={n}): {luc_a}")
    print(f"Fibonacci series (up to N={n}): {fib_a[:-k]}")
    print(f"Golden Ratio (φ): {ratio}")
    print(f"Left-hand side of equation (1): F[N-K] + F[N+K] = {fib_a[n-k]+fib_a[n+k]}")
    print(f"Right-hand side of equation (1): F[N] * L[K] = {fib_a[n] * luc_a[k]}")
    print("Equation (1) holds true!")
    print(
        "Error: Value too small"
        if n > 40
        else f"Fibonacci error at N={n}: {round(abs((fib_a[n]/fib_a[n-1])-ratio), k)}"
    )
    print(
        f"The natural logarithm of the Fibonacci number up to N={n}: {[-math.inf if i == 0 else round(math.log(i), 2) for i in fib_a[:-k]] }"
    )

    with Pdf("hw2_plots.pdf") as out:

        #Graph 1
        graph_pts([i for i in range(n+1)], [ratio], "b-", "Golden Ratio (φ)", 0)
        graph_pts([i for i in range(n+1)], [0 if i <= 0 else fib_a[i+1]/fib_a[i] for i in range(-1, n)], "r--", "Fibonacci Ratio FN/FN-1", 4)
        format_graph(title="The ratio FN/FN-1 for the Fibonacci series against N", x_label="N")
        save_graph(out, graph)
        show_graph()
        clear_graph()
        
        #Graph 2
        graph_pts([i for i in range(2, n+1)], [0 if i > 40 else round(abs(fib_a[i+1]/fib_a[i] - ratio), k) for i in range(1, n)], "b-", "Fib Error")
        format_graph(title="Fibonacci Error values against N", x_label="N")
        save_graph(out, graph)
        show_graph()
        clear_graph()

        #Graph 3
        graph_pts([i/2 for i in range(n*2+1)], [(i/2)**2 for i in range(n*2+1)], "b-", "Quadratic")
        graph_pts([i for i in range(n+1)], [fib_a[i] for i in range(n+1)], "C1-", "Fibonacci")
        graph_pts([i for i in range(n+1)], [luc_a[i] for i in range(n+1)], "g-", "Lucas", 2)
        format_graph(title="Fibonacci and Lucas sequences' growth VS. quadratic functions", x_label="N")
        save_graph(out, graph)
        show_graph()
        clear_graph()


if __name__ == "__main__":
    main()
