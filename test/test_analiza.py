import pandas as pd
from analiza import podstawowe_statystyki

def test_pusty_dataframe(capsys):
    df = pd.DataFrame()
    podstawowe_statystyki(df)
    result = capsys.readouterr()
    assert "Najpierw wczytaj dane z pliku CSV." in result.out