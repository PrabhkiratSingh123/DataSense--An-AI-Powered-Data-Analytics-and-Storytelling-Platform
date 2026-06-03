import ydata_profiling as yp

def generate_profile_report(df):
    """
    Generates an interactive data profiling report for a Pandas DataFrame.
    """
    return yp.ProfileReport(df, title="Data Profiling Report", explorative=True)
