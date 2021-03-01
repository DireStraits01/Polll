from rest_framework import serializers
from django.db.models import Q
from poll_app.models import Poll, Question, Answer, Option


class PollSerializer(serializers.ModelSerializer):
	class Meta:
		fields = '__all__'
		model = Poll

class OptionSerializer(serializers.ModelSerializer):
	class Meta:
		fields = ['id', 'question']
		model = Option


class QuestionSerializer(serializers.ModelSerializer):
	class Meta:
		fields = '__all__'
		model = Question


class AnswerSerializer(serializers.ModelSerializer):
	class Meta:
		fields = '__all__'
		model = Answer

# question and polls with users answers
class QuestionListSerializer(serializers.ModelSerializer):
	answers = serializers.SerializerMethodField('users_answers')

	class Meta:
		fields = ['body','answers']
		model = Question

	def users_answers(self, question):
		author_id = self.context.get('request').user.id
		answers = Answer.objects.filter(
			Q(question=question) & Q(author__id=author_id))
		serializer = AnswerSerializer(instance=answers, many=True)
		return serializer.data

class UserPollSerializer(serializers.ModelSerializer):
	class Meta:
		fields = '__all__'
		model = Poll


class AnswerOneTextSerializer(serializers.ModelSerializer):
	class Meta:
		fields = ['text_input']
		model = Answer	

class UserFilteredPrimaryKeyRelated(serializers.PrimaryKeyRelatedField):
	def get_queryset(self):
		question_id = self.context.get('request').parser_context['kwargs'][
		'question_pk']
		request = self.context.get('request', None)
		queryset = super(UserFilteredPrimaryKeyRelated, self).get_queryset()
		if not request or not queryset:
			return None
		return queryset.filter(question_id = question_id)
		

class AnswerOneOptionSerializer(serializers.ModelSerializer):
	one_option = UserFilteredPrimaryKeyRelated(many = False, queryset = Option.objects.all())			

	class Meta:
		fields = ['one_option']
		model = Answer

class AnswerManyOptionSerializer(serializers.ModelSerializer):
	many_options = UserFilteredPrimaryKeyRelated(many = True, queryset = Option.objects.all())

	class Meta:
		fields = ['many_options']
		model = Answer