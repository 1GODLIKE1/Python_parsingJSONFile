import pandas

def main():
    pandas.set_option('display.max.columns', 50) # display columns
    df = pandas.read_json(r"json\json.json")
    df.to_csv("csv\json_csv.csv")


if __name__ == "__main__":
    main()