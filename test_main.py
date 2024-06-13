from unittest import TestCase

from checker import checkcheck


class TestMain(TestCase):
    def test_first_len_check(self):
        checked = checkcheck("ASD", "DSA")
        score = checked.len_check()
        score2 = checked.alpha_check()
        self.assertEqual(60, int(score))
        self.assertEqual(40, int(score2))

    def test_second_len_check(self):
        checked = checkcheck("A", "BB")
        score = checked.len_check()
        score2 = checked.alpha_check()
        self.assertEqual(0, int(score))
        self.assertEqual(0, int(score2))

    def test_third_len_check(self):
        checked = checkcheck("AAABB", "BAA")
        score = checked.len_check()
        score2 = checked.alpha_check()
        self.assertEqual(20, int(score))
        self.assertEqual(40, int(score2))

    def test_fourth_len_check(self):
        checked = checkcheck("AA", "AAE")
        score = checked.len_check()
        score2 = checked.alpha_check()
        self.assertEqual(30, int(score))
        self.assertEqual(20, int(score2))
