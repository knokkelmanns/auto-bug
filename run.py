import unittest
import xmlrunner as xmlrunner

from double_click_to_tab import Test1
from check_the_box import Test2


tests_classes=[
    Test1,
    Test2,
]

suites_list = []
for tests_class in tests_classes:
    suite=unittest.TestLoader().loadTestsFromTestCase(tests_class)
    suites_list.append(suite)

if __name__ == "__main__":
    testRunner=xmlrunner.XMLTestRunner(output='test-reports').run(unittest.TestSuite(suites_list))