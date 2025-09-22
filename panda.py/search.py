import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
df = pd.read_csv('country_full.csv')  # Read the CSV file into a Pandas DataFrame

# Display basic information about the dataset
print("Dataset Information:")
df.info()  # Provides the number of entries, column names, and data types of each column

# Display the first few rows of the dataset
print("\nFirst few rows:")
print(df.head())  # Displays the first 5 rows to understand the initial structure

# Display summary statistics for numeric columns
print("\nSummary statistics:")
print(df.describe())  # Summary statistics like mean, std, min, max, etc., for numeric columns

# Check for missing values in each column
print("\nMissing values per column:")
print(df.isnull().sum())  # Counts how many missing values are present in each column

# Display the unique values for each column
print("\nUnique values per column:")
for column in df.columns:  # Loops through all columns
    print(f"{column}: {df[column].nunique()} unique values")  # Prints the number of unique values per column

# Check the data types of all columns
print("\nColumn Data Types:")
print(df.dtypes)  # Displays the data types of each column (e.g., int64, float64, object)

# Visualize missing values using a heatmap
plt.figure(figsize=(10, 6))  # Set the figure size
sns.heatmap(df.isnull(), cbar=False, cmap='viridis')  # Creates a heatmap to visually show missing values
plt.title("Missing Values Heatmap")  # Title for the heatmap
plt.show()  # Displays the plot

# Visualize the distribution of a sample numeric column (e.g., 'country-code')
if 'country-code' in df.columns:  # Check if the 'country-code' column exists
    plt.figure(figsize=(10, 6))  # Set the figure size
    sns.histplot(df['country-code'], kde=True, bins=30, color='blue')  # Histogram of 'country-code' with a Kernel Density Estimate (KDE)
    plt.title("Distribution of 'country-code'")  # Title for the histogram
    plt.xlabel("Country Code")  # Label for the x-axis
    plt.ylabel("Frequency")  # Label for the y-axis
    plt.show()  # Displays the plot

# Visualize the distribution of a sample categorical column (e.g., 'region')
if 'region' in df.columns:  # Check if the 'region' column exists
    plt.figure(figsize=(10, 6))  # Set the figure size
    sns.countplot(data=df, x='region', palette='viridis', order=df['region'].value_counts().index)  # Count plot of 'region'
    plt.title("Distribution of 'region'")  # Title for the count plot
    plt.xlabel("Region")  # Label for the x-axis
    plt.ylabel("Count")  # Label for the y-axis
    plt.xticks(rotation=45)  # Rotate x-axis labels to avoid overlap
    plt.show()  # Displays the plot

# Correlation heatmap for numeric columns
plt.figure(figsize=(12, 8))  # Set the figure size
correlation = df.corr(numeric_only=True)  # Compute the correlation matrix for numeric columns
sns.heatmap(correlation, annot=True, cmap='coolwarm', fmt='.2f')  # Create a heatmap with annotations of correlation values
plt.title("Correlation Heatmap")  # Title for the correlation heatmap
plt.show()  # Displays the plot

# Pairplot for numeric columns (sample visualization)
plt.figure()  # Create a new figure
sns.pairplot(df.select_dtypes(include=['float64', 'int64']), diag_kind='kde', corner=True)  # Pairplot for numeric columns
plt.suptitle("Pairplot of Numeric Columns", y=1.02)  # Title for the pairplot
plt.show()  # Displays the plot
