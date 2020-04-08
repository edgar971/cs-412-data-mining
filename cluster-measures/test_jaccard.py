from main import jaccard_similarity, nmi


def test_sample_1():
    truth = [2, 0, 0, 1, 2]
    predicted = [3, 0, 1, 1, 2]

    val = jaccard_similarity(truth, predicted)
    assert val == 0


def test_sample_2():
    truth = [1, 2, 2, 3]
    predicted = [3, 4, 4, 4]

    val = jaccard_similarity(truth, predicted)
    assert val == 0.3333333333333333


def test_sample_3():
    truth = [1, 2, 2, 1]
    predicted = [1, 2, 2, 1]

    val = jaccard_similarity(truth, predicted)
    assert val == 1.0


def test_nmi_1():
    truth = [2, 0, 0, 1, 2]
    predicted = [3, 0, 1, 1, 2]

    val = nmi(predicted, truth)
    assert round(val, 3) == 0.656
