
class AverageCalculator:
    def calculate_average(self, numbers):
        if not numbers:
            return 0
        return sum(numbers) / len(numbers)

    def compare_averages(self, list1, list2):
        average1 = self.calculate_average(list1)
        average2 = self.calculate_average(list2)
        
        if average1 > average2:
            return "Первый список имеет большее среднее значение"
        if average2 > average1:
            return "Второй список имеет большее среднее значение"
        else:
            return "Средние значения равны"
def test_calculate_average_empty_list():
    calculator = AverageCalculator()
    result = calculator.calculate_average([])
    assert result == 0
def test_calculate_average_positive_numbers():
    calculator = AverageCalculator()
    result = calculator.calculate_average([1, 2, 3, 4, 5])
    assert result == 3.0
def test_compare_averages_first_list_greater():
    calculator = AverageCalculator()
    result = calculator.compare_averages([1, 2, 3, 4, 5], [1, 2, 3])
    assert result == "Первый список имеет большее среднее значение"
def test_compare_averages_second_list_greater():
    calculator = AverageCalculator()
    result = calculator.compare_averages([1, 2, 3], [1, 2, 3, 4, 5])
    assert result == "Второй список имеет большее среднее значение"
def test_compare_averages_equal_averages():
    calculator = AverageCalculator()
    result = calculator.compare_averages([1, 2, 3], [4, 5, 6])
    assert result == "Средние значения равны"
def test_compare_averages_empty_lists():
    calculator = AverageCalculator()
    result = calculator.compare_averages([], [])
    assert result == "Средние значения равны"
