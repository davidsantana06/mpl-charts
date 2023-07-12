from abc import ABC, abstractmethod
import matplotlib.pyplot as plt


class Chart(ABC):
    def __init__(self):
        self.data_prepared = False

    # Preparar os dados
    @abstractmethod
    def prepare_data(self):
        pass

    # Preparar o gráfico
    @abstractmethod
    def prepare_chart(self):
        pass

    # Exibir o gráfico
    def show_chart(self):
        if (not self.data_prepared):
            self.prepare_data()
            self.data_prepared = True
        self.prepare_chart()
        plt.show()
