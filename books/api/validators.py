from django.utils import timezone
from rest_framework import serializers
from datetime import date 

def validate_publication_date(value):
    """
    Garante que a data de publicação não seja no futuro
    e nem em um passado muito distante.
    """
    if value > timezone.now().date():
        raise serializers.ValidationError("Publication date cannot be in the future.")
    if value < date(1455, 1, 1):
        raise serializers.ValidationError("Publication date seems too old. Please check the year.")
        
    return value

def validate_isbn(value):

    isbn = value.replace('-', '')
    
    if not isbn.isdigit():
        raise serializers.ValidationError("ISBN must only contain digits.")
        
    if len(isbn) not in [10, 13]:
        raise serializers.ValidationError("ISBN must be 10 or 13 digits long.")
        
    return value