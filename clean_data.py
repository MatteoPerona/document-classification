import pandas as pd

def load_data(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.readlines()
    content = [line.strip() for line in content if line.strip()]
    return content


def load_nyt_data(dataset_path, labels_path, classes_path, output_path=None):
    nyt_data = pd.DataFrame().assign(
        articles = load_data('data/NYT-Small/dataset.txt'),
        labels = load_data('data/NYT-Small/labels.txt'),
    )
    nyt_data['labels'] = nyt_data['labels'].astype(int)

    classes = load_data('data/NYT-Small/classes.txt')
    nyt_data = nyt_data.assign(
        labels_named = nyt_data['labels'].apply(lambda x: classes[x])
    )
    
    if not output_path is None:
        nyt_data.to_csv(output_path)

    return nyt_data


if '__name__' == '__main__':
    # Clean NYT data
    load_nyt_data(
        dataset_path='data/NYT-Small/dataset.txt', 
        labels_path='data/NYT-Small/labels.txt', 
        classes_path='data/NYT-Small/classes.txt',
        output_path='data/clean/nyt_data.csv'
    )

