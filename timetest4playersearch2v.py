''' Time Travelling Testing algorithm
    Version: 1.0.2
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
    def __init__(self,a):
        super().__init__()
        self._o_function_variables = (None, None)
        self._a = a
    def get_o_variables(self):
        return self._o_function_variables
    def update_o_variables(self, a,b):
        self._o_function_variables = (a,b)
    def get_name(self):
        return 'Player 1'
    def Timeloop(self, Player_B_output, Player_C_output, Player_D_output):
        self._new_input = self.Binary_addition(self._a[0], self._a[1]*Player_B_output)
        self._new_input = self.Binary_addition(self._new_input, self._a[2]*Player_C_output)
        self._new_input = self.Binary_addition(self._new_input, self._a[3]*Player_B_output*Player_C_output)
        return self._new_input
class Player_B(Player):
    def __init__(self,a):
        super().__init__()
        self._o_function_variables = (None, None)
        self._a = a
    def get_o_variables(self):
        return self._o_function_variables
    def update_o_variables(self, a,b):
        self._o_function_variables = (a,b)
    def get_name(self):
        return 'Player 2'
    def Timeloop(self, Player_A_output, Player_C_output, Player_D_output):
        self._new_input = self._new_input = self.Binary_addition(self._a[0], self._a[1]*Player_C_output)
        self._new_input = self.Binary_addition(self._new_input, self._a[2]*Player_D_output)
        self._new_input = self.Binary_addition(self._new_input, self._a[3]*Player_D_output*Player_C_output)
        return self._new_input
class Player_C(Player):
    def __init__(self,a):
        super().__init__()
        self._o_function_variables = (None, None)
        self._a = a
    def get_o_variables(self):
        return self._o_function_variables
    def update_o_variables(self, a,b):
        self._o_function_variables = (a,b)
    def get_name(self):
        return 'Player 3'
    def Timeloop(self, Player_A_output, Player_B_output, Player_D_output): #update timeloop here
        self._new_input = self.Binary_addition(self._a[0], self._a[1]*Player_D_output)
        self._new_input = self.Binary_addition(self._new_input, self._a[2]*Player_A_output)
        self._new_input = self.Binary_addition(self._new_input, self._a[3]*Player_D_output*Player_A_output)
        return self._new_input
class Player_D(Player):
    def __init__(self,a):
        super().__init__()
        self._o_function_variables = (None, None)
        self._a = a
    def get_o_variables(self):
        return self._o_function_variables
    def update_o_variables(self, a,b):
        self._o_function_variables = (a,b)
    def get_name(self):
        return 'Player 4'
    def Timeloop(self, Player_A_output, Player_B_output, Player_C_output): #update timeloop here
        self._new_input = self.Binary_addition(self._a[0], self._a[1]*Player_B_output)
        self._new_input = self.Binary_addition(self._new_input, self._a[2]*Player_A_output)
        self._new_input = self.Binary_addition(self._new_input, self._a[3]*Player_B_output*Player_A_output)
        return self._new_input
class Time_Game(object):
    def __init__(self,a,b,c,d):
        self._player_1 = Player_A(a) 
        self._player_2 = Player_B(b)
        self._player_3 = Player_C(c)
        self._player_4 = Player_D(d)
        self._player_1_combination = a
        self._player_2_combination = b
        self._player_3_combination = c
        self._player_4_combination = d
        self._iterations = 1
        self._number_of_tested_functions = 1
        self._errors = 0
    def get_errors(self):
        return self._errors
    def reset_o_function(self, p1_variables, p2_variables,p3_variables, p4_variables):
        self._iterations = 1
        self._player_1.update_o_variables(p1_variables[0], p1_variables[1])
        self._player_2.update_o_variables(p2_variables[0], p2_variables[1])
        self._player_3.update_o_variables(p3_variables[0], p3_variables[1])
        self._player_4.update_o_variables(p4_variables[0], p4_variables[1])
        self._potential_fixed_point = [0,0,0,0]
        self._potential_fixed_point[0] = self._player_1.Timeloop(self._player_2.output_function(0,self._player_2.get_o_variables()[0],self._player_2.get_o_variables()[1]), 
                                                               self._player_3.output_function(0,self._player_3.get_o_variables()[0],self._player_3.get_o_variables()[1]),
                                                               self._player_4.output_function(0,self._player_4.get_o_variables()[0],self._player_4.get_o_variables()[1]))
        self._potential_fixed_point[1] = self._player_2.Timeloop(self._player_1.output_function(0,self._player_1.get_o_variables()[0],self._player_1.get_o_variables()[1]),
                                                               self._player_3.output_function(0,self._player_3.get_o_variables()[0],self._player_3.get_o_variables()[1]),
                                                               self._player_4.output_function(0,self._player_4.get_o_variables()[0],self._player_4.get_o_variables()[1]))
        self._potential_fixed_point[2] = self._player_3.Timeloop(self._player_1.output_function(0,self._player_1.get_o_variables()[0],self._player_1.get_o_variables()[1]),
                                                               self._player_2.output_function(0,self._player_2.get_o_variables()[0],self._player_2.get_o_variables()[1]),
                                                               self._player_4.output_function(0,self._player_4.get_o_variables()[0],self._player_4.get_o_variables()[1]))
        self._potential_fixed_point[3] = self._player_4.Timeloop(self._player_1.output_function(0,self._player_1.get_o_variables()[0],self._player_1.get_o_variables()[1]),
                                                               self._player_2.output_function(0,self._player_2.get_o_variables()[0],self._player_2.get_o_variables()[1]),
                                                               self._player_3.output_function(0,self._player_3.get_o_variables()[0],self._player_3.get_o_variables()[1]))

        self._player_1.update_input(self._potential_fixed_point[0])
        self._player_2.update_input(self._potential_fixed_point[1])
        self._player_3.update_input(self._potential_fixed_point[2])
        self._player_4.update_input(self._potential_fixed_point[3])
        
    def User_selection(self, user):
        #print('{}'.format(user.get_name()))
  #      print('Your input is {}'.format(user.get_input()))
        user.update_output(user.output_function(user.get_input(),user.get_o_variables()[0],user.get_o_variables()[1]))
        #print('Your output is {}'.format(user.get_output()))
    def Test_Functions(self):
        
        self.User_selection(self._player_1)
        self.User_selection(self._player_2)
        self.User_selection(self._player_3)
        self.User_selection(self._player_4)

        self._player_1.update_input(self._player_1.Timeloop(self._player_2.get_output(), self._player_3.get_output(), self._player_4.get_output())) 
        self._player_2.update_input(self._player_2.Timeloop(self._player_1.get_output(), self._player_3.get_output(), self._player_4.get_output()))
        self._player_3.update_input(self._player_3.Timeloop(self._player_1.get_output(), self._player_2.get_output(), self._player_4.get_output()))
        self._player_4.update_input(self._player_4.Timeloop(self._player_1.get_output(), self._player_2.get_output(), self._player_3.get_output()))
        if self._iterations == 2:
            self._potential_fixed_point = [self._player_1.get_input(), self._player_2.get_input(), self._player_3.get_input(), self._player_4.get_input()]
        self._player_1.update_output(None)
        self._player_2.update_output(None)
        self._player_3.update_output(None)
        self._player_4.update_output(None)
        if self._player_1.get_input() != self._potential_fixed_point[0] and self._iterations >= 3:
            self._errors +=1
        elif self._player_2.get_input() != self._potential_fixed_point[1] and self._iterations >= 3:
            self._errors += 1
        elif self._player_3.get_input() != self._potential_fixed_point[2] and self._iterations >= 3:
            self._errors += 1
        elif self._player_4.get_input() != self._potential_fixed_point[3] and self._iterations >= 3:
            self._errors += 1
        elif self._iterations < 20 and self._errors < 1:
 #           print('Step Number {}'.format(self._iterations))
            self._iterations += 1
            self.Test_Functions()

       
def main(a,b,c,d):
    iterations = 0
    Sample_Game = Time_Game(a,b,c,d)
    binary_digits = [(0, 0), (0, 1), (1, 0), (1, 1)]
    for i in binary_digits:
        for j in binary_digits:
            for k in binary_digits:
                for l in binary_digits:
                    Sample_Game.reset_o_function(i,j,k,l)
                    Sample_Game.Test_Functions()
    if Sample_Game.get_errors() == 0:
 #       print((a,b,c,d)) #commented out for speedability, normally prints a successful fuuncyion as it is discovered
        return (a,b,c,d)
    else:
        return None
    
def search():
    binary_combinations = (0,1)
    combinations = []
    successful_functions = []
    iterations = 0
    for a in binary_combinations:
        for b in binary_combinations:
            for c in binary_combinations:
                for d in binary_combinations:
                    combinations.append((a,b,c,d))
    print(combinations)
    for i in combinations:
        for j in combinations:
            for k in combinations:
                for l in combinations:
                    result = main(i,j,k,l)
                    if result != None:
                        successful_functions.append(result)
                    iterations += 1
                    if iterations % 500 == 0:
                        print(len(successful_functions))
                        print('Completed {} operations'.format(iterations))
    print('No of successful functions is {}'.format(len(successful_functions)))

 #   print(successful_functions)
search()
                                
