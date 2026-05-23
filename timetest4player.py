''' Time Travelling Testing algorithm
    Version: 1.0.2
    Tests if a possible process function is a valid process function by checking the fixed point condition
'''
import itertools

class Player(object):
    def __init__(self):
        self._input = 0 #Default to 0
        self._output = None
    def get_name(self):
        if self._name is None:
            raise NotImplementedError('This Method is to be accessed through subclasses only')
    def update_input(self, _input):
        self._input = _input
    def get_input(self):
        return self._input
    def get_output(self):
        return self._output
    def update_output(self, output):
        self._output = output
    def output_function(self, _input, a, b):
        return self.Binary_addition(a, b*_input)
    def Binary_addition(self, a, b):
        if a != 0 and a != 1:
            raise RuntimeError('Paramaters not 0 or 1')
        if b != 0 and b !=1:
            raise RuntimeError('Paramaters not 0 or 1')
        if a == b:
            return 0
        if a != b:
            return 1
    def Timeloop(self):
        raise NotImplementedError('This Method is to be accessed through subclasses only')
class Player_A(Player):
    def __init(self):
        super().__init__()
        self._o_function_variables = (None, None)
    def get_o_variables(self):
        return self._o_function_variables
    def update_o_variables(self, a,b):
        self._o_function_variables = (a,b)
    def get_name(self):
        return 'Player 1'
    def Timeloop(self, Player_B_output, Player_C_output):
        self._new_input = Player_B_output*(self.Binary_addition(Player_C_output,1))
        return self._new_input
class Player_B(Player):
    def __init(self):
        super().__init__()
        self._o_function_variables = (None, None)
    def get_o_variables(self):
        return self._o_function_variables
    def update_o_variables(self, a,b):
        self._o_function_variables = (a,b)
    def get_name(self):
        return 'Player 2'
    def Timeloop(self, Player_A_output, Player_C_output):
        try:
            self._new_input = Player_C_output*(self.Binary_addition(Player_A_output,1))
        except Exception: #Handle RuntimeError and TypeError
            raise RuntimeError('Timeloop Error') 
        return self._new_input
class Player_C(Player):
    def __init(self):
        super().__init__()
        self._o_function_variables = (None, None)
    def get_o_variables(self):
        return self._o_function_variables
    def update_o_variables(self, a,b):
        self._o_function_variables = (a,b)
    def get_name(self):
        return 'Player 3'
    def Timeloop(self, Player_A_output, Player_B_output):
        try:
            self._new_input = Player_A_output*(self.Binary_addition(Player_B_output,1))
        except Exception: 
            raise RuntimeError('Timeloop Error')
        return self._new_input
class Time_Game(object):
    def __init__(self):
        self._player_1 = Player_A() 
        self._player_2 = Player_B()
        self._player_3 = Player_C()
        self._iterations = 1
        self._number_of_tested_functions = 1
        self._o_function_variables = (None, None)
    def reset_o_function(self, p1_variables, p2_variables,p3_variables):
        self._player_1.update_o_variables(p1_variables[0], p1_variables[1])
        self._player_2.update_o_variables(p2_variables[0], p2_variables[1])
        self._player_3.update_o_variables(p3_variables[0], p3_variables[1])
        self._potential_fixed_point = (self._player_1.Timeloop(self._player_2.output_function(0,self._player_2.get_o_variables()[0],self._player_2.get_o_variables()[1]),
                                                               self._player_3.output_function(0,self._player_3.get_o_variables()[0],self._player_3.get_o_variables()[1])),
                                       self._player_2.Timeloop(self._player_1.output_function(0,self._player_1.get_o_variables()[0],self._player_1.get_o_variables()[1]),
                                                               self._player_3.output_function(0,self._player_3.get_o_variables()[0],self._player_3.get_o_variables()[1])),
                                       self._player_3.Timeloop(self._player_1.output_function(0,self._player_1.get_o_variables()[0],self._player_1.get_o_variables()[1]),
                                                               self._player_2.output_function(0,self._player_2.get_o_variables()[0],self._player_2.get_o_variables()[1])))
        self._player_1.update_input(self._potential_fixed_point[0])
        self._player_2.update_input(self._potential_fixed_point[1])
        self._player_3.update_input(self._potential_fixed_point[2])
        
    def User_selection(self, user):
        #print('{}'.format(user.get_name()))
       # print('Your input is {}'.format(user.get_input()))
        user.update_output(user.output_function(user.get_input(),user.get_o_variables()[0],user.get_o_variables()[1]))
 #      print('Your output is {}'.format(user.get_output()))
    def Test_Functions(self):
        
        self.User_selection(self._player_1)
        self.User_selection(self._player_2)
        self.User_selection(self._player_3)

        self._player_1.update_input(self._player_1.Timeloop(self._player_2.get_output(), self._player_3.get_output()))
        self._player_2.update_input(self._player_2.Timeloop(self._player_1.get_output(), self._player_3.get_output()))
        self._player_3.update_input(self._player_3.Timeloop(self._player_1.get_output(), self._player_2.get_output()))
    
        self._player_1.update_output(None)
        self._player_2.update_output(None)
        self._player_3.update_output(None)
        if self._player_1.get_input() != self._potential_fixed_point[0]:
            print('Error in logic at step {}'.format(self._iterations))
        elif self._player_2.get_input() != self._potential_fixed_point[1]:
            print('Error in logic at step {}'.format(self._iterations))
        elif self._player_3.get_input() != self._potential_fixed_point[2]:
            print('Error in logic at step {}'.format(self._iterations))
        elif self._iterations < 900:
 #           print('Step Number {}'.format(self._iterations))
            self._iterations += 1
            self.Test_Functions()
        else:
            print('Successfully completed {} steps with fixed point {}'.format(self._iterations, self._potential_fixed_point))
            
        
def main():
    Sample_Game = Time_Game()
    binary_combinations = [(0, 0), (0, 1), (1, 0), (1, 1)]
    for i in binary_combinations:
        for j in binary_combinations:
            for k in binary_combinations:
                Sample_Game.reset_o_function(i,j,k)
                Sample_Game.Test_Functions()
    
main()
