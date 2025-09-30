class TestCase:
    def __init__(self, test_method_name):
        self.test_method_name = test_method_name

    def run(self, result):
        result.test_started()
        self.set_up()
        try:
            test_method = getattr(self, self.test_method_name)
            test_method()
        except AssertionError:
            result.add_failure(self.test_method_name)
        except Exception:
            result.add_error(self.test_method_name)
        self.tear_down()

    def set_up(self):
        pass

    def tear_down(self):
        pass


# Exemplo de uso
class MyTest(TestCase):
    def set_up(self):
        print("set_up")

    def tear_down(self):
        print("tear_down")

    def test_success(self):
        print("test_success")

    def test_failure(self):
        print("test_failure")
        assert False  # força falha

    def test_error(self):
        print("test_error")
        raise Exception("erro inesperado")


if __name__ == "__main__":
    from test_result import TestResult

    result = TestResult()

    MyTest("test_success").run(result)
    MyTest("test_failure").run(result)
    MyTest("test_error").run(result)

    print(result.summary())  # esperado: "3 run, 1 failed, 1 error"
