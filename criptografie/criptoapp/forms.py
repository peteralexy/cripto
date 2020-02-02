from django.forms import ModelForm
from .models import Voter

class VoteForm(ModelForm):
    class Meta:
        model = Voter
        fields = ['voter_name', 'voter_age', 'voter_city', 'voter_county', 'voter_address', 'voter_vote']