import unittest
from monthblock import MonthBlock

class TestMonthBlock(unittest.TestCase):

    def test_block_color_equals_month_items(self):

        #arrange
        block = MonthBlock("May", 10)
        correct_color_for_10_items = 'rgb(117, 174, 255)'
        
        #act
        block_color = block.color

        #assert
        self.assertEqual(block_color, correct_color_for_10_items)

    def test_month_items_greater_than_block_color(self):

        #arrange
        block = MonthBlock("May", 9)
        correct_color_for_5_items = 'rgb(182, 213, 255)'
        
        #act
        block_color = block.color

        #assert
        self.assertEqual(block_color, correct_color_for_5_items)

    def test_block_color_does_not_match_month_items(self):

        #arrange
        block = MonthBlock("May", 8)
        correct_color_for_0_items = 'rgb(236, 236, 236)'

        #act
        block_color = block.color

        #assert
        self.assertNotEqual(block_color, correct_color_for_0_items)

if __name__ == "__main__":

    unittest.main()

