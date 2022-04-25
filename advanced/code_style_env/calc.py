"""Module with implemented class Calculator."""


class Calculator:
    """Class Calculator that can do four simple math operations."""

    def addition(self, first_operand, second_operand):
        """Method allows to addition two operands."""
        return self, first_operand + second_operand

    def subtraction(self, first_operand, second_operand):
        """Method allows to subtraction two operands."""
        return self, first_operand - second_operand

    def multiplication(self, first_operand, second_operand):
        """Method allows to multiplication two operands."""
        return self, first_operand * second_operand

    def division(self, first_operand, second_operand):
        """Method allows to division two operands."""
        return self, first_operand / second_operand
