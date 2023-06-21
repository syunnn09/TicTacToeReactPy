from reactpy import component, html

from components.square import Square


@component
def Board(squares, click_func):
    def render_square(i):
        return Square(squares[i], lambda: click_func(i))

    return(
        html.div(
            html.div(
                {'style': 'height: 50px'},
                render_square(0),
                render_square(1),
                render_square(2),
            ),
            html.div(
                {'style': 'height: 50px'},
                render_square(3),
                render_square(4),
                render_square(5),
            ),
            html.div(
                {'style': 'height: 50px'},
                render_square(6),
                render_square(7),
                render_square(8),
            ),
        )
    )
