from rest_framework import serializers
from .models import TitikPoin, Sampah, User, Setor, Tarik, Tabungan, Contact_Us, Admin

class SampahSerializer (serializers.ModelSerializer):
    class Meta:
        model = Sampah
        fields = '__all__'

class TitikPoinSerializer (serializers.ModelSerializer):
    class Meta:
        model = TitikPoin
        fields = '__all__'

class UserSerializer (serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class SetorSerializer (serializers.ModelSerializer):
    class Meta:
        model = Setor
        fields = '__all__'

class TarikSerializer (serializers.ModelSerializer):
    class Meta:
        model = Tarik
        fields = '__all__'

class TabunganSerializer (serializers.ModelSerializer):
    class Meta:
        model = Tabungan
        fields = '__all__'

class Contact_UsSerializer (serializers.ModelSerializer):
    class Meta:
        model = Contact_Us
        fields = '__all__'

class AdminSerializer (serializers.ModelSerializer):
    class Meta:
        model = Admin
        fields = '__all__'