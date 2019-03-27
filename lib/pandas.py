import os


def aaa():
    if os.path.exists(CSV_PATH):
        df = pd.read_csv(CSV_PATH)

    df = pd.DataFrame([
        ["subnet-AAAAAA", "subnet-BBBBBB"],
        [32, 32],
        [31, 25]
    ]).T

    df.columns = ["subnet-id", "1000", "1030"]
    df.index = [1, 2]

    # append
    df['1100'] = [30, 20]

    # df.to_csv(CSV_PATH)
    print(df)
