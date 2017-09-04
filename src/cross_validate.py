from preprocessing.preprocessing import get_data
from pipeline.pipeline import create_pipeline


def main():
    df = get_data()
    pipeline = create_pipeline()
    data = pipeline.fit_transform(df)
    print(df)


if __name__ == '__main__':
    main()
