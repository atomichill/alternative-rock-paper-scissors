

class ChekArguments:

    def __init__(self,arr) -> None:
        self.arguments = arr

    def is_valid_array(self):
    
        if len(self.arguments) < 3:
            print("Invalid number of arguments, type in at least 3 arguments, please try again...")
            return False

    
        if len(self.arguments) % 2 == 0:
            print('There must be an odd number of arguments, please try again...')
            return False

    
        seen_strings = set()
        for item in self.arguments:
        
            string_representation = str(item)
            if string_representation in seen_strings:
                print("Arguments contain duplicate words. please try again...")
                return False
            seen_strings.add(string_representation)

        return True