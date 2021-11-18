from rest_framework                   import serializers
from libreriauserapp.models.user      import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'password', 'nombre', 'email']

    def to_representation(self, obj):
        user    = User.objects.get(id=obj.id)
        return {
            'id'      : user.id,
            'username': user.username,
            'nombre'  : user.nombre,
            'email'   : user.email,
            'saldo'   : user.saldo
        }