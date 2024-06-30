# Asset Management Factor Investing Repository

This repository contains code and data for analyzing and implementing an asset management factor investing strategy, focusing on the Upside Ratio. This factor aims to maximize correlation with the market during positive performance periods and minimize it during negative performance periods. The analysis is conducted using data from 100 stocks in the S&P 100 index, with complete data available for 93 of these stocks. The timeframe for the analysis is from June 2006 to July 2016 (120 months). Total returns index is used for the calculation of returns.

## Repository Structure

- **data/**: Contains raw data files.
- **data_copulas/**: Contains data related to copulas fitting.
- **data_uniform/**: Contains transformed uniform data.
- **helpers/**: Contains helper scripts and functions.

## Files Description

### 00_TransformUniform.ipynb
This notebook transforms the returns of all stocks into uniform margins using CDF functions. The previous five months of daily returns are used, calculated on a rolling basis. The following distributions are considered:
- GeV
- Logistic
- Normal
- Student's t

The best fit is selected based on P-value.

### 01_FitCopula.Rmd
This R script fits Gaussian and Student t copulas to the data. The copula fitting is performed in R due to the availability of the copula package. The best fit is chosen based on maximum likelihood. The uniform data is split into two segments (0 to 0.5 and 0.5 to 1) to capture the negative and positive correlations of the stock with the market, respectively. Joint PDFs of the returns of the stocks and the market are then calculated.

### 02_CalcUpsideRatio.ipynb
This notebook calculates the Upside Ratio in Python and saves the results. The ratio is computed to maximize market correlation during good performance and minimize it during bad performance.

### 03_VisualizationIdea.ipynb
This notebook provides visualizations for the Upside Ratio and related concepts, helping to illustrate the underlying ideas and results.

### 10_PredictiveRegression.ipynb
This notebook performs a predictive regression to assess the effectiveness of the Upside Ratio as a market timing tool. Excess returns of an equally weighted portfolio are regressed on an equally weighted value of the Upside Ratio factor obtained from previous steps.

### 20_FamaFrench.ipynb
This notebook conducts a Fama-French regression test on the top and bottom 20 stocks sorted annually. IPOs are considered in January when the company appears, and delisted companies have a return of 0 for the delisting period and are excluded from subsequent sorts. Excess returns are regressed on 1 and 3 factor Fama-French models.

### 30_FamaMacbeth.ipynb
This notebook performs a Fama-MacBeth test on the Upside Ratio factor. It compares the Upside Ratio to market beta. The first regression runs for each company over the 120-month testing period, generating betas. Then, 120 regressions are performed, regressing excess returns on the betas and the Upside Ratio.

## Data and Timeframe
- **Stocks**: 100 stocks from the S&P 100 index, with data available for 93.
- **Timeframe**: June 2006 to July 2016 (120 months).
- **Returns Calculation**: Total returns index.

## Summary
This repository provides a comprehensive analysis of the Upside Ratio factor, exploring its potential as a tool for market timing and performance enhancement. The combination of Python and R scripts facilitates robust statistical analysis and visualization.

Feel free to explore the notebooks and scripts for detailed implementation and results. Contributions and feedback are welcome!

---

**Note**: Ensure you have the necessary dependencies installed for both Python and R environments to run the scripts and notebooks seamlessly.
