from bs4 import BeautifulSoup
import requests
import pyshorteners
import time

# URL de recherche d'emploi sur timesjobs.com
url = "https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=python&txtLocation="

def trouver_emplois():
    # Obtenir le contenu HTML de la page web
    data = requests.get(url).text
    print("Entrez les compétences que vous ne connaissez pas :")
    # Inviter l'utilisateur à saisir les compétences qu'il ne connaît pas
    competences_utilisateur = input('>>')

    print(f'Filtrage des offres nécessitant {competences_utilisateur}...')

    # Utiliser BeautifulSoup pour analyser le contenu HTML
    soup = BeautifulSoup(data, 'lxml')
    # Trouver les éléments HTML correspondant aux offres d'emploi
    emplois = soup.find_all('li', class_='clearfix job-bx wht-shd-bx')

    for emploi in emplois:
        # Extraire la date de publication de l'offre d'emploi
        date_publication = emploi.find('span', 'sim-posted').text.strip()
        if 'few' in date_publication:
            # Extraire le nom de l'emploi, le nom de l'entreprise, les compétences requises et le lien de description de l'emploi
            nom_emploi = emploi.find('h2').text.strip()
            nom_entreprise = emploi.find('h3', 'joblist-comp-name').text.strip()
            competences_requises = emploi.find('span', 'srp-skills').text.strip()
            lien_description = emploi.header.h2.a['href']

            # Utiliser pyshorteners pour raccourcir le lien de description de l'emploi
            s = pyshorteners.Shortener()
            lien_description_court = s.tinyurl.short(lien_description)
            # Vérifier si les compétences de l'utilisateur ne sont pas requises pour cet emploi
            if competences_utilisateur not in competences_requises:
                # Afficher les détails de l'emploi
                print(f'''
            Nom de l'emploi : {nom_emploi}
            Nom de l'entreprise : {nom_entreprise}
            Compétences requises : {competences_requises.strip()}
            Date de publication : {date_publication}
            Plus d'informations : {lien_description_court}
                '''
                )

if __name__ == '__main__':
    while True:
        # Appeler la fonction pour trouver des emplois et afficher les détails
        trouver_emplois()
        temps_attente = 5
        print(f'Attente de {temps_attente} secondes avant la mise à jour...')
        time.sleep(temps_attente)
