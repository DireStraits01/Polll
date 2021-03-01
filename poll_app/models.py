from django.db import models
from django.utils import timezone 
from django.contrib.auth import get_user_model




User = get_user_model()

class Poll(models.Model):
    title = models.CharField(max_length=256)
    start_date = models.DateField(auto_now_add=True)
    end_date = models.DateField()
    description = models.TextField(max_length=1024, blank=True)

    def __str__(self):
    	return self.title

TYPES_OF_POLLS = (
    ('free_text', 'free text input'),
    ('option', 'only one choice'),
    ('options', 'many choices'),
)

class Question(models.Model):
    poll = models.ForeignKey(Poll, on_delete=models.CASCADE, related_name='questions')
    body = models.CharField(max_length=250)
    poll_type = models.CharField(max_length=50, choices=TYPES_OF_POLLS, verbose_name='Types of polls')

    def __str__(self):
    	return str(self.body)



class Option(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name="question_options")
    text = models.CharField(max_length=256)

    def __str__(self):
    	return f'{self.question} - {self.text}'

class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='answers')
    one_option = models.ForeignKey(Option, on_delete=models.CASCADE, null=True, related_name='answer_option_one', blank=True)
    many_options = models.ManyToManyField(Option, null=True, blank=True)
    text_input = models.TextField(null=True, blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    
    def __str__(self):
    	return f'{self.question} - {self.one_option} - {self.many_options} - {self.text_input}  '

