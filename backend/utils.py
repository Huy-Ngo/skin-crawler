from kaggle import download, validate, SkinCancerMnist


if __name__ == '__main__':
    if validate():
        dataset = 'kmader/skin-cancer-mnist-ham10000'
        dataset_path = download(dataset)
        scm = SkinCancerMnist(dataset_path)
        for img_metadata in scm.get_img_metadata_list():
            print('Image path: ', img_metadata[0])
            print('Image info: ', img_metadata[1])
            print('===')
