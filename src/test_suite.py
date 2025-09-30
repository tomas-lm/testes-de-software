from test_case import TestCase
from test_result import TestResult
from test_case_test import TestStub


class TestSuite:
    def __init__(self):
        self.tests = []

    def add_test(self, test):
        self.tests.append(test)

    def run(self, result):
        for test in self.tests:
            test.run(result)


class TestSuiteTest(TestCase):
    def test_suite_size(self):
        suite = TestSuite()
        suite.add_test(TestStub("test_success"))
        suite.add_test(TestStub("test_failure"))
        suite.add_test(TestStub("test_error"))

        assert len(suite.tests) == 3

    def test_suite_success_run(self):
        result = TestResult()
        suite = TestSuite()
        suite.add_test(TestStub("test_success"))
        suite.run(result)

        assert result.summary() == "1 run, 0 failed, 0 error"

    def test_suite_multiple_run(self):
        result = TestResult()
        suite = TestSuite()
        suite.add_test(TestStub("test_success"))
        suite.add_test(TestStub("test_failure"))
        suite.add_test(TestStub("test_error"))
        suite.run(result)

        assert result.summary() == "3 run, 1 failed, 1 error"


if __name__ == "__main__":
    result = TestResult()
    suite = TestSuite()

    suite.add_test(TestSuiteTest("test_suite_size"))
    suite.add_test(TestSuiteTest("test_suite_success_run"))
    suite.add_test(TestSuiteTest("test_suite_multiple_run"))

    suite.run(result)
    print(result.summary())
