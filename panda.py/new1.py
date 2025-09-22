# Importing necessary libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
df = pd.read_csv('country_full.csv')

# Display basic information about the dataset
print("Dataset Information:")
df.info()  # Gives the number of non-null entries, data types, and memory usage

# Display the first few rows of the dataset
print("\nFirst few rows:")
print(df.head())  # Displays the first 5 rows of the dataset to give an initial look

# Display summary statistics for numeric columns
print("\nSummary statistics:")
print(df.describe())  # Provides statistics like mean, std, min, max, etc., for numeric columns

# Check for missing values in each column
print("\nMissing values per column:")
print(df.isnull().sum())  # Summarizes the count of missing (NaN) values in each column

# Handle missing values: Drop rows with missing values or fill with mean
df_cleaned = df.dropna()  # Alternatively, df.fillna(df.mean(), inplace=True) could be used to fill with mean

# Handle duplicates (if any)
df_cleaned = df_cleaned.drop_duplicates()  # Removes any duplicate rows from the dataset

# Display cleaned dataframe info
print(f"\nCleaned DataFrame Information (after handling missing values and duplicates):")
df_cleaned.info()  # Shows updated info after cleaning the dataset

# Visualize missing values using a heatmap
plt.figure(figsize=(10, 6))
sns.heatmap(df.isnull(), cbar=False, cmap='viridis')  # Visualizes missing values with a heatmap
plt.title("Missing Values Heatmap")
plt.show()  # Displays the heatmap

# Visualize the distribution of a sample numeric column (e.g., 'country-code')
if 'country-code' in df.columns:
    plt.figure(figsize=(10, 6))
    sns.histplot(df['country-code'], kde=True, bins=30, color='blue')  # Distribution of country-code column
    plt.title("Distribution of 'country-code'")
    plt.xlabel("Country Code")
    plt.ylabel("Frequency")
    plt.show()  # Displays the histogram with Kernel Density Estimation (KDE)

# Visualize the distribution of a sample categorical column (e.g., 'region')
if 'region' in df.columns:
    plt.figure(figsize=(10, 6))
    sns.countplot(data=df, x='region', palette='viridis', order=df['region'].value_counts().index)  # Countplot for region
    plt.title("Distribution of 'region'")
    plt.xlabel("Region")
    plt.ylabel("Count")
    plt.xticks(rotation=45)  # Rotates x-axis labels for readability
    plt.show()  # Displays the count plot

# Correlation heatmap for numeric columns
plt.figure(figsize=(12, 8))
correlation = df.corr(numeric_only=True)  # Calculates correlation matrix for numeric columns
sns.heatmap(correlation, annot=True, cmap='coolwarm', fmt='.2f')  # Visualizes correlation with annotations
plt.title("Correlation Heatmap")
plt.show()  # Displays the heatmap

# Pairplot for numeric columns (explores relationships between multiple numeric features)
plt.figure()
sns.pairplot(df.select_dtypes(include=['float64', 'int64']), diag_kind='kde', corner=True)  # Pairplot for numeric columns
plt.suptitle("Pairplot of Numeric Columns", y=1.02)  # Adds a title to the pairplot
plt.show()  # Displays the pairplot

# Data Transformation: Scaling and Encoding
scaler = StandardScaler()  # Initialize StandardScaler for scaling
df['scaled_column'] = scaler.fit_transform(df[['numeric_column']])  # Scale the 'numeric_column'

encoder = LabelEncoder()  # Initialize LabelEncoder for encoding categorical variables
df['encoded_region'] = encoder.fit_transform(df['region'])  # Encode the 'region' column

# Handle outliers using the Interquartile Range (IQR) method
Q1 = df['numeric_column'].quantile(0.25)  # Calculate the first quartile (25th percentile)
Q3 = df['numeric_column'].quantile(0.75)  # Calculate the third quartile (75th percentile)
IQR = Q3 - Q1  # Interquartile range
lower_bound = Q1 - 1.5 * IQR  # Lower bound for detecting outliers
upper_bound = Q3 + 1.5 * IQR  # Upper bound for detecting outliers
df_no_outliers = df[(df['numeric_column'] >= lower_bound) & (df['numeric_column'] <= upper_bound)]  # Filter out outliers

# Display data after removing outliers
print(f"\nData after removing outliers:")
print(df_no_outliers[['numeric_column']].describe())  # Shows updated stats after removing outliers

# Visualizing outliers using a Violin plot (distribution comparison)
if 'region' in df.columns and 'numeric_column' in df.columns:
    plt.figure(figsize=(10, 6))
    sns.violinplot(data=df, x='region', y='numeric_column', palette='viridis')  # Violin plot to compare distributions
    plt.title("Violin Plot: Numeric Column by Region")
    plt.xlabel("Region")
    plt.ylabel("Numeric Column")
    plt.xticks(rotation=45)
    plt.show()  # Displays the violin plot

# Visualizing outliers using a Boxplot (another method of outlier detection)
plt.figure(figsize=(10, 6))
sns.boxplot(data=df, x='region', y='numeric_column', palette='viridis')  # Boxplot for numeric column by region
plt.title("Boxplot: Numeric Column by Region")
plt.xlabel("Region")
plt.ylabel("Numeric Column")
plt.xticks(rotation=45)
plt.show()  # Displays the boxplot

# Feature Engineering: Creating new features based on existing ones
df['new_feature'] = df['numeric_column'] * df['scaled_column']  # New feature by multiplying numeric_column and scaled_column

# Hypothesis Testing: T-test to compare means between two groups
group1 = df[df['region'] == 'Group1']['numeric_column']  # Select data for 'Group1'
group2 = df[df['region'] == 'Group2']['numeric_column']  # Select data for 'Group2'
t_stat, p_value = stats.ttest_ind(group1, group2)  # Perform t-test between the two groups
print(f"\nT-test result: t-statistic = {t_stat}, p-value = {p_value}")
# Based on p-value, we can conclude if the difference is statistically significant (p < 0.05 is significant)

# Applying a simple machine learning model: Linear Regression
X = df[['scaled_column', 'new_feature']]  # Independent variables (predictors)
y = df['numeric_column']  # Dependent variable (target)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)  # Split data into train/test sets

model = LinearRegression()  # Initialize a Linear Regression model
model.fit(X_train, y_train)  # Train the model on the training data

# Make predictions and evaluate the model
y_pred = model.predict(X_test)  # Predict using the test data
mse = mean_squared_error(y_test, y_pred)  # Calculate Mean Squared Error (MSE)
print(f"\nModel Mean Squared Error: {mse}")  # Display MSE for model evaluation

# Feature importance visualization for the linear regression model
importances = model.coef_  # Get the coefficients (importance) of the features in the model
features = X.columns  # List of feature names
feature_importance = pd.DataFrame({'Feature': features, 'Importance': importances})  # Create DataFrame for importance
feature_importance = feature_importance.sort_values(by='Importance', ascending=False)  # Sort by importance

# Visualize feature importance
plt.figure(figsize=(10, 6))
sns.barplot(x='Importance', y='Feature', data=feature_importance, palette='viridis')  # Barplot to show feature importance
plt.title("Feature Importance")
plt.show()  # Displays the bar plot
