import json
from .Steps import Tokenize, RemoveCharacters, ConvertToCase, ConvertToVocabulary, PadSequences

ALLOWED_STEPS = (
    Tokenize,
    RemoveCharacters,
    ConvertToCase,
    ConvertToVocabulary
)

class LanguagePreprocessor:
    """
    Preprocessor object for natural language
    """
    def __init__(
            self,
            steps = None
    ):
        """
        Parameters
        ----------
        steps : list or None (default None)
            List of preprocessing steps for natural language
        """

        self.steps = None
        if steps is not None:
            for step in steps:
                self.add_step(step)

    def add_step(self, step):
        """
        Add a step to the preprocessor object
        """
        if not isinstance(step, ALLOWED_STEPS):
            raise TypeError(f'Each step must be one of {ALLOWED_STEPS}')
        if self.steps is None:
            self.steps = [step]
        else:
            self.steps = self.steps + [step]

    def to_dict(self):
        """
        Get the preprocessor object as a dictionary
        """
        return {
            'className' : 'LanguagePreprocessor',
            'steps' : [
                step.to_dict() for step in self.steps
            ]
        }

    def to_json(self):
        """
        Get the preprocessor object as a JSON string
        """
        return json.dumps(self.to_dict())
