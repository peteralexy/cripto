from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponseRedirect
from .forms import VoteForm
from .models import Voter
from .RSA import *
import mysql.connector as mc

# Create your views here.
def index(request):
    return render(request, 'index.html')

def page(request):

    if request.method != 'POST':
        form = VoteForm()
    else:
        form = VoteForm(request.POST)
        if form.is_valid():
      
            voter = Voter()
            voter.voter_name = form.data['voter_name']
            voter.voter_age = form.data['voter_age']
            voter.voter_city = form.data['voter_city']
            voter.voter_county = form.data['voter_county']
            voter.voter_address = form.data['voter_address']
            voter.voter_vote = form.data['voter_vote']

            p = 331
            q = 137

            public, private = generate_keypair(p, q)
            message = str(voter.voter_vote)
            encrypted_msg = encrypt(private, message)
            decrypted_msg = decrypt(public, encrypted_msg)
            #conn to mysq;

            mysqslcc = mc.connect(host='localhost', user='root', password='1234', database='evoting')

            cursor = mysqslcc.cursor()

            cursor.execute(
                """
                SELECT * FROM evoting.voter
                WHERE name LIKE '{0}' AND age LIKE '{1}' AND city LIKE '{2}' AND country LIKE '{3}' AND address LIKE '{4}' 
                """.format(voter.voter_name, voter.voter_age, voter.voter_city, voter.voter_county, voter.voter_address)
            )

            c = cursor.fetchall()

            if len(c) == 0:
                cursor.execute(
                    """
                    INSERT INTO evoting.voter
                    VALUES
                    ({0}, {1}, {2}, {3}, {4}, {5})
                    """.format(
                        voter.voter_name, voter.voter_age, voter.voter_city, voter.voter_county, voter.voter_address
                    )
                )
                cursor.execut(
                    """
                    UPDATE evoting.candidate
                    SET votes = votes + 1
                    WHERE name LIKE '{0}'
                    """.format(
                        decrypted_msg
                    )
                )

            return HttpResponseRedirect(reverse('criptoapp:index'))

    return render(request, 'page.html', {'form': form})