from .libraries import *

def plot_portf_rf_excess(returns_portfolio, risk_free_rate, excess_returns):
    plt.figure(figsize=(12, 7))

    plt.subplot(3, 1, 1)
    plt.plot(returns_portfolio.index.to_timestamp(), returns_portfolio)
    plt.axhline(y=0, color='red', linestyle='--')
    plt.title('Portfolio Returns')
    plt.ylabel('Returns')

    plt.subplot(3, 1, 2)
    plt.plot(risk_free_rate.index.to_timestamp(), risk_free_rate['RF'], color='red')
    plt.title('Risk Free Rate')
    plt.ylabel('Rate (%)')

    plt.subplot(3, 1, 3)
    plt.plot(excess_returns.index.to_timestamp(), excess_returns)
    plt.axhline(y=0, color='red', linestyle='--')
    plt.title('Excess Returns')
    plt.ylabel('Excess Returns')

    plt.tight_layout()
    plt.show()
    return

def plot_ew_test(returns_portfolio, ew_portfolio, factor_data, ew_factor):
    plt.figure(figsize=(12, 7))

    plt.subplot(2, 1, 1)
    plt.plot(returns_portfolio.index.to_timestamp(), returns_portfolio, color='blue', alpha=0.5)
    plt.plot(ew_portfolio.index.to_timestamp(), ew_portfolio, color='red', linewidth=2)
    plt.title('Portfolio and EW Portfolio Returns')
    plt.ylabel('Returns')

    plt.subplot(2, 1, 2)
    plt.plot(factor_data.index.to_timestamp(), factor_data, color='purple', alpha=0.5)
    plt.plot(ew_factor.index.to_timestamp(), ew_factor, color='orange', linewidth=2)
    plt.title('Factor and EW Factor Data')
    plt.ylabel('Factor Value')

    plt.tight_layout()
    plt.show()
    return

def plot_predictive_regressions(ew_portfolio_excess_ret, no_lag_factor, one_year_lag_factor, five_year_lag_factor):
    plt.figure(figsize=(12, 12))
    
    ax1 = plt.subplot(3, 1, 1)
    plot_regression(ax1, ew_portfolio_excess_ret, no_lag_factor, 'No Lag Predictive Regression')
    
    ax2 = plt.subplot(3, 1, 2)
    plot_regression(ax2, ew_portfolio_excess_ret, one_year_lag_factor, 'One-Year Lag Predictive Regression')
    
    ax3 = plt.subplot(3, 1, 3)
    plot_regression(ax3, ew_portfolio_excess_ret, five_year_lag_factor, 'Five-Year Lag Predictive Regression')
    
    plt.tight_layout()
    plt.show()
    return

def plot_regression(ax, ew_portfolio_excess_ret, factor, title):
    X = sm.add_constant(factor)
    Y = ew_portfolio_excess_ret

    model = sm.OLS(Y, X)
    results = model.fit()

    x_val = factor.values.flatten()
    y_val = Y.values.flatten()

    x_fit = np.linspace(x_val.min(), x_val.max(), 100)
    y_fit = results.params['const'] + results.params[X.columns[1]] * x_fit

    ax.scatter(x_val, y_val, color='blue', alpha=0.6, label='Data Points')
    
    ax.plot(x_fit, y_fit, 'r', label=f'Regression Line: Y = {results.params["const"]:.4f} + {results.params[X.columns[1]]:.4f}X')
    
    ax.set_title(title)
    ax.set_xlabel('Predictor Factor')
    ax.set_ylabel('Excess Returns of Portfolio')
    ax.legend()
    return

def plot_std_dev_predicted_excess_returns(time_index, no_lag_predicted_excess_returns, one_year_lag_predicted_excess_returns, five_year_lag_predicted_excess_returns):
    plt.figure(figsize=(15, 10))
    
    plt.subplot(3, 1, 1)
    plt.plot(time_index, no_lag_predicted_excess_returns, label='Predicted Excess Returns', color='blue')
    plt.fill_between(time_index, no_lag_predicted_excess_returns - np.std(no_lag_predicted_excess_returns), 
                     no_lag_predicted_excess_returns + np.std(no_lag_predicted_excess_returns), color='blue', alpha=0.2, label='±1 Std Dev')
    # get mean of predicted excess returns
    no_lag_mean_predicted_excess_returns = np.mean(no_lag_predicted_excess_returns)
    plt.axhline(no_lag_mean_predicted_excess_returns, color='black', linestyle='--', label='Mean Predicted Excess Returns')
    plt.title('No Lag Predicted Excess Returns')
    plt.xlabel('Time')
    plt.ylabel('Excess Returns')
    plt.legend()

    # 1 Year Lag
    plt.subplot(3, 1, 2)
    plt.plot(time_index, one_year_lag_predicted_excess_returns, label='Predicted Excess Returns', color='green')
    plt.fill_between(time_index, one_year_lag_predicted_excess_returns - np.std(one_year_lag_predicted_excess_returns), 
                     one_year_lag_predicted_excess_returns + np.std(one_year_lag_predicted_excess_returns), color='green', alpha=0.2, label='±1 Std Dev')
    one_year_lag_mean_predicted_excess_returns = np.mean(one_year_lag_predicted_excess_returns)
    plt.axhline(one_year_lag_mean_predicted_excess_returns, color='black', linestyle='--', label='Mean Predicted Excess Returns')
    plt.title('1 Year Lag Predicted Excess Returns')
    plt.xlabel('Time')
    plt.ylabel('Excess Returns')
    plt.legend()

    # 5 Year Lag
    plt.subplot(3, 1, 3)
    plt.plot(time_index, five_year_lag_predicted_excess_returns, label='Predicted Excess Returns', color='orange')
    plt.fill_between(time_index, five_year_lag_predicted_excess_returns - np.std(five_year_lag_predicted_excess_returns), 
                     five_year_lag_predicted_excess_returns + np.std(five_year_lag_predicted_excess_returns), color='orange', alpha=0.2, label='±1 Std Dev')
    five_year_lag_mean_predicted_excess_returns = np.mean(five_year_lag_predicted_excess_returns)
    plt.axhline(five_year_lag_mean_predicted_excess_returns, color='black', linestyle='--', label='Mean Predicted Excess Returns')
    plt.title('5 Year Lag Predicted Excess Returns')
    plt.xlabel('Time')
    plt.ylabel('Excess Returns')
    plt.legend()
    
    plt.tight_layout()
    plt.show()
    return

def plot_combined_predicted_excess_returns(time_index, no_lag_predicted_excess_returns, one_year_lag_predicted_excess_returns, five_year_lag_predicted_excess_returns, actual_excess_returns):
    mean_actual_excess_returns = np.mean(actual_excess_returns)
    
    plt.figure(figsize=(15, 8))
    
    plt.plot(time_index, no_lag_predicted_excess_returns, label='No Lag Predicted Excess Returns', color='blue')
    plt.plot(time_index, one_year_lag_predicted_excess_returns, label='1 Year Lag Predicted Excess Returns', color='green')
    plt.plot(time_index, five_year_lag_predicted_excess_returns, label='5 Year Lag Predicted Excess Returns', color='orange')
    plt.axhline(mean_actual_excess_returns, color='red', linestyle='--', label='Mean Actual Excess Returns')
    
    plt.title('Predicted Excess Returns with Different Lags')
    plt.xlabel('Time')
    plt.ylabel('Excess Returns')
    plt.legend()
    
    plt.tight_layout()
    plt.show()
    return

def plot_combined_predicted_excess_returns_annualized(time_index, no_lag_predicted_excess_returns, one_year_lag_predicted_excess_returns, five_year_lag_predicted_excess_returns, actual_excess_returns):
    # Annualizing by multiplying by 12
    no_lag_predicted_annualized = no_lag_predicted_excess_returns * 12
    one_year_lag_predicted_annualized = one_year_lag_predicted_excess_returns * 12
    five_year_lag_predicted_annualized = five_year_lag_predicted_excess_returns * 12
    mean_actual_excess_annualized = np.mean(actual_excess_returns) * 12
    
    plt.figure(figsize=(15, 8))
    
    plt.plot(time_index, no_lag_predicted_annualized, label='No Lag Predicted Annualized Excess Returns', color='blue', linewidth=2)
    plt.plot(time_index, one_year_lag_predicted_annualized, label='1 Year Lag Predicted Annualized Excess Returns', color='green', linewidth=2)
    plt.plot(time_index, five_year_lag_predicted_annualized, label='5 Year Lag Predicted Annualized Excess Returns', color='orange', linewidth=2)
    plt.axhline(mean_actual_excess_annualized, color='red', linestyle='--', label='Mean Actual Annualized Excess Returns', linewidth=2)
    
    # Setting up the y-axis with percentage format
    plt.gca().yaxis.set_major_formatter(PercentFormatter(xmax=1, decimals=0))
    plt.grid(True, which='major', linestyle='--', linewidth='0.5', color='gray')
    plt.grid(True, which='minor', linestyle=':', linewidth='0.5', color='lightgray')
    
    plt.title('Predicted Annualized Excess Returns with Different Lags')
    plt.xlabel('Time')
    plt.ylabel('Annualized Excess Returns (%)')
    plt.legend()
    
    plt.tight_layout()
    plt.show()

def plot_coefficient_of_variation_bars(no_lag_coef_of_variation, one_year_lag_coef_of_variation, five_year_lag_coef_of_variation):
    lags = ['No Lag', '1 Year Lag', '5 Year Lag']
    coef_of_variation_values = [no_lag_coef_of_variation, one_year_lag_coef_of_variation, five_year_lag_coef_of_variation]
    
    plt.figure(figsize=(15, 3))
    plt.barh(lags, coef_of_variation_values, color=['blue', 'green', 'orange'], alpha=0.7)
    
    for i, v in enumerate(coef_of_variation_values):
        plt.text(v, i, round(v, 2), color='black', va='center')
    
    plt.title(r'Coefficient of Variation of Predicted Excess Returns: $\frac{\sigma [E_t(Re)]}{E(Re)}$', fontsize=14)
    plt.ylabel('Lag Period')
    plt.xlabel('Coefficient of Variation')
    
    plt.tight_layout()
    plt.show()
    return

def plot_spread_cumulative_returns(top_20_returns, bottom_20_returns, ew_returns):
    plt.figure(figsize=(15, 8))
    
    # Plot each series
    plt.plot(top_20_returns.index.to_timestamp(), top_20_returns['Cumulative Returns'], label='Top 20 Portfolio Returns', color='blue')
    plt.plot(bottom_20_returns.index.to_timestamp(), bottom_20_returns['Cumulative Returns'], label='Bottom 20 Portfolio Returns', color='red')
    plt.plot(ew_returns.index.to_timestamp(), ew_returns['Cumulative Returns'], label='Equally Weighted Portfolio Returns', color='green')
    
    # Highlight positive spread in light green
    plt.fill_between(top_20_returns.index.to_timestamp(), 
                     top_20_returns['Cumulative Returns'], 
                     bottom_20_returns['Cumulative Returns'], 
                     where=(top_20_returns['Cumulative Returns'] >= bottom_20_returns['Cumulative Returns']), 
                     facecolor='lightgreen', 
                     interpolate=True, 
                     alpha=0.5, 
                     label='Positive Spread (Top 20 > Bottom 20)')

    # Highlight negative spread in light red
    plt.fill_between(top_20_returns.index.to_timestamp(), 
                     top_20_returns['Cumulative Returns'], 
                     bottom_20_returns['Cumulative Returns'], 
                     where=(top_20_returns['Cumulative Returns'] < bottom_20_returns['Cumulative Returns']), 
                     facecolor='lightcoral', 
                     interpolate=True, 
                     alpha=0.5, 
                     label='Negative Spread (Top 20 < Bottom 20)')

    plt.title('Cumulative Portfolio Returns Spread Comparison')
    plt.grid(True, which='major', linestyle='--', linewidth='0.5', color='gray')
    plt.grid(True, which='minor', linestyle=':', linewidth='0.5', color='lightgray')
    plt.xlabel('Time')
    plt.ylabel('Cumulative Returns')
    plt.legend()
    plt.tight_layout()
    plt.show()
    return

def plot_cumulative_returns(long_short_portfolio_returns, short_long_portfolio_returns, equally_weighted_portfolio_returns):
    plt.figure(figsize=(15, 8))
    
    plt.plot(long_short_portfolio_returns.index.to_timestamp(), long_short_portfolio_returns['Cumulative Returns'], label='Long-Short Portfolio Returns', color='purple')
    plt.plot(short_long_portfolio_returns.index.to_timestamp(), short_long_portfolio_returns['Cumulative Returns'], label='Short-Long Portfolio Returns', color='orange')
    plt.plot(equally_weighted_portfolio_returns.index.to_timestamp(), equally_weighted_portfolio_returns['Cumulative Returns'], label='Equally Weighted Portfolio Returns', color='green')
    
    plt.title('Cumulative Portfolio Returns Long-Short and Short-Long Uside Ratio vs Inverse Upside Ratio')
    plt.xlabel('Time')
    plt.ylabel('Cumulative Returns')
    plt.grid(True, which='major', linestyle='--', linewidth='0.5', color='gray')
    plt.grid(True, which='minor', linestyle=':', linewidth='0.5', color='lightgray')
    plt.legend()
    plt.tight_layout()
    plt.show()
    return

def plot_portfolio_portf_rf_excess(top_20_portfolio_returns, bottom_20_portfolio_returns, long_short_portfolio_returns, short_long_portfolio_returns, risk_free_rate):
    plt.figure(figsize=(12, 10))

    plt.subplot(3, 1, 1)
    plt.plot(top_20_portfolio_returns.index.to_timestamp(), top_20_portfolio_returns['Monthly Returns'], label='Top 20 Portfolio Returns', color='blue')
    plt.plot(bottom_20_portfolio_returns.index.to_timestamp(), bottom_20_portfolio_returns['Monthly Returns'], label='Bottom 20 Portfolio Returns', color='red')
    plt.plot(long_short_portfolio_returns.index.to_timestamp(), long_short_portfolio_returns['Monthly Returns'], label='Long-Short Portfolio Returns', color='green')
    plt.plot(short_long_portfolio_returns.index.to_timestamp(), short_long_portfolio_returns['Monthly Returns'], label='Short-Long Portfolio Returns', color='orange')
    plt.legend(loc='center right', bbox_to_anchor=(1, 0.5))
    plt.axhline(y=0, color='red', linestyle='--')
    plt.title('Portfolio Returns')
    plt.ylabel('Returns')

    plt.subplot(3, 1, 2)
    plt.plot(risk_free_rate.index.to_timestamp(), risk_free_rate['RF'], color='red')
    plt.legend(loc='center right', bbox_to_anchor=(1, 0.5))
    plt.title('Risk Free Rate')
    plt.ylabel('Rate')

    plt.subplot(3, 1, 3)
    plt.plot(top_20_portfolio_returns.index.to_timestamp(), top_20_portfolio_returns['Excess Returns'], label='Top 20 Portfolio Excess Returns', color='blue')
    plt.plot(bottom_20_portfolio_returns.index.to_timestamp(), bottom_20_portfolio_returns['Excess Returns'], label='Bottom 20 Portfolio Excess Returns', color='red')
    plt.plot(long_short_portfolio_returns.index.to_timestamp(), long_short_portfolio_returns['Excess Returns'], label='Long-Short Portfolio Excess Returns', color='green')
    plt.plot(short_long_portfolio_returns.index.to_timestamp(), short_long_portfolio_returns['Excess Returns'], label='Short-Long Portfolio Excess Returns', color='orange')
    plt.axhline(y=0, color='red', linestyle='--')
    plt.title('Excess Returns')
    plt.ylabel('Excess Returns')

    plt.tight_layout()
    plt.show()
    return



def plot_ff_one_predictive_regressions(top20_excess_ret, bottom20_excess_ret, long_short_excess_ret, short_long_excess_ret, ff_one_factor):
    plt.figure(figsize=(12, 12))
    
    ax1 = plt.subplot(4, 1, 1)
    plot_ff_one_regression(ax1, top20_excess_ret, ff_one_factor, 'Top 20 Portfolio Predictive Regression')
    
    ax2 = plt.subplot(4, 1, 2)
    plot_ff_one_regression(ax2, bottom20_excess_ret, ff_one_factor, 'Bottom 20 Portfolio Predictive Regression')
    
    ax3 = plt.subplot(4, 1, 3)
    plot_ff_one_regression(ax3, long_short_excess_ret, ff_one_factor, 'Long Short Portfolio Predictive Regression')

    ax4 = plt.subplot(4, 1, 4)
    plot_ff_one_regression(ax4, short_long_excess_ret, ff_one_factor, 'Short Long Portfolio Predictive Regression')
    
    plt.tight_layout()
    plt.show()
    return

def plot_ff_one_regression(ax, ew_portfolio_excess_ret, factor, title):
    X = sm.add_constant(factor)
    Y = ew_portfolio_excess_ret

    model = sm.OLS(Y, X)
    results = model.fit()

    x_val = factor.values.flatten()
    y_val = Y.values.flatten()

    x_fit = np.linspace(x_val.min(), x_val.max(), 100)
    y_fit = results.params['const'] + results.params[X.columns[1]] * x_fit

    ax.scatter(x_val, y_val, color='blue', alpha=0.6, label='Data Points')
    
    ax.plot(x_fit, y_fit, 'r', label=f'Regression Line: Y = {results.params["const"]:.4f} + {results.params[X.columns[1]]:.4f}X')
    
    ax.set_title(title)
    ax.set_xlabel('Market Factor (Mkt-RF)')
    ax.set_ylabel('Excess Returns of Portfolio')
    ax.legend()
    return

def plot_gamma_histograms(gammas):
    fig, axes = plt.subplots(2, 1, figsize=(10, 10), sharey=True)
    fig.suptitle('Histograms of Lambda 1 and Lambda 2', fontsize=16)

    axes[0].hist(gammas['Gamma 1'].dropna(), bins=40, color='skyblue', edgecolor='black')
    axes[0].axvline(gammas['Gamma 1'].mean(), color='red', linestyle='dashed', linewidth=2)
    axes[0].set_title('Lambda 1')
    axes[0].set_xlabel('Lambda 1 Values')
    axes[0].set_ylabel('Frequency')

    axes[0].text(gammas['Gamma 1'].mean(), plt.ylim()[1]*0.9, f'Mean: {gammas["Gamma 1"].mean():.4f}', color='red', horizontalalignment='center')


    axes[1].hist(gammas['Gamma 2'].dropna(), bins=40, color='lightgreen', edgecolor='black')
    axes[1].axvline(gammas['Gamma 2'].mean(), color='red', linestyle='dashed', linewidth=2)
    axes[1].set_title('Lambda 2')
    axes[1].set_xlabel('Lambda 2 Values')

    axes[1].text(gammas['Gamma 2'].mean(), plt.ylim()[1]*0.9, f'Mean: {gammas["Gamma 2"].mean():.4f}', color='red', horizontalalignment='center')

    plt.tight_layout(rect=[0, 0.03, 1, 0.95])
    plt.show()
    return

def plot_ff_one_predictive_regressions_no_labels(top20_excess_ret, bottom20_excess_ret, long_short_excess_ret, short_long_excess_ret, ff_one_factor):
    plt.figure(figsize=(10, 11))

    ax1 = plt.subplot(4, 1, 1)
    plot_ff_one_regression_no_labels(ax1, top20_excess_ret, ff_one_factor)
    
    ax2 = plt.subplot(4, 1, 2)
    plot_ff_one_regression_no_labels(ax2, bottom20_excess_ret, ff_one_factor)
    
    ax3 = plt.subplot(4, 1, 3)
    plot_ff_one_regression_no_labels(ax3, long_short_excess_ret, ff_one_factor)
    
    ax4 = plt.subplot(4, 1, 4)
    plot_ff_one_regression_no_labels(ax4, short_long_excess_ret, ff_one_factor)
    
    plt.tight_layout()
    plt.show()
    return

def plot_ff_one_regression_no_labels(ax, ew_portfolio_excess_ret, factor):
    X = sm.add_constant(factor)
    Y = ew_portfolio_excess_ret

    model = sm.OLS(Y, X)
    results = model.fit()

    x_val = factor.values.flatten()
    y_val = Y.values.flatten()

    x_fit = np.linspace(x_val.min(), x_val.max(), 100)
    y_fit = results.params['const'] + results.params[X.columns[1]] * x_fit

    ax.scatter(x_val, y_val, color='blue', alpha=0.6, label='Data Points')
    
    ax.plot(x_fit, y_fit, 'r', label=f'Regression Line: Y = {results.params["const"]:.4f} + {results.params[X.columns[1]]:.4f}X')
    
    ax.set_title('')
    ax.set_xlabel('')
    ax.set_ylabel('')
    return