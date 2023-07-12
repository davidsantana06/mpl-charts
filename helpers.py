MARKER_LEN = len('||')
WELCOME, PANEL, INV_INP, SHOW_CHART, GBYE = 0, 1, 2, 3, 4


def format(msg: str):
    # Dividir a mensagem em lista de linhas
    msg = msg.splitlines()

    # Resgatar a quantidade de caracteres da maior linha na mensagem
    larger_line = max(len(line) for line in msg)

    # Formatar as linhas da mensagem
    formatted_lines = [f'| {line:<{larger_line}} |\n' for line in msg]

    # Compor a mensagem com as linhas formatadas
    formatted_msg = ''.join(formatted_lines)

    # Calcular a quantidade de hifens com base na maior linha
    hyphens = '-' * (larger_line + MARKER_LEN)

    # Retornar a mensagem formatada
    return (f'|{hyphens}|\n{formatted_msg}|{hyphens}|')


def msg(idx):
    msg = None

    if (idx == WELCOME):
        msg = 'Matplotlib Charts ~~~\n' + \
              '~~~~ by David Santana'
    elif (idx == PANEL):
        msg = 'Selecione o gráfico:\n'    + \
              '1. Gráfico de barras\n'    + \
              '2. Grafico de linha I\n'   + \
              '3. Gráfico de linha II\n'  + \
              '4. Gráfico de pizza\n'     + \
              '5. Gráfico de dispersão\n' + \
              '0. Encerrar a aplicação'
    elif (idx == INV_INP):
        msg = '~ Aviso\n' + \
              'Entrada inválida!'
    elif (idx == SHOW_CHART):
        msg = 'Exibindo o gráfico...'
    elif (idx == GBYE):
        msg = '~~~~~~~ Até mais! ~~~~~~~\n' + \
              'github.com/davidsantana06'
    else:
        msg = 'Índice inválido!'

    return format(msg)


def validate(chart_selected):
    return (len(chart_selected) == 1 and '0' <= chart_selected <= '5')
