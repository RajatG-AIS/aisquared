import json

class Regression:
    """
    Postprocessing configuration object for Regression
    """
    def __init__(
        self,
        min = None,
        max = None
    ):
        """
        min : None, int, or float (default None)
            The value to map an output of 0 to from the model
        max : None, int, or float (default None)
            The value to map an output of 1 to from the model
        """

        self.min = min
        self.max = max

    @property
    def min(self):
        return self._min
    @min.setter
    def min(self, value):
        if not isinstance(value, (float, int)) and value is not None:
            raise TypeError('min must be None, float, or int')
        self._min = value
    
    @property
    def max(self):
        return self._max
    @max.setter
    def max(self, value):
        if not isinstance(value, (float, int)) and value is not None:
            raise TypeError('max must be None, float, or int')
        self._max = value

    def to_dict(self):
        """
        Get the configuration object as a dictionary
        """
        return {
            'regression' : {
                'min' : self.min,
                'max' : self.max
            }
        }

    def to_json(self):
        """
        Get the configuration object as a JSON string
        """
        return json.dumps(self.to_dict())