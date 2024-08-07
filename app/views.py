from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import HttpResponseRedirect, JsonResponse
from django.core.paginator import Paginator
from django.db.models import Count, Q
import json
from django.shortcuts import render
from .models import Utilisateur,DepotOrdureForm, Produit, Annonce, Transaction, Message, Commentaire, Suivi, DepotOrdure, Criticite, Panier
from .models import Utilisateur,DepotOrdureForm, Produit, Annonce, Transaction, Message, Commentaire, Suivi, DepotOrdure, Criticite, Panier
from django import forms


@login_required(login_url='/authentication/login')
def signalization(request):
    depots = DepotOrdure.objects.all()
    return render(request, 'app/signalization.html', {'depots': depots})

@login_required(login_url='/authentication/login')
def collect(request):
    return render(request, 'app/collect.html')

@login_required(login_url='/authentication/login')
def marketplace(request):
    return render(request, 'app/marketplace_accueil.html')

@login_required(login_url='/authentication/login')
def product_view(request):
    return render(request, 'app/product_view.html')
@login_required(login_url='/authentication/login')
def product2(request):
    return render(request, 'app/product2.html')
@login_required(login_url='/authentication/login')
def annonces(request):
    return render(request, 'app/annonces.html')

class DepotOrdureForm(forms.ModelForm):
    class Meta:
        model = DepotOrdure
        fields = ['localisation', 'photo', 'date_signalement', 'description', 'id_type', 'id_niveau_criticite']
        widgets = {
            'date_signalement': forms.DateInput(attrs={'type': 'date'}),
        }

@login_required(login_url='/authentication/login')
def depot(request):
    if request.method == 'POST':
        form = DepotOrdureForm(request.POST, request.FILES)
        if form.is_valid():
            depot = form.save(commit=False)
            depot.id_reporter = request.user.utilisateur  # Assigner l'utilisateur connecté comme reporter
            depot.save()
            return redirect('signalization')  # Rediriger vers la page de signalisation après l'enregistrement
    else:
        form = DepotOrdureForm()
    return render(request, 'app/depot-signal.html', {'form': form})
'''
def search_clients(request):
    if request.method == 'POST':
        search_str = json.loads(request.body).get('searchText', '')
        clients = Clients.objects.filter(
            Q(client_id__istartswith=search_str) |
            Q(username__icontains=search_str) |
            Q(phone_number__icontains=search_str)
        ).distinct()

        data = list(clients.values('client_id', 'username', 'phone_number'))

        return JsonResponse(data, safe=False)


@login_required(login_url='/authentication/login')
def index(request):
    app = Incidents.objects.all().order_by('-id')
    categories = Incidents.objects.values_list('category', flat=True).distinct()
    statuses = Incidents.objects.values_list('status', flat=True).distinct()
    paginator = Paginator(app, 3)
    page_number = request.GET.get('page')
    page_obj = Paginator.get_page(paginator, page_number)

    context = {
        'app': app,
        'page_obj': page_obj,
        'categories': categories,
        'statuses': statuses,
    }
    return render(request, 'app/index.html', context)



def details(request, client_id):
    client = get_object_or_404(Clients, pk=client_id)
    messages.success(request, "Client affiché avec succès.")
    return render(request, 'app/details.html', {'client': client})


def clients(request):
    clients_list = Clients.objects.all()
    return render(request, 'app/clients.html', {'clients': clients_list})


def list_clients(request):
    clients = Clients.objects.annotate(number_of_incidents=Count('incidents'))
    for client in clients:
        print(client.username, client.number_of_incidents)
    return render(request, 'app/clients.html', {'clients': clients})

'''



def home(request):
    return render(request, 'index.html')




'''
def search_utilisateurs(request):
    if request.method == 'POST':
        search_str = json.loads(request.body).get('searchText', '')
        utilisateurs = Utilisateur.objects.filter(
            Q(id_utilisateur__istartswith=search_str) |
            Q(nom__icontains=search_str) |
            Q(email__icontains=search_str)
        ).distinct()

        data = list(utilisateurs.values('id_utilisateur', 'nom', 'email'))

        return JsonResponse(data, safe=False)
'''
'''
@login_required(login_url='/authentication/login')
def index(request):
    transactions = Transaction.objects.all().order_by('-id_transaction')
    categories = Transaction.objects.values_list('id_annonce__id_produit__categorie', flat=True).distinct()
    statuses = Transaction.objects.values_list('id_annonce__statut', flat=True).distinct()
    paginator = Paginator(transactions, 3)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'transactions': transactions,
        'page_obj': page_obj,
        'categories': categories,
        'statuses': statuses,
    }
    return render(request, 'app/index.html', context)


get_object_or_404



def details(request, id_utilisateur):
    utilisateur = get_object_or_404(Utilisateur, pk=id_utilisateur)
    messages.success(request, "Utilisateur affiché avec succès.")
    return render(request, 'app/details.html', {'utilisateur': utilisateur})

def utilisateurs(request):
    utilisateurs_list = Utilisateur.objects.all()
    return render(request, 'app/utilisateurs.html', {'utilisateurs': utilisateurs_list})

def list_utilisateurs(request):
    utilisateurs = Utilisateur.objects.annotate(number_of_transactions=Count('transactions_acheteur'))
    for utilisateur in utilisateurs:
        print(utilisateur.nom, utilisateur.number_of_transactions)
    return render(request, 'app/utilisateurs.html', {'utilisateurs': utilisateurs})


'''