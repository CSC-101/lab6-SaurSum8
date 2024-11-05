import data
import lab6
import unittest


# Write your test cases for each part below.

class TestCases(unittest.TestCase):
    # Part 0
    def test_index_smallest_from_1(self):
        input = [2, 1, 9, 0, 4, 5]
        expected = 3
        actual = lab6.index_smallest_from(input, 0)
        self.assertEqual(expected, actual)


    def test_index_smallest_from_2(self):
        input = [2, 1, 9, 0, 4, 5]
        expected = 4
        actual = lab6.index_smallest_from(input, 4)
        self.assertEqual(expected, actual)


    def test_index_smallest_from_3(self):
        input = [2, 1, 9, 0, 4, 5]
        expected = None
        actual = lab6.index_smallest_from(input, 6)
        self.assertEqual(expected, actual)


    def test_index_smallest_from_4(self):
        input = []
        expected = None
        actual = lab6.index_smallest_from(input, 0)
        self.assertEqual(expected, actual)


    def test_selection_sort_1(self):
        input = [1, 2, 3, 4, 5]
        expected = [1, 2, 3, 4, 5]
        lab6.selection_sort(input)
        self.assertEqual(expected, input)


    def test_selection_sort_2(self):
        input = []
        expected = []
        lab6.selection_sort(input)
        self.assertEqual(expected, input)


    def test_selection_sort_3(self):
        input = [9, 7, 5, 3, 1]
        expected = [1, 3, 5, 7, 9]
        lab6.selection_sort(input)
        self.assertEqual(expected, input)


    def test_selection_sort_4(self):
        input = [5, 0, 19, 21, 4, 6]
        expected = [0, 4, 5, 6, 19, 21]
        lab6.selection_sort(input)
        self.assertEqual(expected, input)


    # Part 1
    def test_selection_sort_books_1(self):
        b0 = data.Book(['Leshy', 'Grimora', 'Magnifus', 'P03'], "Inscryption")
        b1 = data.Book(['Leshy'], "The Scrybe Of Beasts")
        b2 = data.Book(['Luke', 'Dealer'], "Buckshot Roulette")

        inp = [b0, b1, b2]
        exp = [b2, b0, b1]

        lab6.selection_sort_books(inp)
        self.assertEqual(exp, inp)

    def test_selection_sort_books_2(self):
        b0 = data.Book(['Stoat', 'P03'], "The Scrybe Of Technology")
        b1 = data.Book(['Leshy'], "The Scrybe Of Beasts")
        b2 = data.Book(['Luke', 'Dealer'], "Buckshot Roulette")

        inp = [b0, b1, b2]
        exp = [b2, b1, b0]

        lab6.selection_sort_books(inp)
        self.assertEqual(exp, inp)

    # Part 2
    def test_swap_case_1(self):
        inp = "HeLlO WORld"
        exp = "hElLo worLD"
        self.assertEqual(exp, lab6.swap_case(inp))

    def test_swap_case_2(self):
        inp = "EEEEEEEE&* (&*^&%^a"
        exp = "eeeeeeee&* (&*^&%^A"
        self.assertEqual(exp, lab6.swap_case(inp))

    # Part 3
    def test_str_translate_1(self):
        inp = "abcdcba"
        exp = "xbcdcbx"

        self.assertEqual(exp, lab6.str_translate(inp, 'a','x'))

    def test_str_translate_2(self):
        inp = "aaabbbba%aaccccCCC )"
        exp = "aaabbbba%aappppCCC )"

        self.assertEqual(exp, lab6.str_translate(inp, 'c','p'))

    # Part 4
    def test_histogram_1(self):
        inp = "Hello World world"
        exp = {"hello": 1, "world": 2}

        self.assertEqual(exp, lab6.histogram(inp))

    def test_histogram_2(self):
        inp = "ABC abc DEF abcd"
        exp = {"abc": 2, "def": 1, "abcd":1}

        self.assertEqual(exp, lab6.histogram(inp))


if __name__ == '__main__':
    unittest.main()
