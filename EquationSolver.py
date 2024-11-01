from math import sqrt


class EquationSolver:
    def __init__(self, equation: str) -> None:
        self.__equation = equation.replace(" ", "")
        self.__equation_dict = self.__separator(self.__equation)
        if "x^3" in equation and self.__equation_dict["x^3"] != 0:
            self.__roots = self.__cubic_equation_solver(self.__equation_dict)
        elif "x^2" in equation and self.__equation_dict["x^2"] != 0:
            self.__roots = self.__quadratic_equation_solver(
                self.__equation_dict)
        elif "x" in equation and self.__equation_dict["x"] != 0:
            self.__roots = self.__linear_equation_solver(self.__equation_dict)
        else:
            raise SyntaxError("the equation is incomplete")

    def __separator(self, equation: str) -> dict:
        duplicated_eq = equation
        equation_dict = {}
        for element in ["x^3", "x^2", "x", "="]:
            if element in duplicated_eq:
                coefficient = duplicated_eq[:duplicated_eq.index(element)]
                duplicated_eq = duplicated_eq.replace(coefficient+element, "")
                if element == "=":
                    if coefficient == "":
                        coefficient = - \
                            int(equation[equation.index(element)+1:])
                    else:
                        coefficient = int(
                            coefficient) - int(equation[equation.index(element)+1:])
                else:
                    if coefficient == "" or coefficient == "+":
                        coefficient = 1
                    elif coefficient == "-":
                        coefficient = -1
                    else:
                        coefficient = int(coefficient)
                equation_dict[element] = coefficient
            else:
                equation_dict[element] = 0
        return equation_dict

    def __cubic_equation_solver(self, equation_dict: dict) -> tuple:
        if (equation_dict["x^2"] != 0) and (equation_dict["x"] != 0) and (equation_dict["="] == 0):
            equation_dict["x^2"], equation_dict["x"], equation_dict["="], equation_dict[
                "x^3"] = equation_dict["x^3"], equation_dict["x^2"], equation_dict["x"], equation_dict["="]
            x2x3 = self.__quadratic_equation_solver(equation_dict)
            return 0, *x2x3
        elif (equation_dict["x^2"] != 0) and (equation_dict["x"] == 0) and (equation_dict["="] == 0):
            equation_dict["x"], equation_dict["="], equation_dict["x^3"], equation_dict[
                "x^2"] = equation_dict["x^3"], equation_dict["x^2"], equation_dict["x"], equation_dict["="]
            x2 = self.__linear_equation_solver(equation_dict)
            return 0, x2
        elif (equation_dict["x^2"] == 0) and (equation_dict["x"] == 0) and (equation_dict["="] == 0):
            return (0,)
        else:
            variable_multiplier_c = []
            if equation_dict["="] < 0:
                for x in range(1, -equation_dict["="]+1):
                    if (-equation_dict["="]) % (x) == 0:
                        variable_multiplier_c.append(x)
                        variable_multiplier_c.append(-x)
            else:
                for x in range(1, equation_dict["="]+1):
                    if (-equation_dict["="]) % (x) == 0:
                        variable_multiplier_c.append(x)
            for x in variable_multiplier_c:
                if (equation_dict["x^3"]*(x**3))+(equation_dict["x^2"]*(x**2))+(equation_dict["x"]*x)+equation_dict["="] == 0:
                    x1 = x
                    break
            else:
                raise ValueError("the equation has a remainder")
            beta = 0
            for index in equation_dict:
                beta = (x1*beta) + equation_dict[index]
                equation_dict[index] = beta
            equation_dict["x^2"], equation_dict["x"], equation_dict["="], equation_dict[
                "x^3"] = equation_dict["x^3"], equation_dict["x^2"], equation_dict["x"], equation_dict["="]
            x2x3 = self.__quadratic_equation_solver(equation_dict)
            return x1, *x2x3

    def __quadratic_equation_solver(self, equation_dict: dict) -> tuple:
        if (equation_dict["x"] != 0) and (equation_dict["="] == 0):
            equation_dict["x"], equation_dict["="], equation_dict["x^2"] = equation_dict["x^2"], equation_dict["x"], equation_dict["="]
            x2 = self.__linear_equation_solver(equation_dict)
            return 0, x2
        elif (equation_dict["x"] == 0) and (equation_dict["="] == 0):
            return (0,)
        else:
            a, b, c = equation_dict["x^2"], equation_dict["x"], equation_dict["="]
            if a + b + c == 0:
                return (1, c/a)
            elif b == a + c:
                return (-1, (-c)/a)
            else:
                delta = (b**2)-(4*a*c)
                if delta > 0:
                    sqrt_delta = sqrt(delta)
                    x1 = ((-b)+sqrt_delta)/(2*a)
                    x2 = ((-b)-sqrt_delta)/(2*a)
                    return (x1, x2)
                elif delta == 0:
                    x1 = x2 = (-b)/(2*a)
                    return (x1, x2)
                else:
                    return ()

    def __linear_equation_solver(self, equation_dict: dict) -> tuple:
        a, b = equation_dict["x"], equation_dict["="]
        return ((-b)/a,)

    def value(self) -> tuple:
        output_values = []
        for x in self.__roots:
            if int(x) == x:
                output_values.append(int(x))
            else:
                output_values.append(round(x, 10))
        return tuple(output_values)

    def __iter__(self):
        return iter(self.value())

    def __len__(self):
        return len(self.__roots)

    def __repr__(self) -> str:
        return f"EquationSolver(equation= {self.__equation}) -> return {self.value()}"

    def __str__(self) -> str:
        return f"The root/roots of the equation: {self.value()}"
