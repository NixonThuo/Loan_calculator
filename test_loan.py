import unittest
from loan_amount import loan


class Test(unittest.TestCase):
    def test_it_works(self):
        self.assertEquals(loan(10000, 12, 12), 11200)

    def test_it_does_not_take_more_than_one_year(self):
        self.assertEquals(loan(10000, 12, 14), "Invalid")

    def test_it_does_not_take_amount_of_type_string(self):
        self.assertEquals(loan("10000", 12, 14), "Invalid")

   # def test_it_does_not_take_rate_of_type_string(self):
        #self.assertEquals(loan(10000, "12", 14), "Invalid")

    # def test_it_does_not_take_time_of_type_string(self):
        #self.assertEquals(loan(10000, 12, "14"), "Invalid")


if __name__ == '__main__':
    unittest.main()
