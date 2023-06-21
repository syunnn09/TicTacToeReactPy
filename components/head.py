from reactpy import html

def Head():
    return(
        html.link({
            'rel': 'stylesheet',
            'href': 'css/tic-tac-toe.css'
        })
    )
