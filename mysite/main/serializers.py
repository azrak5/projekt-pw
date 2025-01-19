from rest_framework import serializers
from .models import Knjiga, Izdavac, Autor

class KnjigaSerializer(serializers.HyperlinkedModelSerializer):
    izdavac = serializers.HyperlinkedRelatedField(
        view_name='izdavac-detail',
        queryset=Izdavac.objects.all()
    )
    class Meta:
        model = Knjiga
        fields = '__all__'

    def validate_naslov(self, value):
        if not value:
            raise serializers.ValidationError("Naslov ne može biti prazan.")
        if len(value)>100:
            raise serializers.ValidationError("Naslov ne može biti dulji od 100 znakova.")
        return value
    
class IzdavacSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Izdavac
        fields = '__all__'

    def validate_naziv(self, value):
        if not value:
            raise serializers.ValidationError("Naziv ne može biti prazan.")
        if len(value)>30:
            raise serializers.ValidationError("Naziv ne može biti dulji od 30 znakova.")
        return value
    
class AutorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Autor
        fields = '__all__'

    def validate_ime(self, value):
        if not value:
            raise serializers.ValidationError("Ime autora ne može biti prazno.")
        if len(value)>30:
            raise serializers.ValidationError("Ime ne može biti dulje od 30 znakova.")
        return value