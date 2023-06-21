from reactpy import component, html, hooks

from components.board import Board
from utils import calculate_winner


@component
def Game():
    history, set_history = hooks.use_state([{ 'squares': [None for _ in range(9)] }])
    step_number, set_step_number = hooks.use_state(0)
    x_is_next, set_x_is_next = hooks.use_state(True)

    def handle_click(i):
        last_history = history.copy()[0:step_number+1]
        current = history[len(history) - 1]
        square = current['squares'].copy()
        if calculate_winner(square) or square[i]:
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
    winner = calculate_winner(current['squares'])
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
