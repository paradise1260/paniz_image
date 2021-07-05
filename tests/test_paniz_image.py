from paniz_image import __version__
from paniz_image import paniz_image
import numpy as np
from pytest import raises


def test_version():
    assert __version__ == '0.1.0'

def test_rotate_image():
    image1 = np.arange(18).reshape(3,2,3)
    image2 = np.arange(10).reshape(2,5)
    with raises(TypeError):
       paniz_image.rotate_image(image1, 2.1)
    with raises(TypeError):
        paniz_image.rotate_image(4, 1)
    with raises(ValueError):
        paniz_image.rotate_image(np.array([1,2]), 3)
    
    assert paniz_image.rotate_image(image1, 1).shape == (2,3,3)
    assert paniz_image.rotate_image(image1, 2).shape == (3,2,3)
    assert type(paniz_image.rotate_image(image1, 3)) == np.ndarray
    assert paniz_image.rotate_image(image1, 6)[0].sum() == 87

    assert paniz_image.rotate_image(image2, 3).shape == (5, 2)
    assert paniz_image.rotate_image(image2, 7).shape == (5,2)
    assert type(paniz_image.rotate_image(image2, 5)) == np.ndarray
    assert paniz_image.rotate_image(image2, 2)[0].sum() == 35