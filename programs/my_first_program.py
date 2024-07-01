from nada_dsl import *


def nada_main():
    party1 = Party(name="Party1")
    my_int1 = SecretInteger(Input(name="my_int1", party=party1))
    my_int2 = SecretInteger(Input(name="my_int2", party=party1))

    # Perform addition of the two secret integers
    result = my_int1 + my_int2

    # Return the result as output
    return [Output(result, "result_output", party1)]

