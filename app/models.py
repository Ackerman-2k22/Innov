from django.db import models

# Create your models here.
'''class Clients(models.Model):
    client_id = models.AutoField(primary_key=True)
    username = models.CharField(unique=True, blank=True, null=True, max_length=255)
    phone_number = models.CharField(unique=True, blank=True, null=True, max_length=9)

    class Meta:
        db_table = 'clients'

    def __str__(self):
        return self.username
'''

class Statut(models.TextChoices):
    ACTIVE = 'ACTIVE', 'Active'
    VENDU = 'VENDU', 'Vendu'

class Etat(models.TextChoices):
    NEUF = 'NEUF', 'Neuf'
    OCCASION = 'OCCASION', 'Occasion'

class Niveau(models.TextChoices):
    FAIBLE = 'FAIBLE', 'Faible'
    MOYEN = 'MOYEN', 'Moyen'
    ELEVE = 'ELEVE', 'Élevé'

class Utilisateur(models.Model):
    id_utilisateur = models.AutoField(primary_key=True)
    nom = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    mot_de_passe = models.CharField(max_length=255)
    adresse = models.TextField()

    def se_connecter(self):
        pass

    def se_deconnecter(self):
        pass

    def creer_compte(self):
        pass

    def modifier_compte(self):
        pass

class Produit(models.Model):
    id_produit = models.AutoField(primary_key=True)
    nom = models.CharField(max_length=255)
    description = models.TextField()
    categorie = models.CharField(max_length=255)
    prix = models.FloatField()
    etat = models.CharField(max_length=10, choices=Etat.choices)
    id_vendeur = models.ForeignKey(Utilisateur, on_delete=models.CASCADE)

    def ajouter_produit(self):
        pass

    def modifier_produit(self):
        pass

    def supprimer_produit(self):
        pass

class Annonce(models.Model):
    id_annonce = models.AutoField(primary_key=True)
    id_produit = models.ForeignKey(Produit, on_delete=models.CASCADE)
    date_publication = models.DateField()
    statut = models.CharField(max_length=10, choices=Statut.choices)
    id_acheteur = models.ForeignKey(Utilisateur, on_delete=models.SET_NULL, null=True, blank=True)

    def publier_annonce(self):
        pass

    def supprimer_annonce(self):
        pass

    def marquer_comm_vendu(self):
        pass

class Transaction(models.Model):
    id_transaction = models.AutoField(primary_key=True)
    id_acheteur = models.ForeignKey(Utilisateur, related_name='transactions_acheteur', on_delete=models.CASCADE)
    id_vendeur = models.ForeignKey(Utilisateur, related_name='transactions_vendeur', on_delete=models.CASCADE)
    id_annonce = models.ForeignKey(Annonce, on_delete=models.CASCADE)
    date_transaction = models.DateField()
    montant = models.FloatField()

    def effectuer_transaction(self):
        pass

    def supprimer_transaction(self):
        pass

    def stocker_transaction(self):
        pass

class Message(models.Model):
    id_message = models.AutoField(primary_key=True)
    id_expediteur = models.ForeignKey(Utilisateur, related_name='messages_expediteur', on_delete=models.CASCADE)
    id_destinataire = models.ForeignKey(Utilisateur, related_name='messages_destinataire', on_delete=models.CASCADE)
    contenu = models.TextField()
    date_envoi = models.DateField()

    def envoyer_message(self):
        pass

    def supprimer_message(self):
        pass

    def stocker_message(self):
        pass

class Commentaire(models.Model):
    id_commentaire = models.AutoField(primary_key=True)
    id_depot = models.ForeignKey('DepotOrdure', on_delete=models.SET_NULL, null=True, blank=True)
    id_annonce = models.ForeignKey(Annonce, on_delete=models.SET_NULL, null=True, blank=True)
    id_utilisateur = models.ForeignKey(Utilisateur, on_delete=models.CASCADE)
    texte = models.TextField()

    def ajouter_commentaire(self):
        pass

    def modifier_commentaire(self):
        pass

    def supprimer_commentaire(self):
        pass

class Suivi(models.Model):
    id_suivi = models.AutoField(primary_key=True)
    id_depot = models.ForeignKey('DepotOrdure', on_delete=models.CASCADE)
    id_utilisateur = models.ForeignKey(Utilisateur, on_delete=models.CASCADE)
    date_suivi = models.DateField()

    def ajouter_suivi(self):
        pass

    def supprimer_suivi(self):
        pass

class DepotOrdure(models.Model):
    id_depot = models.AutoField(primary_key=True)
    localisation = models.CharField(max_length=255)
    photo = models.ImageField(upload_to='photos/')
    date_signalement = models.DateField()
    id_niveau_criticite = models.ForeignKey('Criticite', on_delete=models.CASCADE)
    id_reporter = models.ForeignKey(Utilisateur, on_delete=models.CASCADE)

    def signaler_depot(self):
        pass

    def modifier_depot(self):
        pass

    def supprimer_depot(self):
        pass

class Criticite(models.Model):
    id_criticite = models.AutoField(primary_key=True)
    niveau = models.CharField(max_length=10, choices=Niveau.choices)
    description = models.TextField()

    def ajouter_criticite(self):
        pass

    def modifier_criticite(self):
        pass

    def supprimer_criticite(self):
        pass

class Panier(models.Model):
    id_panier = models.AutoField(primary_key=True)
    id_utilisateur = models.ForeignKey(Utilisateur, on_delete=models.CASCADE)
    id_produit = models.ManyToManyField(Produit)

    def ajouter_produit_au_panier(self, produit):
        pass

    def retirer_produit_du_panier(self, produit):
        pass

    def vider_panier(self):
        pass