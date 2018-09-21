from sklearn.decomposition import PCA
from sklearn.neighbors import KNeighborsClassifier
import time

if __name__ =="__main__":
    line = 10000
    train_data = []
    train_label = []
    test_data = []
    test_label = []
    train_filename = 'spectrum1000_train_s1.txt'
    test_filename = 'spectrum1000_test_s1.txt'
    for spr in open(train_filename):
        spectrum = []
        values = spr.split()
        for i in range(0, len(values) - 2):
            spectrum.append(int(values[i]))
        train_data.append(spectrum)
        labell = int(float(values[len(values) - 1]) * 10000)
        if labell < line:
            train_label.append(labell)
        else:
            train_label.append(line)
    for spr in open(test_filename):
        spectrum = []
        values = spr.split()
        for i in range(0, len(values) - 2):
            spectrum.append(int(values[i]))
        test_data.append(spectrum)
        labell = int(float(values[len(values)-1])*10000)
        if labell<line:
          test_label.append(labell)
        else:
          test_label.append(line)

    #print train_label
    #print test_label
    t = time.time()
    pca = PCA(n_components=0.8)
    train_x = pca.fit_transform(train_data)
    test_x = pca.transform(test_data)
    neighbors = KNeighborsClassifier(n_neighbors=10)
    neighbors.fit(train_x, train_label)
    pre = neighbors.predict(test_x)

    acc = float((pre == test_label).sum()) / len(test_x)
    print(acc, time.time() - t)
