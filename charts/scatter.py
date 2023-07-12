from charts.abstract import Chart, plt
from overrides import override
import numpy as np
import pandas as pd


class Scatter(Chart):
    @override
    def prepare_data(self):
        # Listas de dados que serão convertidas em array
        students = [
            'David', 'Kaik', 'Alisson', 'David', 'Kaik', 'Giovana', 'David', 'Kaik'
        ]
        subjects = ['PLP', 'PLP', 'BD I', 'BD I', 'BD I', 'RC', 'RC', 'RC']
        classrooms = [
            'H405', 'H405', 'H407', 'H407', 'H407', 'H408', 'H408', 'H408'
        ]

        # Converter as listas em arrays
        array_students = np.array(students)
        array_subjects = np.array(subjects)
        array_classrooms = np.array(classrooms)

        # Indicar uma cor para cada matéria
        self.colors = {
            'PLP': '#198754',
            'BD I': '#FFC107',
            'RC': '#DC3545'
        }

        # Compor o dataframe com o nome do estudante, matéria e sala
        self.data_frame = pd.DataFrame({
            'Student': array_students,
            'Subject': array_subjects,
            'Classroom': array_classrooms
        })

        # Armazenar o dataframe como uma string
        self.df_str = self.data_frame.to_string(index=False)

    @override
    def prepare_chart(self):
        # Atribuir estilo à exibição do gráfico
        plt.style.use('default')

        # Compor o gráfico e definir a cor para cada elemento
        for subject, group in self.data_frame.groupby('Subject'):
            color = self.colors[subject]  # Resgatar a cor da matéria
            plt.scatter(group.Student,    # Nome do estudante
                        group.Classroom,  # Numeração da sala
                        c=color,          # Definir as cor
                        label=subject,    # Nome da matéria
                        s=70)             # Tamanho do elemento

        # Adicionar o título e definir o tamanho da fonte
        plt.title('Salas frequentadas pelos estudantes', fontsize=10)

        # Legendar o gráfico
        plt.legend()

    def get_df(self):
        return self.df_str
