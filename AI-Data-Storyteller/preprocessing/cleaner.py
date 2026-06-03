import pandas as pd
import numpy as np



def clean_dataset(df):
        """
        Complete preprocessing pipeline
        """

        report = {}

        # 1. Remove duplicate rows
        duplicates = df.duplicated().sum()
        df = df.drop_duplicates()
        report["duplicates_removed"] = duplicates

        # 2. Fix column names
        df.columns = (
            df.columns
            .str.strip()
            .str.lower()
            .str.replace(" ", "_")
        )

        # 3. Handle missing values
        missing_before = df.isnull().sum().sum()

        for col in df.columns:

            if df[col].dtype in ["int64", "float64"]:

                df[col] = df[col].fillna(
                    df[col].median()
                )

            else:

                mode = df[col].mode()

                if len(mode) > 0:
                    df[col] = df[col].fillna(mode[0])
                else:
                    df[col] = df[col].fillna("Unknown")

        report["missing_values_handled"] = missing_before

        # 4. Remove fully empty columns
        df = df.dropna(axis=1, how="all")

        # 5. Convert date columns automatically
        for col in df.columns:

            try:
                converted = pd.to_datetime(df[col])

                if converted.notna().sum() > 0.8 * len(df):
                    df[col] = converted

            except:
                pass

        # 6. Basic outlier clipping (numeric columns)
        numeric_cols = df.select_dtypes(
            include=np.number
        ).columns

        for col in numeric_cols:

            q1 = df[col].quantile(0.25)
            q3 = df[col].quantile(0.75)

            iqr = q3 - q1

            lower = q1 - 1.5 * iqr
            upper = q3 + 1.5 * iqr

            df[col] = df[col].clip(lower, upper)

        report["rows"] = df.shape[0]
        report["columns"] = df.shape[1]

        return df, report