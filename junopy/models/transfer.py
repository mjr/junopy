from junopy.utils import get, put, post, delete


BASE_MODEL_URL = '/transfers'


def create(params):
    return post(end_point=BASE_MODEL_URL, data=params)