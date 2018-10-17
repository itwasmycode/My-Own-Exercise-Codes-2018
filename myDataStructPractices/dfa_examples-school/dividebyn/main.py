from automata.fa.dfa import DFA


dfa = DFA(
    states={'q0', 'q1', 'q2', 'q3', 'q4'},
    input_symbols={'0', '1'},
    transitions={
        'q0': {'0': 'q0', '1': 'q1'},
        'q1': {'0': 'q2', '1': 'q3'},
        'q2': {'0': 'q4', '1' : 'q0'},
        'q3' :{'0': 'q1','1':'q2'},
        'q4' :{'0': 'q3','1':'q4'}
        },
    initial_state='q0',
    final_states={'q0'}
)


def dfa_checker(dfa_str):
    if not dfa_str:
        raise ValueError("No str specified")
    try:
        dfa.read_input(dfa_str)
        print("No exception, successful state")
    except:
        print("Non final statement error.")

print("\n")
dfa_checker('1110')
print("------------")
dfa_checker('1111')
print("----------")
dfa_checker('')
