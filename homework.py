def test_function():
    def inner_funktion():
        print('Я в области видимости функции test_function')
    inner_funktion()
test_function()
