from .libraries import *

def print_checks_01(risk_free_rate, returns_portfolio, factor_data):
    print('RiskF First Date:', risk_free_rate.index.min(), 'Last Date:', risk_free_rate.index.max(), 'Shape:', risk_free_rate.shape)
    print('Portf First Date:', returns_portfolio.index.min(), 'Last Date:', returns_portfolio.index.max(), 'Shape:', returns_portfolio.shape)
    print('Factor First Date:', factor_data.index.min(), 'Last Date:', factor_data.index.max(), 'Shape:', factor_data.shape, '\n')
    return