def get_summary(df):
    
    return {
        "Rows": df.shape[0],
        "Columns": df.shape[1],
        "Missing Values Percentage": df.isnull().sum().sum()/df.shape[0]*100,
        "Duplicate Values": df.duplicated().sum(),
        "Data Types": df.dtypes,
        "Unique Values": df.nunique()
}
def get_statistical_summary(df):
    return df.describe()

def get_correlation_matrix(df):
    return df.corr(numeric_only=True)

def get_column_summary(df):
    summary = {}
    for col in df.columns:
        summary[col] = {
            "Data Type": df[col].dtype,
            "Missing Values": df[col].isnull().sum(),
            "Unique Values": df[col].nunique(),
            "Top Values": df[col].value_counts().head(5)
        }
    return summary
def get_row_summary(df):
    summary = {}
    for col in df.columns:
        summary[col] = {
            "Data Type": df[col].dtype,
            "Missing Values": df[col].isnull().sum(),
            "Unique Values": df[col].nunique(),
            "Top Values": df[col].value_counts().head(5)
        }
    return summary

    