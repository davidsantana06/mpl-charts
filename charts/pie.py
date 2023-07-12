from charts.abstract import Chart, plt
from overrides import override


class Pie(Chart):
    @override
    def prepare_data(self):
        # Dados que serão carregados ao gráfico
        self.platforms = [
            'JavaScript', 'Python', 'Java', 'Go', 'TypeScript', 'Outras'
        ]
        self.popularity_percentages = [20.15, 15.87, 11.40, 8.8, 7.5, 36.28]

    @override
    def prepare_chart(self):
        # Atribuir estilo à exibição
        plt.style.use('default')

        # Compor o gráfico com dados
        plt.pie(self.popularity_percentages,    # Percentual de popularidade
                labels=self.platforms,          # Nome da plataforma
                autopct='%.2f%%',               # Formato de exibição do percentual
                explode=(0.05, 0, 0, 0, 0, 0),  # Taxa de separação por setor
                textprops={'fontsize': 8})      # Tamanho da fonte

        # Adicionar o título e definir o tamanho da fonte
        plt.title('Plataformas mais usadas no GitHub em 2020', fontsize=10)
