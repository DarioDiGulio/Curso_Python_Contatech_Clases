class Calculator:
    def add(self, num1: int, num2: int) -> int:
        num1_total = self.total_number_by_digits(num1)
        num2_total = self.total_number_by_digits(num2)
        return num1_total + num2_total

    def substraction(self, num1: int, num2: int) -> int:
        num1_total = self.total_number_by_digits(num1)
        num2_total = self.total_number_by_digits(num2)
        return num1_total - num2_total

    def multiplication(self, factor1: int, factor2: int) -> int:
        factor1_total = self.total_multiplication_number_by_digits(factor1)
        factor2_total = self.total_multiplication_number_by_digits(factor2)
        return factor1_total * factor2_total

    def total_multiplication_number_by_digits(self, factor1):
        factor1_array = self.salice_number_by_digits(factor1)
        factor1_total = 1
        for num in factor1_array:
            factor1_total *= num
        return factor1_total

    def total_number_by_digits(self, num1: int) -> int:
        num1_array = self.salice_number_by_digits(num1)
        num1_total = 0
        for num in num1_array:
            num1_total += num
        return num1_total

    def salice_number_by_digits(self, factor1):
        return [int(a) for a in str(factor1)]
