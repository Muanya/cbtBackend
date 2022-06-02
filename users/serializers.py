from rest_framework import serializers

from users.models import Students, CustomUser, Department


class CustomUserSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(style={"input_type": "password"}, write_only=True)

    class Meta:
        model = CustomUser
        fields = ['first_name', 'last_name', 'reg_no', 'email', 'password', 'password2']
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def save(self):
        user = CustomUser(first_name=self.validated_data['first_name'],
                          last_name=self.validated_data['last_name'],
                          reg_no=self.validated_data['reg_no'],
                          email=self.validated_data['email'],
                          )
        password = self.validated_data['password']
        password2 = self.validated_data['password2']
        if password != password2:
            raise serializers.ValidationError({'password': 'Passwords must match.'})
        user.set_password(password)
        user.save()
        return user


class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = ('name', 'faculty')


class StudentSerializer(serializers.ModelSerializer):
    user = CustomUserSerializer(read_only=True)
    department = DepartmentSerializer(read_only=True)
    user_id = serializers.PrimaryKeyRelatedField(queryset=CustomUser.objects.all())
    department_id = serializers.PrimaryKeyRelatedField(queryset=Department.objects.all())

    def save(self, **kwargs):
        student = Students(
            user=self.validated_data['user_id'],
            department=self.validated_data['department_id'],
            level=self.validated_data['level']
        )

        student.save()
        return student

    class Meta:
        model = Students
        fields = ('id', 'user_id', 'user', 'level', 'department_id', 'department')
        depth = 1


class StudentRegistrationSerializer(serializers.Serializer):
    first_name = serializers.CharField(max_length=50)
    last_name = serializers.CharField(max_length=50)
    email = serializers.EmailField()
    reg_no = serializers.CharField(max_length=15)
    level = serializers.IntegerField()
    password = serializers.CharField(style={"input_type": "password"}, write_only=True)
    password2 = serializers.CharField(style={"input_type": "password"}, write_only=True)

    def create(self, validated_data):
        userSerialize = CustomUserSerializer(data=validated_data)
        if not userSerialize.is_valid():
            raise serializers.ValidationError({'student_info': "Incorrect Student details"})
        user = userSerialize.save()
        validated_data['user_id'] = user.id
        # TODO: to be modified later
        validated_data['department_id'] = 1
        studentSerialize = StudentSerializer(data=validated_data)
        if not studentSerialize.is_valid():
            raise serializers.ValidationError({'student_info': "Incorrect Student details"})
        studentSerialize.save()
        return validated_data
