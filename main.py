# Für die Verknüpfung der zweiten elif-Bedingung habe ich mir den Ansatz von chatgpt geben lassen + die Bedingung in Zeile 46 & 65
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
    print('Options:')
    print('1. Show available teams') # Shows all teams from the german Bundesliga
    print('2. Select a team and show high-level information') # User can select a team and gets infos about it
    print('3. Select a team and show all players') # User can select a team and gets a list of its players
    print('4. Stop the program') # Break out of the while loop
    print (15 * '-') # For formatting purposes
    choice = input('Enter your choice:> ') # User can choose based on the numbers

    if choice == '1': # If user chooses option 1
        print('Available teams:') 
        if r.status_code == 200: # Uses status code to check if the request was successful
            htmlText = r.text # Extract the raw html
            htmlDocument = bs4.BeautifulSoup(htmlText, 'html.parser') # Parse the raw html to Python
            teams = htmlDocument.find_all("td", {"class": "hauptlink no-border-links"}) # Find all team elements over the matching class from the html code

            for index, team in enumerate(teams, 1): # Iterate over each team element
                text = team.get_text() # Get the text content of the team element
                print(f"{index}. {text}") # Print the index and related team name
                print() # Print an empty line for better readability
        else: # If the request was not successful
            print ('request failed') # Print message indicating request failure

    elif choice == '2': # If the user chooses option 2
        team_number = int(input('Enter the team number: ')) # User selects team; input gets converted into an integer 
        if r.status_code == 200: # Uses the status code to check if the request was successful
            htmlText = r.text # Extract the raw html
            htmlDocument = bs4.BeautifulSoup(htmlText, 'html.parser') # Parse the raw html to Python
            table = htmlDocument.find('table', {'class': 'items'}).find ('tbody') # Find the table element with the matching class from the html structure
            teams = table.find_all('tr') # Find all rows (tr elements)
            if 1 <= team_number <= len(teams): # Check if the team number is within the range of available teams
                selected_team = teams[team_number - 1] # Get the selected team based on its index; adjust with -1 because the lists starts with 0
                team_name = selected_team.find ('td', {'class': 'hauptlink no-border-links'}) # Get the team name over the matching class from the table data from its html
                info = selected_team.find_all ('td', {'class': 'zentriert'}) # Find all cells with the class zentriert within the selected team 
                squad = info[1].text.strip() # Get the squad value from the second cell
                age = info[2].text.strip() # Get the age value from the third cell
                foreigners = info[3].text.strip() # Get the foreigners value from the fourth cell 
                info1 = selected_team.find_all ('td', {'class': 'rechts'}) # Find all cells with the class rechts within the selected team
                averageMarketValue = info1[0].text.strip() # Get the averageMarketValue from the first cell
                totalMarketValue = info1[1].text.strip() # Get the total market value from the second cell
                print (f'Team: {team_name}, Squad: {squad}, Foreigners: {foreigners}, Average Market Value: {averageMarketValue}, Total Market Value: {totalMarketValue}') # Print team information
            else: # If the team number is out of range
                print('Team number is out of range') # Print error message
        else: # If the request was not successful
            print('request failed') # Print message indicating request failure

    elif choice == '3': # If the user chooses option 3
        team_number = int(input('Enter the team number: ')) # User selects team; input gets converted into an integer
        if r.status_code == 200: # Uses the status code to check if the request was successful
            if 1 <= team_number <= len(teams): # Check if the team number is within the range of available teams
                selected_team = teams[team_number - 1] # Get the selected team based on its index
                team_name = selected_team.get_text() # Get the text content of the selected team
            
                team_link = selected_team.find('a')['href'] # Find the link to the selected team's page
                team_url = "https://www.transfermarkt.com" + team_link # Construct the URL of the selected team's page

                team_response = requests.get(team_url, headers=userAgent) # Send a request to the selected team's page
                team_html = team_response.text # Get the html content of the response
                team_soup = bs4.BeautifulSoup(team_html, 'html.parser') # Parse the html content using Beuatiful soup

                players_table = team_soup.find('table', class_ ='items') # Find the table containing the players information
                
                players = players_table.find_all('td', class_ ='hauptlink') # Find all player names in the table
                print("Players:") # Print message indicating the list of players
                
                for player in players: # Iterate over each player
                    player_name = player.get_text(strip = True) # Get the text content of the player's names 
                    print(player_name) # Print the name(s)
        else: # If the request was not successful
            print('request failed') # Print message indicating request failure        
                
    elif choice == '4': # If user chooses option 4
        print('Exiting program') # Print exit statement
        break # Ends the while-loop
    else: # If the user did not choose a number between 1 and 4
        print('Invalid input') # Tells the user that the input is not possible