import warnings

from django.conf import settings


def test_dummy():
    """Test for checkign proper project config"""
    warnings.warn(
        'Using DB backend {}.'.format(
            settings.DATABASES['default']['ENGINE'].replace('django.db.backends.', '')
        )
    )
    assert True
