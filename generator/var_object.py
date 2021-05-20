class Variable:
    """
            A class to represent a variable.
            ...

                Attributes
                ----------
                name : String
                    variable name

                type : String
                    variable type

                generated_value : String
                    final variable value

                min : <value>
                    minimal possible value

                max : <value>
                    maximal possible value

                length : int
                    specified String length of final value

                prohibited : list
                    list of values which cannot be used as final value

                Methods
                -------
        """

    def __init__(self, v_name, v_type, v_min, v_max, v_prohibited_list, v_length):
        self.name = v_name
        self.type = v_type
        self.generated_value = ""
        self.min = v_min
        self.max = v_max
        self.length = v_length
        self.prohibited = v_prohibited_list

    def __str__(self):
        return str(self.name) + "=" + str(self.generated_value)
