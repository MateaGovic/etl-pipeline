def identify_and_remove_duplicated_data(df):
    if df.duplicated().sum() > 0:
        print("# of duplicated rows:", df.duplicated().sum())

        df_cleaned = df.drop_duplicates(keep='first')

        print("shape of data before removing duplicated data", df.shape)
        print("shape of data after removing duplicated data", df_cleaned.shape)

        return df_cleaned
    else:
        print("No duplicated data found")
        return df

