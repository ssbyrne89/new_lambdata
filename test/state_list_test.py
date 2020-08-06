
import unittest
from pandas import DataFrame

from new_lambdata_ssbyrne89.state_list import add_state_names

#OBJECTIVE: test the add_state_names() function from the my_lambdate/assignment.py file

class TestAssignment(unittest.TestCase):

    def test_add_state_names(self):
        
        df = DataFrame({"abbrev":["CA","CO","CT","DC","TX"]})
        self.assertEqual(list(df.columns), ['abbrev'])
        breakpoint()


        result = add_state_names(df)
        self.assertEqual(list(result.columns), ["abbrev", "name"])
        self.assertEqual(result.iloc[0]['abbrev'], "CA")
        self.assertEqual(result.iloc[0]['abbrev'], "Cali")
    # after we invoke the function:
    # expect that it has one more column and same number of rows
    # expect that certain column names exist before and certain column names exist after

    #self.assertEqual("foo".upper(), "FOO") #> True or False
    #df.columns)
if __name__ == '__main__':
    unittest.main()