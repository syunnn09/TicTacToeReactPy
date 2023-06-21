from reactpy import component, html


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
