from EquationSolver import EquationSolver

def TESTER(equations_dict):
    index = 1
    for eq_di in equations_dict:
        try:
            roots = EquationSolver(eq_di).value()
            if equations_dict[eq_di] == Ellipsis:
                print(f"{index}:", roots)
            else:
                if roots == equations_dict[eq_di]:
                    print(f"{index}:", True)
                else:
                    print(f"{index}:", False)
        except (SyntaxError, ValueError) as text:
            if equations_dict[eq_di] == Ellipsis:
                print(f"{index}:", "Error,", text)
            else:
                if type(text) == equations_dict[eq_di]:
                    print(f"{index}:", True)
                else:
                    print(f"{index}:", False)
        index += 1


equations_dict = {
    "3x-3=0": (2,),
    "4x^2+3x-1=0": (-1, 0.25),
    "4x^3+3x^2-x=0": (0, -1, 0.25),
    "x^3+4x^2-x-10=0": ...,
    "-x^2-5x+14=0": (-7, 2),
    "x^2+2x+1=0": (-1, -1),
    "26x^2-165x+1115=0": (),
    "26x^3-165x^2+1115x=0": (0,),
    "2=0": ...,
    "5x^3+3x^2-6x+1=0": ValueError,
}

TESTER(equations_dict)
