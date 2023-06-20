from fastapi import FastAPI
from reactpy import component, html, hooks
from uvicorn import run
from reactpy.backend.fastapi import configure, Options

def Head():
    return(
        html.link({
            'rel': 'stylesheet',
            'href': 'css/tic-tac-toe.css'
        })
    )

def center():
    return 'display: flex; align-items: center; justify-content: center;'

def calclate_winner(squares):
    lines = [
        [0, 1, 2],
        [3, 4, 5],
        [6, 7, 8],
        [0, 3, 6],
        [1, 4, 7],
        [2, 5, 8],
        [0, 4, 8],
        [2, 4, 6],
    ]
    for i in range(len(lines)):
        a, b, c = lines[i]
        if squares[a] and squares[a] == squares[b] == squares[c]:
            return squares[a]
    return None

@component
def Square(value: str, click_func):
    return (
        html.button(
            {
                'on_click': lambda e: click_func(),
                'style': '''
                    background: #fff;
                    border: 1px solid #999; 
                    font-size: 24px;
                    line-height: 50px;
                    width: 50px;
                    height: 50px;
                    padding: 0;
                '''
            },
            value if value is not None else ''
        )
    )

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

@component
def Game():
    history, set_history = hooks.use_state([{ 'squares': [None for _ in range(9)] }])
    step_number, set_step_number = hooks.use_state(0)
    x_is_next, set_x_is_next = hooks.use_state(True)

    def handle_click(i):
        last_history = history.copy()[0:step_number+1]
        current = history[len(history) - 1]
        square = current['squares'].copy()
        if calclate_winner(square) or square[i]:
            return
        square[i] = 'X' if x_is_next else 'O'
        last_history.append({ "squares": square })
        set_history(last_history)
        set_step_number(len(last_history))
        set_x_is_next(not x_is_next)

    def jump_to(step):
        set_step_number(step)
        set_x_is_next((step % 2) == 0)
        set_history(history[0:step+1])

    def move_func(move):
        desc = f'Go to move# {move}' if move else 'Go to game start'
        return (
            html.li(
                html.button({ 'on_click': lambda e: jump_to(move) }, desc)
            )
        )
    moves = map(move_func, range(len(history)))

    current = history[len(history) - 1]
    winner = calclate_winner(current['squares'])
    if winner:
        status = 'Winner: ' + winner
    else:
        status = 'Next player: ' + ('X' if x_is_next else 'O')
    return(
        html.div(
            html.div(
                Board(current['squares'], lambda i: handle_click(i))
            ),
            html.div(
                html.p(status)
            ),
            html.ol(
                moves
            )
        )
    )

app = FastAPI()

configure(
    app,
    Game,
    Options(head=Head()),
)

run(app)
