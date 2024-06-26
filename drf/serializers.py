from rest_framework import serializers
from .models import Student


# Validators using function.
def start_with_a(value):
    if value.lower()[0]!='a':
        raise serializers.ValidationError('Name must start with r')

# class StudentSerializer(serializers.Serializer):
#     name = serializers.CharField(max_length=100,validators=[start_with_a])
#     roll = serializers.IntegerField()
#     city = serializers.CharField(max_length=100)
#
#     def create(self, validated_data):
#         return Student.objects.create(**validated_data)

    # This is field level validation
    # def validate_roll(self, value):
    #     if value >= 200:
    #         raise serializers.ValidationError("Seats are Full")
    #     return value


    # Object level validation
    # def validate(self,data):
    #     name=data.get('name')
    #     ct=data.get('city')
    #     roll_no=data.get('roll')
    #
    #     if roll_no >200:
    #         raise serializers.ValidationError("Seats full vayo")
    #     elif roll_no ==170:
    #         raise serializers.ValidationError("YOu are not allowed here ")
    #     elif ct!='kathmandu':
    #         raise serializers.ValidationError("Only kathmandu is allowed")
    #
    #     return data


# We can also use model serializer in below way.
class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['name','roll','city']
        read_only_fields = ['roll']

