import itertools
import math


def cluster_probability(cluster):
    cluster_sum = []
    cluster_len = float(len(cluster))
    cluster_names = list(set(cluster))

    for index, cluster_name in enumerate(cluster_names):
        cluster_sum.append(0)
        for i in cluster:
            if cluster_name == i:
                cluster_sum[index] += 1

    return [i / cluster_len for i in cluster_sum]


def entropy(cluster):
    entropy = 0
    cluster_prob = cluster_probability(cluster)

    for i in cluster_prob:
        entropy += i * math.log(i, 2)

    return entropy * (-1)


def mutual_information(cluster, truth):
    cluster_len = float(len(cluster))
    sc = list(set(cluster))
    st = list(set(truth))
    mutual_info = 0
    c_probability = cluster_probability(cluster)
    truth_probability = cluster_probability(truth)

    probability_matrix = [[0 for x in range(len(sc))] for y in range(len(st))]

    for i in range(len(truth)):
        probability_matrix[st.index(truth[i])][sc.index(cluster[i])] += 1

    for i in range(len(st)):
        for j in range(len(sc)):
            joint_probability = probability_matrix[i][j] / (cluster_len)
            if joint_probability != 0:
                mutual_info += joint_probability * (
                    math.log(
                        joint_probability
                        / float(c_probability[j] * truth_probability[i]),
                        2,
                    )
                )
    return mutual_info


def nmi(cluster, truth):
    hc = entropy(cluster)
    ht = entropy(truth)
    mutual_info = mutual_information(cluster, truth)
    return mutual_info / math.sqrt(hc * ht)


def jaccard_similarity(labels1, labels2):
    num_labels = len(labels1)
    m11 = 0
    m10 = 0
    m01 = 0

    for i, j in itertools.combinations(range(num_labels), 2):
        group1 = labels1[i] == labels1[j]
        group2 = labels2[i] == labels2[j]
        if group1 and group2:
            m11 += 1
        elif group1 and not group2:
            m10 += 1
        elif not group1 and group2:
            m01 += 1

    return float(m11) / (m11 + m10 + m01)
