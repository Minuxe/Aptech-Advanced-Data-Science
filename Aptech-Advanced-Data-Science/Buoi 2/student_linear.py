from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
import pandas as pd 
import numpy as np 

df = pd.read_csv("Student_Performance.csv")
# print(df.shape)
# print(df.info())
# print(df.head())
# print(df.describe())

x = df.drop("Performance Index", axis = 1 )
y = df["Performance Index"]

# print(df.isnull().sum())
# print(df.duplicated().sum())
# print(df[df.duplicated(keep= False)])

import seaborn as sns 
import matplotlib.pyplot as plt 

sns.histplot(y , kde=True)
plt.title("Phân phối performance index")
plt.show()

plt.figure(figsize=(10,8))
sns.heatmap(x.corr(numeric_only= True), annot= False , cmap= "coolwarm")
#annot = False mean not to write the numerical value inside the colored cells
plt.title("Correlation matrix of the dataset")
plt.show()

target_corr = df.corr(numeric_only= True)['Performance Index'].drop('Performance Index')
#Correlation only works with numercial values , you cannot compare the correlation between an apple and a banana
plt.figure(figsize = (6, 10))
sns.barplot(x=target_corr.index, y=target_corr.values)
plt.title("Correlation of all features to the target variable")
plt.title("Correlation of every features to the target variable")
plt.tight_layout()
plt.show()

#Kết luận từ hist plot cho thấy performance index phân phối chuẩn ,
## với phần lớn  giá trị tập trung trong khoảng từ 40 đến 80, cho thấy trung bình và trung vị nằm trong khoảng đó
## Để ý ở giữa có những columns thấp hơn đáng kể so với phần giữa , có thể là do bins bắt phân phối giá trị như vậy , và cũng có thể một số điểm cụ thể ít được thể hiện hơn , có thể do cách chấm điểm 
## ta có phần tail rất mỏng, cho thấy các giá trị cực đại và cực tiểu hay những "extreme performers" ít phổ biến trong dataset 
## các giá trị giảm dần khi tiến tới performance score 100 , tránh khỏi celling effect khi mà số lượng giá trị cực đại tăng đột biến khiến khó phân biệt được sự khác biệt "performance index" trong dataset 

from sklearn.preprocessing import StandardScaler , LabelEncoder
le = LabelEncoder()
scaler = StandardScaler()

x_categorical_encoded = pd.Series(
    le.fit_transform(df['Extracurricular Activities']) ,
    name = "Extracurricular Activities",
    index = df.index
)
x_without_Extracurricular = df.drop(["Extracurricular Activities", "Performance Index"], axis = 1)
#By default , the drop is looking at rows (axis = 0) but im trying to drop the columns , so without axis = 1 , an error will show up 
x_numerical_encoded = pd.DataFrame(
    scaler.fit_transform(x_without_Extracurricular),
    columns = x_without_Extracurricular.columns,
    index = x.index
)
x_concat_encoded = pd.concat([x_numerical_encoded, x_categorical_encoded], axis = 1)


x_train, x_test, y_train, y_test = train_test_split(x_concat_encoded, y, test_size=0.2, random_state=42)
model = LinearRegression()
model.fit(x_train , y_train)
y_predict = model.predict(x_test)

print(f"The coefficient of the linear regression model f{model.coef_}")
print(f"The intercept of the linear regression model f{model.intercept_}")

r2 = r2_score(y_test , y_predict)
mae = mean_absolute_error(y_test , y_predict)
mse = mean_squared_error(y_test , y_predict)

print(f"R2 score for the linear regression model is : f{r2}")
print(f"mean absolute error index for the linear regression model is : f{mae}")
print(f"mean squared error index for the linear regression model is : f{mse}")




