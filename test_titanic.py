from titanic_analysis import TitanicAnalysis
import pytest

@pytest.fixture
def titanic():
    t = TitanicAnalysis(filepath='../DAY2/train.csv')
    t.load_data()
    t.clean_data()
    return t

def test_load_data(titanic):
    assert titanic.df is not None
    assert len(titanic.df) > 0

def test_clean_data(titanic):
    assert titanic.df['Age'].isnull().sum() == 0
    assert 'Cabin' not in titanic.df.columns 
    assert 'Embarked' not in titanic.df.columns

def test_survival_by_gender(titanic):
    assert 'female' in titanic.survival_by_gender().index
    assert 'male' in titanic.survival_by_gender().index

def test_plot_survival(titanic):
    try:
        titanic.plot_survival()
        assert True
    except Exception as e:
        assert False, f"Plot failed: {e}"


