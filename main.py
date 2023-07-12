from charts.bar import Bar
from charts.line import Line
from charts.line_grid import LineGrid
from charts.pie import Pie
from charts.scatter import Scatter
from helpers import WELCOME, PANEL, INV_INP, SHOW_CHART, GBYE, format, msg, validate


print(msg(WELCOME))
charts = {
    '1': Bar(),
    '2': Line(),
    '3': LineGrid(),
    '4': Pie(),
    '5': Scatter()
}

while True:
    print('\n' + msg(PANEL))
    chart_selected = input('_Entrada: ')

    if (validate(chart_selected)):
        if (chart_selected == '0'):
            print('\n' + msg(GBYE))
            break
        else:
            print('\n' + msg(SHOW_CHART))
            charts[chart_selected].show_chart()

            if (chart_selected == '5'):
                print(f'\n~ DF:\n{charts[chart_selected].get_df()}')
    else:
        print(msg(INV_INP))
