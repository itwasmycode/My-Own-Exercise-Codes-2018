class Autonoma:
    def __init__(self, states):
        self.transaction = [{} for _ in range(states)]
        self.accept_states = [False] * states

    def register(self, source_state, char, target_state):
        self.transaction[source_state][char] = target_state

    def register_accept(self, state):
        self.accept_states[state] = True

    def accept(self, input):
        for value in input:
            if len(input) == 2:
                self.register_accept(1)
        return self.accept_states[1]


automaton = Autonoma(2)
"""
Aynı mantıkla ilerleyip, stateleri buna göre değiştirdim.
"""
print(automaton.transaction)
print(automaton.accept_states)

automaton.register(0, 'b', 1)
automaton.register(0, 'c', 0)
automaton.register(1, 'b', 1)
automaton.register(0, 'c', 0)
print(automaton.accept('11'))
print(automaton.accept('01'))

print(automaton.transaction)

automaton.accept('01')

print(automaton.accept_states)
