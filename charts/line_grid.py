from charts.abstract import Chart, plt
from overrides import override


class LineGrid(Chart):
    @override
    def prepare_data(self):
        # Dados que serão carregados ao gráfico
        self.games = ['PUBG', 'Lost Ark', 'CS: GO', 'Dota 2', 'Cyberpunk 2077']
        self.players = [3257248, 1325305, 1308963, 1295114, 1054388]

    @override
    def prepare_chart(self):
        # Atribuir estilo à exibição
        plt.style.use('default')

        # Compor o gráfico com dados
        plt.plot(self.games,                             # Nome do jogo
                 self.players,                           # Número de jogadores
                 label='Pico de jogadores, em milhões',  # Descrição da legenda
                 marker='o')                             # Marcador

        # Adicionar o título e definir o tamanho da fonte
        plt.title('Jogos mais populares da Steam', fontsize=10)

        # Adicionar marcação e definir seu estilo
        plt.grid(True, linestyle='--')

        # Legendar o gráfico
        plt.legend()
