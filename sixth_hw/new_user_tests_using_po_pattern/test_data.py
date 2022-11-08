import datetime
import datetime

USER = 'user'
PASSWORD = 'bitnami'
PRODUCT_NAME = 'PRODUCT_NAME'
PRODUCT_TAG = 'PRODUCT_TAG'
PRODUCT_MODEL = 'PRODUCT_MODEL'


def generate_product_name():
    return PRODUCT_NAME + str(datetime.datetime.now())


def generate_product_tag():
    return PRODUCT_TAG + str(datetime.datetime.now())


def generate_product_model():
    return PRODUCT_MODEL + str(datetime.datetime.now())
