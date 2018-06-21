import unittest
import library

NUM_CORPUS = '''
On the 5th of May every year, Mexicans celebrate Cinco de Mayo. This tradition
began in 1845 (the twenty-second anniversary of the Mexican Revolution), and
is the 1st example of a national independence holiday becoming popular in the
Western Hemisphere. (The Fourth of July didn't see regular celebration in the
US until 15-20 years later.) It is celebrated by 77.9% of the population--
trending toward 80.                                                                
'''

class TestCase(unittest.TestCase):

    # Helper function
    def assert_extract(self, text, extractors, *expected):
        actual = [x[1].group(0) for x in library.scan(text, extractors)]
        self.assertEquals(str(actual), str([x for x in expected]))

    # First unit test; prove that if we scan NUM_CORPUS looking for mixed_ordinals,
    # we find "5th" and "1st".
    def test_mixed_ordinals(self):
        self.assert_extract(NUM_CORPUS, library.mixed_ordinals, '5th', '1st')

    # Second unit test; prove that if we look for integers, we find four of them.
    def test_integers(self):
        self.assert_extract(NUM_CORPUS, library.integers, '1845', '15', '20', '80')

    # Third unit test; prove that if we look for integers where there are none, we get no results.
    def test_no_integers(self):
        self.assert_extract("no integers", library.integers)
    
    # Fourth unit test; test date with format like 2015-07-25
    def test_date(self):
        self.assert_extract('I was born on 2015-07-25.', library.dates_iso8601, '2015-07-25')

    # Fifth unit test; test date with invalid months/days
    def test_incorrectDate(self):
        self.assert_extract("2015-13-48", library.test_dates_iso8601)

    # test date with format 25 Jan 2017
    def test_dates_fmt2(self):
        self.assert_extract('I was born on 25 Jan 2017.', library.test_dates_fmt2, '25 Jan 2017')
   
   # Assignment tests - 



    # Test 1 - test iso8601 date with timeStamp with format 2018-06-22 18:22:19.123
    def test_timeStamp1(self):
        self.assert_extract('Current timeStamp is 2018-06-22 18:22:19:123', library.test_dates_iso8601, '2018-06-22 18:22:19:123')

    # test iso8601 timeStamp with format 2018-06-22T18:22:19.123
    def test_timeStamp2(self):
        self.assert_extract('Current timeStamp is 2018-06-22T18:22:19.123', library.test_dates_iso8601, '2018-06-22T18:22:19.123')
    
    # test iso8601 timeStamp with format 2018-06-22T18:22:19.123MDT
    def test_timeStamp3(self):
        self.assert_extract('Current timeStamp is 2018-06-22T18:22:19.123MDT', library.test_dates_iso8601, '2018-06-22T18:22:19.123MDT')

    # test  iso8601 timeStamp with format 2018-06-22T18:22:19.123Z
    def test_timeStamp4(self):
        self.assert_extract('Current timeStamp is 2018-06-22T18:22:19.123Z', library.test_dates_iso8601, '2018-06-22T18:22:19.123Z')

     # test iso8601 timeStamp with format 2018-06-22T18:22:19.123-800
    def test_timeStamp5(self):
        self.assert_extract('Current timeStamp is 2018-06-22T18:22:19.123-800', library.test_dates_iso8601, '2018-06-22T18:22:19.123-800')

     # test iso8601 timeStamp with wrong format 
    def test_timeStamp6(self):
        self.assert_extract('Current timeStamp is 2018-06-22T18:22:19.12', library.test_dates_iso8601)    

    # test date format 2 with comma like 25 Jun, 2017 
    def test_date_fmt2_comma(self):
        self.assert_extract('Current date is 25 Jul, 2017', library.test_dates_fmt2, '25 Jul, 2017')

       # test date format 2 with comma like 25 Jun, 2017
    def test_date_fmt2_comma(self):
        self.assert_extract('Current date is 25 July, 2017', library.test_dates_fmt2)
        
    # test number with comma separated groupings
    def test_integers_comma(self):
        self.assert_extract('I have 145,345', library.test_integers, '145,345')

         # test number with comma separated groupings
    def test_invalid_integers_comma(self):
        self.assert_extract('I have 145,345d', library.test_integers)


if __name__ == '__main__':
    unittest.main()
