from django.contrib import admin


from django.contrib import admin
from .models import Utilisateur, Produit, Annonce, Transaction, Message, Commentaire, Suivi, DepotOrdure, Criticite, Panier



class AdminUtilisateur(admin.ModelAdmin):
    readonly_fields = ('id_utilisateur',)
    list_display = ('id_utilisateur', 'nom', 'email')
    search_fields = ('id_utilisateur', 'nom', 'email')

class AdminProduit(admin.ModelAdmin):
    readonly_fields = ('id_produit',)
    list_display = ('id_produit', 'nom', 'categorie', 'prix', 'etat', 'id_vendeur')
    search_fields = ('id_produit', 'nom', 'categorie', 'etat', 'id_vendeur')

class AdminAnnonce(admin.ModelAdmin):
    readonly_fields = ('id_annonce',)
    list_display = ('id_annonce', 'id_produit', 'date_publication', 'statut', 'id_acheteur')
    search_fields = ('id_annonce', 'id_produit', 'statut', 'id_acheteur')

class AdminTransaction(admin.ModelAdmin):
    readonly_fields = ('id_transaction',)
    list_display = ('id_transaction', 'id_acheteur', 'id_vendeur', 'id_annonce', 'date_transaction', 'montant')
    search_fields = ('id_transaction', 'id_acheteur', 'id_vendeur', 'id_annonce')

class AdminMessage(admin.ModelAdmin):
    readonly_fields = ('id_message',)
    list_display = ('id_message', 'id_expediteur', 'id_destinataire', 'date_envoi')
    search_fields = ('id_message', 'id_expediteur', 'id_destinataire')

class AdminCommentaire(admin.ModelAdmin):
    readonly_fields = ('id_commentaire',)
    list_display = ('id_commentaire', 'id_depot', 'id_annonce', 'id_utilisateur', 'texte')
    search_fields = ('id_commentaire', 'id_depot', 'id_annonce', 'id_utilisateur')

class AdminSuivi(admin.ModelAdmin):
    readonly_fields = ('id_suivi',)
    list_display = ('id_suivi', 'id_depot', 'id_utilisateur', 'date_suivi')
    search_fields = ('id_suivi', 'id_depot', 'id_utilisateur')

class AdminDepotOrdure(admin.ModelAdmin):
    readonly_fields = ('id_depot',)
    list_display = ('id_depot', 'localisation', 'date_signalement', 'id_niveau_criticite', 'id_reporter')
    search_fields = ('id_depot', 'localisation', 'id_niveau_criticite', 'id_reporter')

class AdminCriticite(admin.ModelAdmin):
    readonly_fields = ('id_criticite',)
    list_display = ('id_criticite', 'niveau', 'description')
    search_fields = ('id_criticite', 'niveau')

class AdminPanier(admin.ModelAdmin):
    readonly_fields = ('id_panier',)
    list_display = ('id_panier', 'id_utilisateur')
    search_fields = ('id_panier', 'id_utilisateur')

admin.site.register(Utilisateur, AdminUtilisateur)
admin.site.register(Produit, AdminProduit)
admin.site.register(Annonce, AdminAnnonce)
admin.site.register(Transaction, AdminTransaction)
admin.site.register(Message, AdminMessage)
admin.site.register(Commentaire, AdminCommentaire)
admin.site.register(Suivi, AdminSuivi)
admin.site.register(DepotOrdure, AdminDepotOrdure)
admin.site.register(Criticite, AdminCriticite)
admin.site.register(Panier, AdminPanier)