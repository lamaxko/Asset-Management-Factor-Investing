from .libraries import *

def fit_best_distribution(stock_returns):
    distributions = {
        'genextreme': genextreme,
        'logistic': logistic,
        'norm': norm,
        't': t,
    }
    
    best_distribution = None
    best_p_value = -np.inf
    
    for dist_name, dist in distributions.items():
        params = dist.fit(stock_returns)
        D, p_value = kstest(stock_returns, dist_name, args=params)
        
        if p_value > best_p_value:
            best_p_value = p_value
            best_distribution = dist_name, params
    return best_distribution

def transform_to_uniform(data):
    pct_returns = data
    uniform_returns = pd.DataFrame(index=pct_returns.index)

    for column in pct_returns.columns:
        column_data = pct_returns[column]
        # Handle columns with NaNs by checking for NaNs and continuing the loop if NaNs exist
        if column_data.isnull().all():
            uniform_returns[column] = np.nan  # Assign NaNs to the entire column if all values are NaN
        elif column_data.notnull().any():
            # Fit distribution only if there are non-NaN values
            valid_data = column_data.dropna()
            dist_name, params = fit_best_distribution(valid_data)
            dist = getattr(stats, dist_name)
            # Calculate the CDF values using the fitted distribution parameters and existing non-NaN data
            cdf_values = dist.cdf(valid_data, *params)
            # Use the inverse CDF of the uniform distribution to get uniform values
            uniform_data = uniform.ppf(cdf_values)
            # Convert uniform_data (numpy array) to pandas Series with the appropriate index
            uniform_series = pd.Series(uniform_data, index=valid_data.index)
            # Reindex the uniform series to match the original data's index, filling missing values with NaN
            uniform_returns[column] = uniform_series.reindex(column_data.index)

    return uniform_returns
