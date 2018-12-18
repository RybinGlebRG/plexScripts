from common import TestCase


def bleach_case():
    """
    This case tests ability to form episodes from two groups of video files - "Bleach case"
    """

    def arrange():
        raise NotImplementedError

    def act():
        raise NotImplementedError

    def check():
        raise NotImplementedError

    test_case = TestCase.TestCase(arrange, act, check)
    return test_case
