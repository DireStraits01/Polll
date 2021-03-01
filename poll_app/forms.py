from django.forms import ModelForm
from poll_app.models import Answer

class AnswerForm(ModelForm):
    class Meta:
        model = Answer
        fields = ['one_option', 'many_options', 'text_input']
    
    def __init__(self, *args, **kwargs):
        question = kwargs.pop('question')
        super().__init__(*args, **kwargs)
        if question.poll_type == 'free_text':
            del self.fields['one_option']
            del self.fields['many_options']
        elif question.poll_type == 'option':
            del self.fields['many_options']
            del self.fields['text_input']
            self.fields['one_option'].queryset = question.option_set.all()
        elif question.poll_type == 'options':
            del self.fields['one_option']
            del self.fields['text_input']
            self.fields['many_options'].queryset = question.option_set.all()