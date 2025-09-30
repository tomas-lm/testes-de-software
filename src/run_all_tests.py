from test_suite import TestSuite
from test_loader_runner import TestLoader, TestRunner
from test_case_test import TestCaseTest
from test_suite import TestSuiteTest
from test_loader_runner import TestLoaderTest


def main():
    loader = TestLoader()

    test_case_suite = loader.make_suite(TestCaseTest)
    test_suite_suite = loader.make_suite(TestSuiteTest)
    test_loader_suite = loader.make_suite(TestLoaderTest)

    master = TestSuite()
    master.add_test(test_case_suite)
    master.add_test(test_suite_suite)
    master.add_test(test_loader_suite)

    runner = TestRunner()
    runner.run(master)


if __name__ == "__main__":
    main()
