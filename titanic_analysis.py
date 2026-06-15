import pandas as pd
import matplotlib.pyplot as plt
from dataclasses import dataclass

@dataclass
class TitanicAnalysis:
    filepath: str
    df: pd.DataFrame = None

    #load the data from csv
    def load_data(self) -> pd.DataFrame:
        self.df = pd.read_csv(self.filepath)
        return self.df

    #clean the data
    def clean_data(self) -> pd.DataFrame:
        self.df['Age'] = self.df['Age'].fillna(self.df['Age']).mean()
        self.df = self.df.drop(columns=['Cabin','Embarked'])
        return self.df

    #Calculate the number of people who survived based on gender
    def survival_by_gender(self) -> pd.DataFrame:
        return self.df.groupby('Sex')['Survived'].mean()
    
    #Plot the Survival by gender graph
    def plot_survival(self) -> None:
        survival = self.df.groupby('Sex')['Survived'].mean()
        plt.bar(survival.index,survival.values, color='k', linewidth= 5)
        plt.title('Survival Rate by Gender')
        plt.xlabel('Sex')
        plt.ylabel('Survival Rate')
        plt.tight_layout()
        plt.show()