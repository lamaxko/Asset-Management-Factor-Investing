from .libraries import *

def get_pct_returns(data: pd.DataFrame) -> pd.DataFrame:
    returns = data.pct_change(fill_method=None)
    returns = returns.fillna(0)

    return returns

def get_cum_returns(data: pd.DataFrame) -> pd.DataFrame:
    returns = get_pct_returns(data)
    cumulative_returns = (1 + returns).cumprod()

    return cumulative_returns

def get_log_returns(data: pd.DataFrame) -> pd.DataFrame:
    log_returns = np.log(data / data.shift(1))
    log_returns = log_returns.fillna(0)

    return log_returns