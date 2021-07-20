import numpy as np


def rotate_image(img, rot_num=1):
    """
    rotates the image counterclockwise for a
    given number of rotations like np.rot90(img)

    Parameters
    ----------
    img : numpy.ndarray
      A numpy array representing the image.
    rot_num : int
      An integer determining the number of rotations.

    Returns
    -------
    numpy.ndarray
      The rotated image.

    Examples
    --------
    >>> from paniz_image import paniz_image
    >>> import numpy as np
    >>> image =  np.arange(18).reshape(3,2,3)
    >>> paniz_image.rotate_image(image, 6)
    array([[[15, 16, 17],
        [12, 13, 14]],

       [[ 9, 10, 11],
        [ 6,  7,  8]],

       [[ 3,  4,  5],
        [ 0,  1,  2]]])
    """
    # Handling errors:
    if type(rot_num) != int:
        raise TypeError("Number of rotations has to be an integer!")
    if type(img) != np.ndarray:
        raise TypeError("Please pass a numpy array representing an image!")
    if len(img.shape) not in {2, 3}:
        raise ValueError("Your image should have 2 or 3 dimensions!")

    # For a colored image:
    if len(img.shape) == 3:
        if rot_num == 0:
            return img
        else:
            img = np.vstack(
                ([img[:, i, :] for i in range(img.shape[1] - 1, -1, -1)])
            ).reshape(img.shape[1], img.shape[0], img.shape[2])
            return rotate_image(img, rot_num - 1)
    # For a black and white image:
    else:
        if rot_num == 0:
            return img
        else:
            img = np.vstack(
                ([img[:, i] for i in range(img.shape[1] - 1, -1, -1)])
            ).reshape(img.shape[1], img.shape[0])
            return rotate_image(img, rot_num - 1)
