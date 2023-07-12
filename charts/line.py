from charts.abstract import Chart, plt
from overrides import override
import matplotlib.ticker as mtick


class Line(Chart):
    @override
    def prepare_data(self):
        # Dados que serão carregados ao gráfico
        self.days = ['Segunda-feira', 'Quarta-feira', 'Sexta-feira']
        self.sales_value = [1550.50, 1785.00, 220.25]

    @override
    def prepare_chart(self):
        # Atribuir estilo à exibição
        plt.style.use('default')

        # Compor o gráfico com dados
        plt.plot(self.days, self.sales_value)

        # Adicionar o título e definir o tamanho da fonte
        plt.title('Valores de venda por dia da semana', fontsize=10)

        # Formatar os valores de venda
        fmt = '${x:,.0f}'
        tick = mtick.StrMethodFormatter(fmt)
        plt.gca().yaxis.set_major_formatter(tick)
