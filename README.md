# Asset Management Factor Investing Repository

This repository contains code and data for developing and analyzing our Copula factor investing strategy, the Upside Ratio. This factor aims to maximize correlation with the market during positive performance periods and minimize it during negative performance periods. The analysis is conducted using data from 100 stocks in the S&P 100 index, with complete data available for 93 of these stocks. The timeframe for the analysis is from June 2006 to July 2016 (120 months). Total returns index is used for the calculation of returns.

## Repository Structure

- **data/**: Contains raw data files.
- **data_copulas/**: Contains data related to copulas.
- **data_uniform/**: Contains transformed uniform data.
- **helpers/**: Contains helper scripts, functions, and libraries.
- **requirements.txt**: Install all dependencies with `pip install -r requirements.txt`.

## Files Description

### 00_TransformUniform.ipynb
Transforms the returns of all stocks into uniform margins using CDF functions. Considers the following distributions:
- GeV
- Logistic
- Normal
- Student's t

### 01_FitCopula.Rmd
Fits Gaussian and Student t copulas to the data using R for its copula package. The best fit is chosen based on maximum likelihood. Splits the uniform data into two segments to capture different correlations with the market.

### 02_CalcUpsideRatio.ipynb
Calculates the Upside Ratio in Python and saves the results. The ratio is obtained by dividing the positive density by the negative density for each stock.

### 03_VisualizationIdea.ipynb
Provides visualizations for the Upside Ratio and related concepts.

### 10_PredictiveRegression.ipynb
Performs a predictive regression to assess the effectiveness of the Upside Ratio as a market timing tool. Tests using a lag of the factor of 1 month, 1 year, and 5 years.

### 20_FamaFrench.ipynb
Conducts a Fama-French regression test on the top and bottom 20 stocks sorted annually. Excess returns of various portfolios are regressed on 1 and 3 factor Fama-French models.

### 30_FamaMacbeth.ipynb
Performs a Fama-MacBeth test on the Upside Ratio factor, comparing it to market beta. 

## Data and Timeframe
- **Stocks**: 100 stocks from the S&P 100 index, with data available for 93.
- **Timeframe**: June 2006 to July 2016 (120 months).
- **Returns Calculation**: From the Total returns index.

Explore the notebooks and scripts for detailed implementation and results. Contributions and feedback are welcome!

---

**Note**: Ensure you have the necessary dependencies installed for both Python and R environments to run the scripts and notebooks seamlessly.
