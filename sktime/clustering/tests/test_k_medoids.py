# -*- coding: utf-8 -*-
"""Tests for time series k-medoids."""
import numpy as np
from sklearn import metrics

from sktime.clustering._k_medoids import TimeSeriesKMedoids
from sktime.datasets import load_basic_motions

expected_results = {
    "medoids": [
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        3,
        0,
        0,
        0,
        0,
        0,
        7,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
    ]
}

expected_score = {"medoids": 0.2858974358974359}

expected_iters = {"medoids": 300}

expected_labels = {
    "medoids": [
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        7,
        4,
        3,
        5,
        0,
        3,
        3,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        2,
        0,
        0,
        6,
        0,
        0,
        0,
        0,
        0,
        1,
    ]
}


def test_kmedoids():
    """Test implementation of Kmedoids."""
    X_train, y_train = load_basic_motions(split="train")
    X_test, y_test = load_basic_motions(split="test")

    kmedoids = TimeSeriesKMedoids(random_state=1)
    kmedoids.fit(X_train)
    test_medoids_result = kmedoids.predict(X_test)
    medoids_score = metrics.rand_score(y_test, test_medoids_result)

    assert np.array_equal(test_medoids_result, expected_results["medoids"])
    assert medoids_score == expected_score["medoids"]
    assert kmedoids.n_iter_ == 300
    assert np.array_equal(kmedoids.labels_, expected_labels["medoids"])
    assert isinstance(kmedoids.cluster_centers_, np.ndarray)
