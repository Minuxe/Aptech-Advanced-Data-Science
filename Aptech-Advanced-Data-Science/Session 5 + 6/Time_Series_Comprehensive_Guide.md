# 📊 Hướng Dẫn Toàn Diện Về Time Series Analysis
## Từ Cơ Bản Đến Deep Learning

*Giảng viên: Khóa học Advanced Data Science*

---

## Mục Lục
1. [Giới Thiệu Về Time Series](#1-giới-thiệu-về-time-series)
2. [Các Thành Phần Của Time Series](#2-các-thành-phần-của-time-series)
3. [Tính Dừng (Stationarity)](#3-tính-dừng-stationarity)
4. [Phân Tích Tự Tương Quan](#4-phân-tích-tự-tương-quan)
5. [Các Phương Pháp Cổ Điển](#5-các-phương-pháp-cổ-điển)
6. [Machine Learning Cho Time Series](#6-machine-learning-cho-time-series)
7. [Deep Learning Cho Time Series](#7-deep-learning-cho-time-series)
8. [Kỹ Thuật Nâng Cao](#8-kỹ-thuật-nâng-cao)
9. [Ứng Dụng Thực Tế](#9-ứng-dụng-thực-tế)
10. [Best Practices & Tips](#10-best-practices--tips)

---

## 1. Giới Thiệu Về Time Series

### 1.1 Time Series Là Gì?

**Định nghĩa:** Time series (chuỗi thời gian) là một tập hợp các quan sát được ghi nhận theo thứ tự thời gian đều đặn.

**Đặc điểm chính:**
- Dữ liệu được sắp xếp theo thời gian
- Thứ tự các quan sát có ý nghĩa quan trọng
- Các quan sát có thể phụ thuộc lẫn nhau (temporal dependency)
- Có tính chu kỳ và xu hướng

**Ví dụ thực tế:**
- 📈 Giá cổ phiếu hàng ngày
- 🌡️ Nhiệt độ theo giờ
- 🛒 Doanh số bán hàng theo tháng
- 💓 Nhịp tim theo giây
- 🌊 Mực nước sông theo ngày

### 1.2 Tại Sao Time Series Đặc Biệt?

**Khác biệt với dữ liệu thông thường:**

| Đặc điểm | Dữ liệu Thông Thường | Time Series |
|----------|---------------------|-------------|
| **Độc lập** | Các quan sát độc lập | Quan sát phụ thuộc thời gian |
| **Thứ tự** | Không quan trọng | Rất quan trọng |
| **Tương quan** | Không có tự tương quan | Có autocorrelation |
| **Train-Test Split** | Random split | Sequential split |

### 1.3 Các Loại Time Series

**1. Univariate Time Series:**
- Chỉ có một biến được quan sát theo thời gian
- Ví dụ: Giá Bitcoin theo ngày

**2. Multivariate Time Series:**
- Nhiều biến được quan sát cùng lúc theo thời gian
- Ví dụ: Nhiệt độ, độ ẩm, áp suất cùng thời điểm

**3. Theo tần suất:**
- **High-frequency:** Giây, phút (financial tick data)
- **Medium-frequency:** Giờ, ngày
- **Low-frequency:** Tuần, tháng, năm

---

## 2. Các Thành Phần Của Time Series

### 2.1 Decomposition - Phân Tích Thành Phần

Một time series thường được phân tích thành 4 thành phần chính:

```
Y(t) = Trend + Seasonality + Cyclic + Residual
```

### 2.2 Chi Tiết Từng Thành Phần

#### **A. Trend (Xu hướng)**
- Xu hướng tăng hoặc giảm dài hạn
- Không lặp lại theo chu kỳ cố định
- Phản ánh sự thay đổi dài hạn

**Ví dụ:**
```python
# Trend tuyến tính
Y_trend(t) = β₀ + β₁×t

# Trend phi tuyến
Y_trend(t) = β₀ + β₁×t + β₂×t²
```

#### **B. Seasonality (Tính mùa vụ)**
- Biến động lặp lại theo chu kỳ cố định
- Chu kỳ thường: ngày, tuần, tháng, quý, năm
- Có thể dự đoán được

**Ví dụ:**
- Doanh số kem tăng mùa hè, giảm mùa đông
- Lưu lượng traffic tăng giờ cao điểm

#### **C. Cyclic (Chu kỳ)**
- Biến động không theo chu kỳ cố định
- Thường dài hơn một năm
- Khó dự đoán hơn seasonality

**Ví dụ:** Chu kỳ kinh tế (recession, expansion)

#### **D. Residual/Noise (Nhiễu)**
- Phần không giải thích được
- Biến động ngẫu nhiên
- Sau khi loại bỏ trend, seasonality, cyclic

### 2.3 Hai Mô Hình Decomposition

#### **Additive Model (Mô hình cộng):**
```
Y(t) = T(t) + S(t) + C(t) + R(t)
```
- Sử dụng khi: Biên độ seasonality không đổi
- Phù hợp: Dữ liệu tuyến tính

#### **Multiplicative Model (Mô hình nhân):**
```
Y(t) = T(t) × S(t) × C(t) × R(t)
```
- Sử dụng khi: Biên độ seasonality thay đổi theo trend
- Phù hợp: Dữ liệu có tăng trưởng theo tỷ lệ

**Code ví dụ:**
```python
from statsmodels.tsa.seasonal import seasonal_decompose

# Additive decomposition
result_add = seasonal_decompose(data, model='additive', period=12)

# Multiplicative decomposition
result_mult = seasonal_decompose(data, model='multiplicative', period=12)

# Visualize
result_add.plot()
```

---

## 3. Tính Dừng (Stationarity)

### 3.1 Stationarity Là Gì?

**Định nghĩa:** Một time series được gọi là **stationary** (dừng) nếu các thuộc tính thống kê không thay đổi theo thời gian.

**Các điều kiện:**
1. **Mean không đổi:** E[Y(t)] = μ (constant)
2. **Variance không đổi:** Var[Y(t)] = σ² (constant)
3. **Covariance không phụ thuộc thời gian:** Cov[Y(t), Y(t+k)] chỉ phụ thuộc vào k

### 3.2 Tại Sao Cần Stationarity?

**Lý do quan trọng:**
1. Hầu hết các mô hình thống kê (ARIMA, SARIMA) yêu cầu stationarity
2. Dễ dàng mô hình hóa và dự đoán
3. Các thuộc tính thống kê nhất quán

### 3.3 Các Loại Non-Stationary

#### **A. Trend-Stationary:**
- Có trend nhưng không có unit root
- Khử trend bằng cách: Y'(t) = Y(t) - trend(t)

#### **B. Difference-Stationary:**
- Có unit root
- Khử bằng differencing: Y'(t) = Y(t) - Y(t-1)

### 3.4 Kiểm Tra Stationarity

#### **Method 1: Visual Inspection**
```python
import matplotlib.pyplot as plt

# Plot time series
plt.plot(data)
plt.title('Time Series Plot')
plt.show()

# Plot rolling statistics
rolling_mean = data.rolling(window=12).mean()
rolling_std = data.rolling(window=12).std()

plt.plot(data, label='Original')
plt.plot(rolling_mean, label='Rolling Mean')
plt.plot(rolling_std, label='Rolling Std')
plt.legend()
plt.show()
```

#### **Method 2: Augmented Dickey-Fuller (ADF) Test**

**Giả thuyết:**
- **H₀:** Time series có unit root (non-stationary)
- **H₁:** Time series không có unit root (stationary)

```python
from statsmodels.tsa.stattools import adfuller

def adf_test(series, name=''):
    result = adfuller(series.dropna())
    
    print(f'ADF Test for {name}')
    print(f'ADF Statistic: {result[0]:.4f}')
    print(f'p-value: {result[1]:.4f}')
    print(f'Critical Values:')
    for key, value in result[4].items():
        print(f'   {key}: {value:.3f}')
    
    if result[1] <= 0.05:
        print("✅ Reject H₀: Series is STATIONARY")
    else:
        print("❌ Fail to reject H₀: Series is NON-STATIONARY")
    print()

# Sử dụng
adf_test(data['sales'], 'Sales Data')
```

**Giải thích kết quả:**
- **p-value < 0.05:** Dữ liệu stationary
- **p-value > 0.05:** Dữ liệu non-stationary
- **ADF Statistic < Critical Value:** Stationary

#### **Method 3: KPSS Test**

**Giả thuyết ngược với ADF:**
- **H₀:** Series is stationary
- **H₁:** Series is non-stationary

```python
from statsmodels.tsa.stattools import kpss

def kpss_test(series, name=''):
    result = kpss(series.dropna(), regression='ct')
    
    print(f'KPSS Test for {name}')
    print(f'KPSS Statistic: {result[0]:.4f}')
    print(f'p-value: {result[1]:.4f}')
    print(f'Critical Values:')
    for key, value in result[3].items():
        print(f'   {key}: {value:.3f}')
    
    if result[1] < 0.05:
        print("❌ Reject H₀: Series is NON-STATIONARY")
    else:
        print("✅ Fail to reject H₀: Series is STATIONARY")
```

### 3.5 Chuyển Đổi Non-Stationary Thành Stationary

#### **A. Differencing**

**First-order differencing:**
```python
# Differencing
data_diff = data.diff().dropna()

# Seasonal differencing (period=12 cho monthly data)
data_seasonal_diff = data.diff(12).dropna()

# Combined
data_combined = data.diff().diff(12).dropna()
```

**Khi nào dùng:**
- Data có trend
- ADF test cho p-value > 0.05

#### **B. Log Transformation**
```python
import numpy as np

# Log transformation
data_log = np.log(data)

# Log + Differencing
data_log_diff = np.log(data).diff().dropna()
```

**Khi nào dùng:**
- Variance tăng theo thời gian
- Multiplicative seasonality

#### **C. Detrending**
```python
from scipy import signal

# Linear detrending
data_detrended = signal.detrend(data)

# Polynomial detrending
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression

# Fit polynomial trend
X = np.arange(len(data)).reshape(-1, 1)
poly = PolynomialFeatures(degree=2)
X_poly = poly.fit_transform(X)
model = LinearRegression().fit(X_poly, data)
trend = model.predict(X_poly)

# Remove trend
data_detrended = data - trend
```

#### **D. Seasonal Decomposition**
```python
from statsmodels.tsa.seasonal import seasonal_decompose

decomposition = seasonal_decompose(data, model='additive', period=12)
data_stationary = decomposition.resid.dropna()
```

---

## 4. Phân Tích Tự Tương Quan

### 4.1 Autocorrelation (ACF)

**Định nghĩa:** Mức độ tương quan giữa Y(t) và Y(t-k)

**Công thức:**
```
ACF(k) = Corr(Y_t, Y_{t-k}) = Cov(Y_t, Y_{t-k}) / Var(Y_t)
```

**Code:**
```python
from statsmodels.graphics.tsaplots import plot_acf

# Plot ACF
plot_acf(data, lags=40)
plt.title('Autocorrelation Function (ACF)')
plt.show()
```

**Giải thích:**
- **Lag 0:** Luôn = 1 (tự tương quan với chính nó)
- **Significant lags:** Vượt ra ngoài confidence interval (blue area)
- **Slow decay:** Indicates trend or non-stationarity
- **Sharp cutoff:** Indicates MA process

### 4.2 Partial Autocorrelation (PACF)

**Định nghĩa:** Tương quan giữa Y(t) và Y(t-k) sau khi loại bỏ ảnh hưởng của các lag trung gian

**Code:**
```python
from statsmodels.graphics.tsaplots import plot_pacf

# Plot PACF
plot_pacf(data, lags=40)
plt.title('Partial Autocorrelation Function (PACF)')
plt.show()
```

**Giải thích:**
- **Sharp cutoff at lag p:** Suggests AR(p) model
- **Gradual decay:** Suggests MA component

### 4.3 Sử Dụng ACF/PACF Để Xác Định Model

| Pattern | ACF | PACF | Suggested Model |
|---------|-----|------|-----------------|
| **AR(p)** | Decays gradually | Cuts off after lag p | AR(p) |
| **MA(q)** | Cuts off after lag q | Decays gradually | MA(q) |
| **ARMA(p,q)** | Decays gradually | Decays gradually | ARMA(p,q) |

---

## 5. Các Phương Pháp Cổ Điển

### 5.1 Moving Average (MA)

**Simple Moving Average:**
```python
# Simple MA
window = 7
data['MA_7'] = data['value'].rolling(window=window).mean()

# Weighted MA
data['WMA_7'] = data['value'].rolling(window=window).apply(
    lambda x: np.dot(x, np.arange(1, len(x)+1)) / np.arange(1, len(x)+1).sum()
)

# Exponential MA
data['EMA_7'] = data['value'].ewm(span=window, adjust=False).mean()
```

### 5.2 Exponential Smoothing

#### **Simple Exponential Smoothing (SES)**
**Phù hợp:** Data không có trend và seasonality

```python
from statsmodels.tsa.holtwinters import SimpleExpSmoothing

# Fit model
model = SimpleExpSmoothing(train_data)
fitted_model = model.fit(smoothing_level=0.2, optimized=True)

# Forecast
forecast = fitted_model.forecast(steps=12)
```

**Công thức:**
```
Ŷ_{t+1} = α×Y_t + (1-α)×Ŷ_t
```
- α: smoothing parameter (0 < α < 1)

#### **Holt's Linear Trend**
**Phù hợp:** Data có trend nhưng không có seasonality

```python
from statsmodels.tsa.holtwinters import Holt

model = Holt(train_data)
fitted_model = model.fit(smoothing_level=0.3, smoothing_trend=0.1)
forecast = fitted_model.forecast(steps=12)
```

#### **Holt-Winters (Triple Exponential Smoothing)**
**Phù hợp:** Data có cả trend và seasonality

```python
from statsmodels.tsa.holtwinters import ExponentialSmoothing

# Additive model
model = ExponentialSmoothing(
    train_data,
    trend='add',
    seasonal='add',
    seasonal_periods=12
)

# Multiplicative model
model = ExponentialSmoothing(
    train_data,
    trend='mul',
    seasonal='mul',
    seasonal_periods=12
)

fitted_model = model.fit()
forecast = fitted_model.forecast(steps=12)
```

### 5.3 ARIMA Models

#### **AR (AutoRegressive) Model**

**Định nghĩa:** Giá trị hiện tại phụ thuộc vào các giá trị quá khứ

**Công thức AR(p):**
```
Y_t = c + φ₁Y_{t-1} + φ₂Y_{t-2} + ... + φₚY_{t-p} + ε_t
```

**Ví dụ AR(1):**
```python
from statsmodels.tsa.arima.model import ARIMA

# AR(1) model
model = ARIMA(train_data, order=(1, 0, 0))
fitted_model = model.fit()
print(fitted_model.summary())
```

#### **MA (Moving Average) Model**

**Định nghĩa:** Giá trị hiện tại phụ thuộc vào các error quá khứ

**Công thức MA(q):**
```
Y_t = μ + ε_t + θ₁ε_{t-1} + θ₂ε_{t-2} + ... + θₑε_{t-q}
```

**Ví dụ MA(1):**
```python
# MA(1) model
model = ARIMA(train_data, order=(0, 0, 1))
fitted_model = model.fit()
```

#### **ARMA Model**

**Kết hợp AR và MA:**
```
ARMA(p,q): AR(p) + MA(q)
```

```python
# ARMA(2,1) model
model = ARIMA(train_data, order=(2, 0, 1))
fitted_model = model.fit()
```

#### **ARIMA Model**

**ARIMA(p,d,q):**
- **p:** Order of AR
- **d:** Degree of differencing
- **q:** Order of MA

```python
from statsmodels.tsa.arima.model import ARIMA

# ARIMA(1,1,1) model
model = ARIMA(train_data, order=(1, 1, 1))
fitted_model = model.fit()

# Forecast
forecast = fitted_model.forecast(steps=12)

# Diagnostic plots
fitted_model.plot_diagnostics(figsize=(15, 10))
plt.show()
```

**Cách chọn parameters:**
1. **d:** Dùng ADF test, thường d=1 hoặc d=2
2. **p:** Nhìn PACF plot (cutoff point)
3. **q:** Nhìn ACF plot (cutoff point)

#### **Auto ARIMA**

**Tự động tìm best parameters:**
```python
from pmdarima import auto_arima

# Auto ARIMA
model = auto_arima(
    train_data,
    start_p=0, start_q=0,
    max_p=5, max_q=5,
    d=None,  # Let auto_arima find d
    seasonal=False,
    trace=True,
    error_action='ignore',
    suppress_warnings=True,
    stepwise=True
)

print(model.summary())

# Forecast
forecast = model.predict(n_periods=12)
```

### 5.4 SARIMA (Seasonal ARIMA)

**SARIMA(p,d,q)(P,D,Q)ₛ:**
- **(p,d,q):** Non-seasonal parameters
- **(P,D,Q):** Seasonal parameters
- **s:** Seasonal period

```python
from statsmodels.tsa.statespace.sarimax import SARIMAX

# SARIMA(1,1,1)(1,1,1,12) for monthly data
model = SARIMAX(
    train_data,
    order=(1, 1, 1),
    seasonal_order=(1, 1, 1, 12)
)

fitted_model = model.fit()

# Forecast
forecast = fitted_model.forecast(steps=12)

# Get confidence intervals
forecast_df = fitted_model.get_forecast(steps=12)
forecast_mean = forecast_df.predicted_mean
forecast_ci = forecast_df.conf_int()
```

**Auto SARIMA:**
```python
from pmdarima import auto_arima

model = auto_arima(
    train_data,
    start_p=0, start_q=0,
    max_p=3, max_q=3,
    seasonal=True,
    m=12,  # Seasonal period
    start_P=0, start_Q=0,
    max_P=2, max_Q=2,
    d=None, D=None,
    trace=True,
    error_action='ignore',
    suppress_warnings=True,
    stepwise=True
)
```

### 5.5 Model Evaluation

#### **Metrics:**

```python
from sklearn.metrics import mean_absolute_error, mean_squared_error
import numpy as np

def evaluate_model(actual, predicted):
    mae = mean_absolute_error(actual, predicted)
    mse = mean_squared_error(actual, predicted)
    rmse = np.sqrt(mse)
    mape = np.mean(np.abs((actual - predicted) / actual)) * 100
    
    print(f'MAE:  {mae:.4f}')
    print(f'MSE:  {mse:.4f}')
    print(f'RMSE: {rmse:.4f}')
    print(f'MAPE: {mape:.4f}%')
    
    return {'MAE': mae, 'MSE': mse, 'RMSE': rmse, 'MAPE': mape}
```

#### **AIC và BIC:**
```python
print(f'AIC: {fitted_model.aic:.2f}')
print(f'BIC: {fitted_model.bic:.2f}')
```
- **Lower is better**
- Dùng để so sánh models

#### **Residual Analysis:**
```python
residuals = fitted_model.resid

# Plot residuals
plt.figure(figsize=(12, 4))
plt.subplot(1, 2, 1)
plt.plot(residuals)
plt.title('Residuals Over Time')

plt.subplot(1, 2, 2)
plt.hist(residuals, bins=30)
plt.title('Residuals Distribution')
plt.show()

# Test for white noise
from statsmodels.stats.diagnostic import acorr_ljungbox

lb_test = acorr_ljungbox(residuals, lags=10, return_df=True)
print(lb_test)
```

**Good residuals should:**
- Have zero mean
- Be normally distributed
- Have constant variance (homoscedastic)
- No autocorrelation (white noise)

---

## 6. Machine Learning Cho Time Series

### 6.1 Feature Engineering

#### **A. Lag Features**
```python
def create_lag_features(df, column, lags):
    for lag in range(1, lags + 1):
        df[f'{column}_lag_{lag}'] = df[column].shift(lag)
    return df

# Create lag features
data = create_lag_features(data, 'sales', lags=7)
```

#### **B. Rolling Window Features**
```python
def create_rolling_features(df, column, windows):
    for window in windows:
        df[f'{column}_rolling_mean_{window}'] = df[column].rolling(window).mean()
        df[f'{column}_rolling_std_{window}'] = df[column].rolling(window).std()
        df[f'{column}_rolling_min_{window}'] = df[column].rolling(window).min()
        df[f'{column}_rolling_max_{window}'] = df[column].rolling(window).max()
    return df

# Create rolling features
data = create_rolling_features(data, 'sales', windows=[7, 14, 30])
```

#### **C. Date/Time Features**
```python
def create_date_features(df, date_column):
    df['year'] = df[date_column].dt.year
    df['month'] = df[date_column].dt.month
    df['day'] = df[date_column].dt.day
    df['dayofweek'] = df[date_column].dt.dayofweek
    df['quarter'] = df[date_column].dt.quarter
    df['dayofyear'] = df[date_column].dt.dayofyear
    df['weekofyear'] = df[date_column].dt.isocalendar().week
    df['is_weekend'] = df['dayofweek'].isin([5, 6]).astype(int)
    df['is_month_start'] = df[date_column].dt.is_month_start.astype(int)
    df['is_month_end'] = df[date_column].dt.is_month_end.astype(int)
    return df
```

#### **D. Expanding Window Features**
```python
def create_expanding_features(df, column):
    df[f'{column}_expanding_mean'] = df[column].expanding().mean()
    df[f'{column}_expanding_std'] = df[column].expanding().std()
    return df
```

#### **E. Differencing Features**
```python
def create_diff_features(df, column, periods):
    for period in periods:
        df[f'{column}_diff_{period}'] = df[column].diff(period)
    return df
```

### 6.2 Random Forest for Time Series

```python
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import TimeSeriesSplit

# Prepare data
X = data[feature_columns].values
y = data['target'].values

# Time series cross-validation
tscv = TimeSeriesSplit(n_splits=5)

# Model
rf_model = RandomForestRegressor(
    n_estimators=100,
    max_depth=10,
    min_samples_split=5,
    random_state=42
)

# Train
rf_model.fit(X_train, y_train)

# Predict
predictions = rf_model.predict(X_test)

# Feature importance
feature_importance = pd.DataFrame({
    'feature': feature_columns,
    'importance': rf_model.feature_importances_
}).sort_values('importance', ascending=False)

print(feature_importance)
```

### 6.3 XGBoost for Time Series

```python
import xgboost as xgb

# Model
xgb_model = xgb.XGBRegressor(
    n_estimators=1000,
    learning_rate=0.01,
    max_depth=5,
    min_child_weight=1,
    subsample=0.8,
    colsample_bytree=0.8,
    objective='reg:squarederror',
    random_state=42
)

# Train with early stopping
xgb_model.fit(
    X_train, y_train,
    eval_set=[(X_val, y_val)],
    early_stopping_rounds=50,
    verbose=False
)

# Predict
predictions = xgb_model.predict(X_test)
```

### 6.4 LightGBM for Time Series

```python
import lightgbm as lgb

# Model
lgb_model = lgb.LGBMRegressor(
    n_estimators=1000,
    learning_rate=0.01,
    max_depth=5,
    num_leaves=31,
    subsample=0.8,
    colsample_bytree=0.8,
    random_state=42
)

# Train
lgb_model.fit(
    X_train, y_train,
    eval_set=[(X_val, y_val)],
    callbacks=[lgb.early_stopping(50), lgb.log_evaluation(100)]
)

# Predict
predictions = lgb_model.predict(X_test)
```

### 6.5 Time Series Cross-Validation

```python
from sklearn.model_selection import TimeSeriesSplit

def time_series_cv(model, X, y, n_splits=5):
    tscv = TimeSeriesSplit(n_splits=n_splits)
    scores = []
    
    for train_index, test_index in tscv.split(X):
        X_train, X_test = X[train_index], X[test_index]
        y_train, y_test = y[train_index], y[test_index]
        
        model.fit(X_train, y_train)
        predictions = model.predict(X_test)
        
        rmse = np.sqrt(mean_squared_error(y_test, predictions))
        scores.append(rmse)
        
    print(f'Average RMSE: {np.mean(scores):.4f} (+/- {np.std(scores):.4f})')
    return scores
```

---

## 7. Deep Learning Cho Time Series

### 7.1 Recurrent Neural Networks (RNN)

#### **Basic RNN Architecture**

**Đặc điểm:**
- Có "memory" để nhớ thông tin quá khứ
- Share weights across time steps
- Xử lý sequential data

**Vấn đề:**
- Vanishing gradient problem
- Không thể học long-term dependencies

```python
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import SimpleRNN, Dense

# Prepare data
def create_sequences(data, seq_length):
    X, y = [], []
    for i in range(len(data) - seq_length):
        X.append(data[i:i+seq_length])
        y.append(data[i+seq_length])
    return np.array(X), np.array(y)

seq_length = 10
X, y = create_sequences(scaled_data, seq_length)

# Reshape for RNN: [samples, time steps, features]
X = X.reshape((X.shape[0], X.shape[1], 1))

# Build RNN model
model = Sequential([
    SimpleRNN(50, activation='relu', input_shape=(seq_length, 1)),
    Dense(1)
])

model.compile(optimizer='adam', loss='mse')
model.fit(X_train, y_train, epochs=50, batch_size=32, validation_split=0.2)
```

### 7.2 Long Short-Term Memory (LSTM)

#### **LSTM Architecture**

**Giải quyết vấn đề của RNN:**
- Cell state để lưu trữ long-term memory
- Gates để control information flow:
  - **Forget gate:** Quyết định thông tin nào bỏ
  - **Input gate:** Quyết định thông tin nào thêm vào
  - **Output gate:** Quyết định output gì

**Công thức:**
```
f_t = σ(W_f·[h_{t-1}, x_t] + b_f)     # Forget gate
i_t = σ(W_i·[h_{t-1}, x_t] + b_i)     # Input gate
C̃_t = tanh(W_C·[h_{t-1}, x_t] + b_C)  # Candidate
C_t = f_t * C_{t-1} + i_t * C̃_t      # Cell state
o_t = σ(W_o·[h_{t-1}, x_t] + b_o)     # Output gate
h_t = o_t * tanh(C_t)                 # Hidden state
```

#### **LSTM Implementation**

```python
from tensorflow.keras.layers import LSTM, Dropout, BatchNormalization

# Vanilla LSTM
model = Sequential([
    LSTM(50, activation='relu', input_shape=(seq_length, n_features)),
    Dense(1)
])

# Stacked LSTM
model = Sequential([
    LSTM(50, activation='relu', return_sequences=True, input_shape=(seq_length, n_features)),
    Dropout(0.2),
    LSTM(50, activation='relu', return_sequences=True),
    Dropout(0.2),
    LSTM(50, activation='relu'),
    Dropout(0.2),
    Dense(1)
])

model.compile(optimizer='adam', loss='mse', metrics=['mae'])

# Training with callbacks
from tensorflow.keras.callbacks import EarlyStopping, ModelCheckpoint, ReduceLROnPlateau

early_stop = EarlyStopping(monitor='val_loss', patience=10, restore_best_weights=True)
checkpoint = ModelCheckpoint('best_model.h5', monitor='val_loss', save_best_only=True)
reduce_lr = ReduceLROnPlateau(monitor='val_loss', factor=0.5, patience=5)

history = model.fit(
    X_train, y_train,
    epochs=100,
    batch_size=32,
    validation_split=0.2,
    callbacks=[early_stop, checkpoint, reduce_lr],
    verbose=1
)
```

#### **Bidirectional LSTM**

```python
from tensorflow.keras.layers import Bidirectional

# Bidirectional LSTM
model = Sequential([
    Bidirectional(LSTM(50, return_sequences=True), input_shape=(seq_length, n_features)),
    Dropout(0.2),
    Bidirectional(LSTM(50)),
    Dropout(0.2),
    Dense(1)
])
```

### 7.3 Gated Recurrent Unit (GRU)

**Đơn giản hóa LSTM:**
- Chỉ có 2 gates (update gate, reset gate)
- Ít parameters hơn LSTM
- Train nhanh hơn
- Performance tương đương LSTM

```python
from tensorflow.keras.layers import GRU

# GRU model
model = Sequential([
    GRU(50, activation='relu', return_sequences=True, input_shape=(seq_length, n_features)),
    Dropout(0.2),
    GRU(50, activation='relu'),
    Dropout(0.2),
    Dense(1)
])

model.compile(optimizer='adam', loss='mse')
model.fit(X_train, y_train, epochs=50, batch_size=32, validation_split=0.2)
```

### 7.4 Convolutional Neural Networks (CNN) for Time Series

**1D CNN cho Time Series:**
- Trích xuất local patterns
- Ít parameters hơn RNN
- Train nhanh hơn
- Tốt cho multi-step forecasting

```python
from tensorflow.keras.layers import Conv1D, MaxPooling1D, Flatten

# 1D CNN model
model = Sequential([
    Conv1D(filters=64, kernel_size=3, activation='relu', input_shape=(seq_length, n_features)),
    MaxPooling1D(pool_size=2),
    Conv1D(filters=32, kernel_size=3, activation='relu'),
    MaxPooling1D(pool_size=2),
    Flatten(),
    Dense(50, activation='relu'),
    Dropout(0.2),
    Dense(1)
])

model.compile(optimizer='adam', loss='mse')
```

### 7.5 CNN-LSTM Hybrid

**Kết hợp ưu điểm:**
- CNN: Feature extraction
- LSTM: Sequence learning

```python
# CNN-LSTM Hybrid
model = Sequential([
    Conv1D(filters=64, kernel_size=3, activation='relu', input_shape=(seq_length, n_features)),
    MaxPooling1D(pool_size=2),
    Conv1D(filters=32, kernel_size=3, activation='relu'),
    MaxPooling1D(pool_size=2),
    LSTM(50, activation='relu'),
    Dropout(0.2),
    Dense(1)
])
```

### 7.6 Encoder-Decoder Architecture

**Cho Multi-Step Forecasting:**

```python
from tensorflow.keras.layers import RepeatVector, TimeDistributed

# Encoder-Decoder model
n_future = 7  # Forecast 7 steps ahead

# Encoder
encoder_inputs = tf.keras.Input(shape=(seq_length, n_features))
encoder_lstm = LSTM(50, return_state=True)
encoder_outputs, state_h, state_c = encoder_lstm(encoder_inputs)
encoder_states = [state_h, state_c]

# Decoder
decoder_inputs = RepeatVector(n_future)(encoder_outputs)
decoder_lstm = LSTM(50, return_sequences=True)
decoder_outputs = decoder_lstm(decoder_inputs, initial_state=encoder_states)
decoder_dense = TimeDistributed(Dense(1))
decoder_outputs = decoder_dense(decoder_outputs)

# Model
model = tf.keras.Model(encoder_inputs, decoder_outputs)
model.compile(optimizer='adam', loss='mse')
```

### 7.7 Attention Mechanism

```python
from tensorflow.keras.layers import Layer

class AttentionLayer(Layer):
    def __init__(self, **kwargs):
        super(AttentionLayer, self).__init__(**kwargs)
    
    def build(self, input_shape):
        self.W = self.add_weight(
            name='attention_weight',
            shape=(input_shape[-1], input_shape[-1]),
            initializer='glorot_uniform',
            trainable=True
        )
        self.b = self.add_weight(
            name='attention_bias',
            shape=(input_shape[-1],),
            initializer='zeros',
            trainable=True
        )
        super(AttentionLayer, self).build(input_shape)
    
    def call(self, x):
        e = tf.keras.backend.tanh(tf.keras.backend.dot(x, self.W) + self.b)
        a = tf.keras.backend.softmax(e, axis=1)
        output = x * a
        return tf.keras.backend.sum(output, axis=1)

# LSTM with Attention
model = Sequential([
    LSTM(50, return_sequences=True, input_shape=(seq_length, n_features)),
    AttentionLayer(),
    Dense(1)
])
```

### 7.8 Transformer for Time Series

```python
from tensorflow.keras.layers import MultiHeadAttention, LayerNormalization

def transformer_encoder(inputs, head_size, num_heads, ff_dim, dropout=0):
    # Attention
    x = MultiHeadAttention(
        key_dim=head_size, num_heads=num_heads, dropout=dropout
    )(inputs, inputs)
    x = Dropout(dropout)(x)
    x = LayerNormalization(epsilon=1e-6)(x)
    res = x + inputs
    
    # Feed Forward
    x = tf.keras.layers.Conv1D(filters=ff_dim, kernel_size=1, activation="relu")(res)
    x = Dropout(dropout)(x)
    x = tf.keras.layers.Conv1D(filters=inputs.shape[-1], kernel_size=1)(x)
    x = LayerNormalization(epsilon=1e-6)(x)
    return x + res

# Build Transformer model
inputs = tf.keras.Input(shape=(seq_length, n_features))
x = inputs
x = transformer_encoder(x, head_size=256, num_heads=4, ff_dim=4, dropout=0.1)
x = transformer_encoder(x, head_size=256, num_heads=4, ff_dim=4, dropout=0.1)
x = tf.keras.layers.GlobalAveragePooling1D()(x)
x = Dropout(0.1)(x)
x = Dense(50, activation="relu")(x)
x = Dropout(0.1)(x)
outputs = Dense(1)(x)

model = tf.keras.Model(inputs, outputs)
```

### 7.9 Advanced: Temporal Convolutional Network (TCN)

```python
from tensorflow.keras.layers import Conv1D, Dropout, Add, Activation

def residual_block(x, dilation_rate, nb_filters, kernel_size, padding='causal'):
    # Dilated convolution
    prev_x = x
    x = Conv1D(filters=nb_filters, kernel_size=kernel_size,
               dilation_rate=dilation_rate, padding=padding)(x)
    x = Activation('relu')(x)
    x = Dropout(0.2)(x)
    
    x = Conv1D(filters=nb_filters, kernel_size=kernel_size,
               dilation_rate=dilation_rate, padding=padding)(x)
    x = Activation('relu')(x)
    x = Dropout(0.2)(x)
    
    # Skip connection
    if prev_x.shape[-1] != nb_filters:
        prev_x = Conv1D(filters=nb_filters, kernel_size=1)(prev_x)
    
    res_x = Add()([prev_x, x])
    return Activation('relu')(res_x)

# TCN Model
inputs = tf.keras.Input(shape=(seq_length, n_features))
x = residual_block(inputs, dilation_rate=1, nb_filters=32, kernel_size=3)
x = residual_block(x, dilation_rate=2, nb_filters=32, kernel_size=3)
x = residual_block(x, dilation_rate=4, nb_filters=32, kernel_size=3)
x = residual_block(x, dilation_rate=8, nb_filters=32, kernel_size=3)
x = tf.keras.layers.GlobalAveragePooling1D()(x)
outputs = Dense(1)(x)

model = tf.keras.Model(inputs, outputs)
```

---

## 8. Kỹ Thuật Nâng Cao

### 8.1 Prophet (Facebook)

**Đặc điểm:**
- Xử lý missing data tốt
- Xử lý outliers tốt
- Xử lý multiple seasonality
- Dễ sử dụng

```python
from fbprophet import Prophet

# Prepare data
df = pd.DataFrame({
    'ds': data.index,  # Date column
    'y': data['value']  # Value column
})

# Create model
model = Prophet(
    yearly_seasonality=True,
    weekly_seasonality=True,
    daily_seasonality=False,
    seasonality_mode='multiplicative'
)

# Add custom seasonality
model.add_seasonality(name='monthly', period=30.5, fourier_order=5)

# Add holidays
holidays = pd.DataFrame({
    'holiday': 'holiday_name',
    'ds': pd.to_datetime(['2023-01-01', '2023-12-25']),
    'lower_window': 0,
    'upper_window': 1,
})
model.holidays = holidays

# Fit model
model.fit(df)

# Make future dataframe
future = model.make_future_dataframe(periods=30)

# Predict
forecast = model.predict(future)

# Plot
model.plot(forecast)
model.plot_components(forecast)
```

### 8.2 N-BEATS (Neural Basis Expansion Analysis)

```python
# Requires: pip install nbeats-pytorch

from nbeats_pytorch.model import NBeatsNet

# Model
model = NBeatsNet(
    stack_types=[NBeatsNet.GENERIC_BLOCK, NBeatsNet.GENERIC_BLOCK],
    forecast_length=forecast_horizon,
    backcast_length=lookback_window,
    hidden_layer_units=128
)

# Train
optimizer = torch.optim.Adam(model.parameters())
criterion = torch.nn.MSELoss()

for epoch in range(100):
    optimizer.zero_grad()
    backcast, forecast = model(torch.tensor(X_train))
    loss = criterion(forecast, torch.tensor(y_train))
    loss.backward()
    optimizer.step()
```

### 8.3 Ensemble Methods

#### **A. Simple Averaging**
```python
# Multiple models
pred_arima = arima_model.forecast(steps=12)
pred_lstm = lstm_model.predict(X_test)
pred_xgb = xgb_model.predict(X_test)

# Average
ensemble_pred = (pred_arima + pred_lstm + pred_xgb) / 3
```

#### **B. Weighted Average**
```python
# Based on validation performance
weights = np.array([0.3, 0.5, 0.2])  # ARIMA, LSTM, XGBoost
ensemble_pred = (weights[0] * pred_arima + 
                weights[1] * pred_lstm + 
                weights[2] * pred_xgb)
```

#### **C. Stacking**
```python
from sklearn.ensemble import StackingRegressor
from sklearn.linear_model import Ridge

# Base models
estimators = [
    ('arima', arima_model),
    ('xgb', xgb_model),
    ('lgb', lgb_model)
]

# Meta-learner
stacking_model = StackingRegressor(
    estimators=estimators,
    final_estimator=Ridge()
)

stacking_model.fit(X_train, y_train)
predictions = stacking_model.predict(X_test)
```

### 8.4 Multi-Step Forecasting Strategies

#### **A. Recursive (Iterative)**
```python
def recursive_forecast(model, X_initial, steps):
    predictions = []
    X_current = X_initial.copy()
    
    for _ in range(steps):
        pred = model.predict(X_current.reshape(1, -1))[0]
        predictions.append(pred)
        
        # Update X for next prediction
        X_current = np.roll(X_current, -1)
        X_current[-1] = pred
    
    return np.array(predictions)
```

#### **B. Direct (Independent)**
```python
# Train separate model for each horizon
models = {}
for h in range(1, forecast_horizon + 1):
    y_h = data.shift(-h)  # Target at horizon h
    model_h = RandomForestRegressor()
    model_h.fit(X_train, y_h[train_indices])
    models[h] = model_h

# Predict
predictions = []
for h in range(1, forecast_horizon + 1):
    pred_h = models[h].predict(X_test)
    predictions.append(pred_h)
```

#### **C. Multi-Output**
```python
from sklearn.multioutput import MultiOutputRegressor

# Create multi-output target
y_multi = np.column_stack([data.shift(-i) for i in range(1, forecast_horizon+1)])

# Model
multi_model = MultiOutputRegressor(RandomForestRegressor())
multi_model.fit(X_train, y_multi[train_indices])

# Predict all horizons at once
predictions = multi_model.predict(X_test)
```

### 8.5 Anomaly Detection

```python
# Using Isolation Forest
from sklearn.ensemble import IsolationForest

iso_forest = IsolationForest(contamination=0.1, random_state=42)
anomalies = iso_forest.fit_predict(data[['value']])

# Using Z-score
from scipy import stats

z_scores = np.abs(stats.zscore(data['value']))
anomalies = z_scores > 3

# Using Prophet
model = Prophet()
model.fit(df)
forecast = model.predict(df)

# Calculate residuals
df['residual'] = df['y'] - forecast['yhat']
df['anomaly'] = np.abs(df['residual']) > (3 * forecast['yhat_upper'] - forecast['yhat_lower'])
```

### 8.6 Transfer Learning

```python
# Pre-train on similar dataset
base_model = Sequential([
    LSTM(100, return_sequences=True, input_shape=(seq_length, n_features)),
    LSTM(50),
    Dense(1)
])

# Train on source dataset
base_model.fit(X_source, y_source, epochs=50)

# Freeze early layers
for layer in base_model.layers[:-2]:
    layer.trainable = False

# Fine-tune on target dataset
base_model.fit(X_target, y_target, epochs=20)
```

---

## 9. Ứng Dụng Thực Tế

### 9.1 Sales Forecasting

```python
# Complete pipeline
import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
from xgboost import XGBRegressor

# Load data
data = pd.read_csv('sales_data.csv', parse_dates=['date'])
data.set_index('date', inplace=True)

# Feature engineering
def create_features(df):
    df = df.copy()
    
    # Date features
    df['dayofweek'] = df.index.dayofweek
    df['quarter'] = df.index.quarter
    df['month'] = df.index.month
    df['year'] = df.index.year
    df['dayofyear'] = df.index.dayofyear
    df['dayofmonth'] = df.index.day
    df['weekofyear'] = df.index.isocalendar().week
    
    # Lag features
    for lag in [1, 7, 14, 21, 28]:
        df[f'lag_{lag}'] = df['sales'].shift(lag)
    
    # Rolling features
    for window in [7, 14, 28]:
        df[f'rolling_mean_{window}'] = df['sales'].rolling(window).mean()
        df[f'rolling_std_{window}'] = df['sales'].rolling(window).std()
    
    return df

data = create_features(data)
data = data.dropna()

# Train-test split
split_date = '2023-01-01'
train = data[data.index < split_date]
test = data[data.index >= split_date]

# Prepare X, y
feature_cols = [col for col in data.columns if col != 'sales']
X_train = train[feature_cols]
y_train = train['sales']
X_test = test[feature_cols]
y_test = test['sales']

# Model
model = XGBRegressor(n_estimators=1000, learning_rate=0.01)
model.fit(X_train, y_train, 
          eval_set=[(X_test, y_test)],
          early_stopping_rounds=50,
          verbose=False)

# Predict
predictions = model.predict(X_test)

# Evaluate
from sklearn.metrics import mean_absolute_error, mean_squared_error
print(f'MAE: {mean_absolute_error(y_test, predictions):.2f}')
print(f'RMSE: {np.sqrt(mean_squared_error(y_test, predictions)):.2f}')
```

### 9.2 Stock Price Prediction

```python
# Using LSTM for stock prediction
import yfinance as yf

# Download data
ticker = 'AAPL'
data = yf.download(ticker, start='2020-01-01', end='2023-12-31')

# Use Close price
prices = data['Close'].values.reshape(-1, 1)

# Scale
from sklearn.preprocessing import MinMaxScaler
scaler = MinMaxScaler()
scaled_prices = scaler.fit_transform(prices)

# Create sequences
def create_sequences(data, seq_length):
    X, y = [], []
    for i in range(len(data) - seq_length):
        X.append(data[i:i+seq_length])
        y.append(data[i+seq_length])
    return np.array(X), np.array(y)

seq_length = 60
X, y = create_sequences(scaled_prices, seq_length)

# Split
train_size = int(len(X) * 0.8)
X_train, X_test = X[:train_size], X[train_size:]
y_train, y_test = y[:train_size], y[train_size:]

# LSTM Model
model = Sequential([
    LSTM(50, return_sequences=True, input_shape=(seq_length, 1)),
    Dropout(0.2),
    LSTM(50, return_sequences=True),
    Dropout(0.2),
    LSTM(50),
    Dropout(0.2),
    Dense(1)
])

model.compile(optimizer='adam', loss='mse')
model.fit(X_train, y_train, epochs=50, batch_size=32, validation_split=0.1)

# Predict
predictions = model.predict(X_test)
predictions = scaler.inverse_transform(predictions)
```

### 9.3 Demand Forecasting

```python
# Using Prophet for demand forecasting
from fbprophet import Prophet

# Prepare data
df = pd.DataFrame({
    'ds': demand_data.index,
    'y': demand_data['demand']
})

# Add regressors (additional features)
df['promotion'] = demand_data['promotion']
df['price'] = demand_data['price']

# Model
model = Prophet()
model.add_regressor('promotion')
model.add_regressor('price')
model.add_seasonality(name='monthly', period=30.5, fourier_order=5)

# Fit
model.fit(df)

# Future dataframe
future = model.make_future_dataframe(periods=30)
future['promotion'] = future_promotion_data
future['price'] = future_price_data

# Forecast
forecast = model.predict(future)
```

### 9.4 Energy Consumption Forecasting

```python
# Multi-variate time series
features = ['temperature', 'humidity', 'hour', 'dayofweek', 'holiday']
target = 'energy_consumption'

# LSTM for multivariate
n_features = len(features)
X = data[features].values
y = data[target].values

# Scale
from sklearn.preprocessing import StandardScaler
scaler_X = StandardScaler()
scaler_y = StandardScaler()

X_scaled = scaler_X.fit_transform(X)
y_scaled = scaler_y.fit_transform(y.reshape(-1, 1))

# Sequences
X_seq, y_seq = create_sequences(X_scaled, y_scaled, seq_length=24)

# Model
model = Sequential([
    LSTM(100, return_sequences=True, input_shape=(24, n_features)),
    Dropout(0.2),
    LSTM(50),
    Dropout(0.2),
    Dense(1)
])

model.compile(optimizer='adam', loss='mse')
model.fit(X_seq, y_seq, epochs=50, batch_size=32)
```

---

## 10. Best Practices & Tips

### 10.1 Data Preparation

**✅ DO:**
- Handle missing values appropriately (forward fill, interpolation)
- Check for and handle outliers
- Ensure consistent frequency
- Scale/normalize features for deep learning
- Use proper train-test split (temporal)

**❌ DON'T:**
- Use random train-test split
- Look ahead in your features (data leakage)
- Use future information to predict past

### 10.2 Feature Engineering

**Tips:**
- Create lag features based on domain knowledge
- Add calendar features (holidays, weekends)
- Include external factors (weather, events)
- Use rolling statistics
- Create interaction features

### 10.3 Model Selection

**Guidelines:**
- **Simple patterns:** Moving Average, Exponential Smoothing
- **Linear trends:** ARIMA, SARIMA
- **Complex patterns:** Machine Learning (XGBoost, LightGBM)
- **Long sequences:** Deep Learning (LSTM, GRU)
- **Multiple seasonalities:** Prophet
- **Short training data:** Transfer Learning

### 10.4 Validation Strategy

```python
# Time Series Cross-Validation
from sklearn.model_selection import TimeSeriesSplit

tscv = TimeSeriesSplit(n_splits=5)

for train_index, test_index in tscv.split(X):
    X_train, X_test = X[train_index], X[test_index]
    y_train, y_test = y[train_index], y[test_index]
    
    model.fit(X_train, y_train)
    score = model.score(X_test, y_test)
    print(f'Score: {score}')
```

### 10.5 Hyperparameter Tuning

```python
from sklearn.model_selection import GridSearchCV, TimeSeriesSplit

param_grid = {
    'n_estimators': [100, 200, 300],
    'max_depth': [5, 10, 15],
    'learning_rate': [0.01, 0.05, 0.1]
}

tscv = TimeSeriesSplit(n_splits=3)

grid_search = GridSearchCV(
    estimator=XGBRegressor(),
    param_grid=param_grid,
    cv=tscv,
    scoring='neg_mean_squared_error',
    n_jobs=-1
)

grid_search.fit(X_train, y_train)
best_model = grid_search.best_estimator_
```

### 10.6 Debugging Checklist

1. **Check data quality:**
   - Missing values?
   - Outliers?
   - Correct data types?

2. **Check stationarity:**
   - Run ADF test
   - Apply differencing if needed

3. **Check model assumptions:**
   - Residuals are white noise?
   - No autocorrelation in residuals?

4. **Check for overfitting:**
   - Compare train vs test error
   - Use cross-validation
   - Add regularization

5. **Check predictions:**
   - Make sense domain-wise?
   - Within reasonable range?

### 10.7 Production Considerations

**Monitoring:**
```python
# Track model performance over time
def monitor_model(predictions, actuals, threshold=0.1):
    mape = np.mean(np.abs((actuals - predictions) / actuals))
    
    if mape > threshold:
        print(f"⚠️ WARNING: MAPE {mape:.2%} exceeds threshold {threshold:.2%}")
        print("Consider retraining the model")
    
    return mape

# Log predictions
import logging

logging.basicConfig(filename='predictions.log', level=logging.INFO)
logging.info(f'Prediction at {datetime.now()}: {prediction}')
```

**Retraining Strategy:**
- Set schedule (weekly, monthly)
- Monitor drift in predictions
- Retrain when performance degrades

### 10.8 Common Pitfalls

**1. Data Leakage:**
```python
# ❌ WRONG: Using future information
df['lag_1'] = df['value'].shift(-1)  # This leaks future!

# ✅ CORRECT: Using past information
df['lag_1'] = df['value'].shift(1)
```

**2. Scale After Split:**
```python
# ❌ WRONG
scaler.fit(all_data)
train_scaled = scaler.transform(train)
test_scaled = scaler.transform(test)

# ✅ CORRECT
scaler.fit(train)
train_scaled = scaler.transform(train)
test_scaled = scaler.transform(test)
```

**3. Using Accuracy for Regression:**
```python
# ❌ WRONG
from sklearn.metrics import accuracy_score

# ✅ CORRECT
from sklearn.metrics import mean_absolute_error, mean_squared_error
```

---

## 📚 Tài Liệu Tham Khảo

### Sách Nên Đọc:
1. **"Forecasting: Principles and Practice"** - Rob J Hyndman & George Athanasopoulos
2. **"Time Series Analysis and Its Applications"** - Robert H. Shumway & David S. Stoffer
3. **"Deep Learning for Time Series Forecasting"** - Jason Brownlee

### Online Courses:
1. **Coursera:** "Sequences, Time Series and Prediction" by Laurence Moroney
2. **Udacity:** "Time Series Forecasting"
3. **Fast.ai:** "Practical Deep Learning for Coders"

### Libraries:
- **statsmodels:** Classical time series methods
- **pmdarima:** Auto ARIMA
- **fbprophet:** Facebook Prophet
- **TensorFlow/Keras:** Deep learning
- **PyTorch:** Deep learning
- **sktime:** Unified framework for time series

---

## 💡 Tổng Kết

### Key Takeaways:

1. **Understand your data:**
   - Check stationarity
   - Identify patterns (trend, seasonality)
   - Handle missing values and outliers

2. **Start simple:**
   - Try classical methods first (ARIMA, Prophet)
   - Use ML/DL when patterns are complex

3. **Feature engineering is crucial:**
   - Lag features
   - Rolling statistics
   - Calendar features

4. **Proper validation:**
   - Use TimeSeriesSplit
   - Never shuffle time series data
   - Avoid data leakage

5. **Iterate and improve:**
   - Try multiple models
   - Ensemble predictions
   - Monitor performance in production

### Workflow Tổng Quát:

```
1. Data Collection & Exploration
   ↓
2. Data Preprocessing & Cleaning
   ↓
3. Stationarity Check & Transform
   ↓
4. Feature Engineering
   ↓
5. Model Selection & Training
   ↓
6. Validation & Evaluation
   ↓
7. Hyperparameter Tuning
   ↓
8. Final Model & Deployment
   ↓
9. Monitoring & Maintenance
```

---

*Chúc bạn học tốt! Nếu có câu hỏi, đừng ngại đặt câu hỏi. Time series analysis là một lĩnh vực rộng lớn và đòi hỏi nhiều practice. Keep learning and experimenting! 🚀*
