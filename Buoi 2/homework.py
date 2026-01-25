import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt 
import seaborn as sns 
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score , mean_absolute_error, r2_score, mean_squared_error, confusion_matrix



df = pd.read_csv('student_performance_dataset.csv')
# print(df.info())
# print(df.head())
# print(df.describe())


df_encoded = df.drop(['Student_ID', 'Pass_Fail'], axis =1)
df_encoded = pd.get_dummies(df_encoded , columns= ['Gender', 'Internet_Access_at_Home', 'Extracurricular_Activities', 'Parental_Education_Level'], drop_first= True)
#drop_first = True vì khi tạo ra dummy columns , có nghĩa là 2 columns sẽ cùng biểu diễn dưới dạng 0 và 1 cho một giá trị 
#Và việc 2 column cùng biểu diễn 1 kết quả => có thể dùng columns này mà dự đoán columns còn lại => tăng tính đa cộng tuyến 
#Không tốt cho việc dự đoán kết quả của model linear regression , đồng thời cũng tốn data học thêm một cách vô nghĩa 
print(df.columns.tolist())

x = df_encoded
y = df['Pass_Fail']
#Mapping target variable 
y = y.map({'Pass': 1, 'Fail': 0})


sns.histplot(y, kde = True)
# The kde is a curve estimate the probability density function of your data => show the shape of the distribution without being dependent on the number of bins
plt.title("Histogram chart of the Pass/Fail target variable ")
plt.tight_layout()
plt.show()

plt.figure(figsize = (10, 8))
sns.heatmap(x.corr(numeric_only= True), annot = False , cmap = "coolwarm")
plt.title("Correlation matrix between numerical variables ")
plt.tight_layout()
plt.show()




x_train , x_test , y_train , y_test = train_test_split(x, y , test_size= 0.2 , random_state= 42)
model = LogisticRegression(max_iter = 200 , random_state= 42 )
model.fit(x_train , y_train)
y_predict = model.predict(x_test)

print("Model trained successfully")
print(f"Model coefficient f{model.coef_}")

accuracy = accuracy_score(y_test , y_predict)
print(f"Accuracy score f{accuracy:.4f}")
print(f"Accuracy percentage f{accuracy*100:.2f}%")
mae = mean_absolute_error(y_test, y_predict)
print(f"Mean absolute error score f{mae}")
mse = mean_squared_error(y_test , y_predict)
print(f"Mean squared error score f{mse}")
r2 = r2_score(y_test , y_predict)
print(f"The r2 score f{r2}")

#Confusion matrix 
cm = confusion_matrix(y_test , y_predict)
sns.heatmap(cm , annot= False , cmap= "Blues", fmt = 'd', xticklabels=['Fail', 'Pass'],
            yticklabels= ['Fail', 'Pass'])
#Fmt tell sns how to display the text inside the cell incase annot = True , fmt = 'd' stand for decimal integer
plt.title("Confusion matrix between the test and predicted value")
plt.xlabel("Predicted label")
plt.ylabel("True label")
plt.show()

#Display model coefficient 

coefficient = pd.DataFrame({
    'Feature': x.columns, 
    'Coefficient': model.coef_[0]
})
coefficient = coefficient.sort_values('Coefficient', ascending= False)
print(f"Top 10 most important coef: f{coefficient.head(10)}")
print("\n" + "=" * 50 )
print(f"Top 10 least important coef: f{coefficient.tail(10)}")
