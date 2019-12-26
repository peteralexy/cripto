from django.forms import ModelForm
from .models import Voter

class VoteForm(ModelForm):
    class Meta:
        model = Voter
        fields = ['voter_vote']