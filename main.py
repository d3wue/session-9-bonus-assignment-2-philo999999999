import requests # Import Requests library to send http requests
import bs4 # Import BeautifulSoup4 library to parse HTML data

userAgent = { # Define the user agent telling the website we are using Google Chrome to avoid getting blocked
    'User-Agent':
    'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36'
}

url = 'https://www.transfermarkt.com/bundesliga/startseite/wettbewerb/L1' # Define url

r = requests.get(url, headers=userAgent) # Send the request
htmlText = r.text # Extract the raw HTML
htmlDocument = bs4.BeautifulSoup(htmlText, 'html.parser') # Parse the raw HTML to Python

while True: # Shows user the different menu options
    print("Options:")
    print("1. Show available teams")
    print("2. Select a team and show high-level information")
    print("3. Select a team and show all players")
    print("4. Stop the program")
    print (15 * "--")
    choice = input("Enter your choice: ") # user can choose based on the numbers

    if choice == '1':
        print('Available teams:')
        url = "https://www.transfermarkt.com/bundesliga/startseite/wettbewerb/L1"
        r = requests.get(url, headers=userAgent)
        htmlText = r.text
        htmlDocument = bs4.BeautifulSoup(htmlText, 'html.parser') 
        teams = htmlDocument.find_all("td", {"class": "hauptlink no-border-links"})

        for index, team in enumerate(teams, 1):
            text = team.get_text()
            print(f"{index}. {text}")
            print()


    elif choice == '2':
        team_number = int(input('Enter the team number: '))
    elif choice == '3':
        team_index = int(input('Enter the team number: '))
    elif choice == '4':
        print("Exiting program.")
        break
    else:
        print('Invalid input')