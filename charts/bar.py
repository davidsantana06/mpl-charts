from charts.abstract import Chart, plt
from overrides import override


class Bar(Chart):
    @override
    def prepare_data(self):
        # Dados que serão carregados ao gráfico
        self.subjects = ['AMS', 'BD I', 'MPC', 'RC', 'PLP', 'EMP.']
        self.averages = [8.5, 8.9, 8.0, 2.5, 3.0, 9.5]
        self.colors = ['#DC3545' if (average < 7) else '#198754' for average in self.averages]

    @override
    def prepare_chart(self):
        # Atribuir estilo à exibição
        plt.style.use('default')

        # Compor o gráfico com dados
        plt.bar(self.subjects,      # Eixo X
                self.averages,      # Eixo Y
                color=self.colors)  # Cor das barras

        # Adicionar o título e definir o tamanho da fonte
        plt.title('Médias de nota por matéria', fontsize=10)

        # Adicionar o valor da média acima de cada barra
        for index, average in enumerate(self.averages):
            text = (f'média: {average}')
            x_cord = (index - 0.40)
            y_cord = (average + 0.1)

            plt.text(x=x_cord, y=y_cord, s=text, fontsize=8)
