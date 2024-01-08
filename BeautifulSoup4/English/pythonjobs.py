from bs4 import BeautifulSoup
import requests
import pyshorteners
import time

# URL for job search on timesjobs.com
url = "https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=python&txtLocation="

def find_jobs():
    # Get the HTML content of the webpage
    data = requests.get(url).text
    print("Enter skills you aren't familiar with:")
    # Prompt the user to input skills they are not familiar with
    user_skills = input('>>')

    print(f'Filtering out {user_skills}...')

    # Use BeautifulSoup to parse the HTML content
    soup = BeautifulSoup(data, 'lxml')
    # Find HTML elements corresponding to job listings
    jobs = soup.find_all('li', class_='clearfix job-bx wht-shd-bx')

    for job in jobs:
        # Extract the posted date of the job listing
        published_date = job.find('span', 'sim-posted').text.strip()
        if 'few' in published_date:
            # Extract job name, company name, required skills, and job description link
            job_name = job.find('h2').text.strip()
            company_name = job.find('h3', 'joblist-comp-name').text.strip()
            skills = job.find('span', 'srp-skills').text.strip()
            des_link = job.header.h2.a['href']

            # Use pyshorteners to shorten the job description link
            s = pyshorteners.Shortener()
            des_link_short = s.tinyurl.short(des_link)
            # Check if user skills are not in the required skills for the job
            if user_skills not in skills:
                # Display job details
                print(f'''
            Job Name: {job_name}
            Company Name: {company_name}
            Required Skills: {skills.strip()}
            Posted Date: {published_date}
            More Info: {des_link_short}
                '''
                )
                # job_data = pd.DataFrame(columns=["Job Name", "Company Name", "Required Skills"])
                # job_data = job_data._append({"Job Name": job_name, "Company Name": company_name, "Required Skills": skills}, ignore_index=True)
                # print(job_data.head())

if __name__ == '__main__':
    while True:
        # Call the function to find jobs and display details
        find_jobs()
        wait_time = 5
        print(f'Waiting {wait_time} seconds before refreshing...')
        time.sleep(wait_time)
