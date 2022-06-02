import datetime

from rest_framework import serializers

from questions.models import Question, Choice


class ChoiceSerializer(serializers.ModelSerializer):
    question_id = serializers.PrimaryKeyRelatedField(queryset=Question.objects.all())
    question = serializers.StringRelatedField(read_only=True)

    def save(self, **kwargs):
        choice = Choice(
            question=self.validated_data['question_id'],
            choice_text=self.validated_data['choice_text'],
            is_answer=self.validated_data['is_answer']
        )
        choice.save()
        return choice

    class Meta:
        model = Choice
        fields = ('question_id', 'question', 'choice_text', 'is_answer')


class _ChoiceSerializer(serializers.Serializer):
    choice_text = serializers.CharField(max_length=200)
    is_answer = serializers.BooleanField(required=False)


class QuestionSerializer(serializers.ModelSerializer):
    choice_set = _ChoiceSerializer(many=True)

    def save(self, **kwargs):
        mod_date = datetime.datetime.now()
        question = Question(
            question_text=self.validated_data['question_text'],
            lecturer=self.validated_data['lecturer'],
            course=self.validated_data['course'],
            mod_date=mod_date
        )

        question.save()

        for choice_data in self.validated_data['choice_set']:
            choice_data['question_id'] = question.id
            ser = ChoiceSerializer(data=choice_data)
            if ser.is_valid():
                ser.save()

        return question

    class Meta:
        model = Question
        fields = ('id', 'question_text', 'lecturer', 'course', 'choice_set')
