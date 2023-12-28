__author__ = "Abdessamad Touzani"
'''
Ce projet utilise la bibliothèque Python BeautifulSoup pour extraire des informations sur les offres d'emploi 
depuis le site web Indeed. 
Les utilisateurs peuvent spécifier des mots-clés pour rechercher des postes de travail pertinents.

On va travailler sur indeed France.

YouTube Katsky Studio: https://www.youtube.com/@katskystudio
Medium Abdessamad Touzani: https://medium.com/@abdessamadtouzani
Twitter (X) @at9kat: https://twitter.com/at9kat 
Instagram @t___abdessamad__: https://www.instagram.com/t___abdessamad__/
Website: https://katskydio.wordpress.com/ or directly links: https://lnk.bio/katskystudio
Github: https://www.github.com/AbdessamadTzn
'''
from bs4 import BeautifulSoup


url = "https://fr.indeed.com/jobs?q=d%C3%A9veloppeur&l=&from=searchOnHP"

#Poste pour développeur

def find_jobs_developer():
    data = requests.get(url).text

    #Parse html content
    soup = BeautifulSoup(data, 'lxml')
    job = soup.find('li', class_='css-5lfssm eu4oa1w0')
    #TODO: GO BACK TO ibm COURSE for tables scraping...
    job_name = job.find('h2').text
    print(job_name)