from urllib.request import urlopen  #urllib handles the chinese character set better than requests
from bs4 import BeautifulSoup
import pandas as pd

masterDataFrame = pd.DataFrame(columns=['character', 'stroke_count'])

# There are 750 pages of characters on the website
for pageNumber in range(1, 751):
    try:
        url = "http://hanzidb.org/character-list/by-stroke-count?page=" + str(pageNumber)

        client = urlopen(url)
        page = client.read()
        client.close()
        
        #open the result with BS
        soup = BeautifulSoup(page, 'html.parser')

        characters = []
        character_counts = []

        for i, row in enumerate(soup.find_all('tr')):
            
            # the first tr is the header, skip that
            if i == 0: continue

            # extract the hanzi character - found in the link text within the first cell
            characters.append(row.td.a.text)

            # extract the number of strokes from the 5th column
            character_counts.append(row.find_all('td')[4].string)
        
        #build the dataframe from this page
        df = pd.DataFrame(list(zip(characters, character_counts)), columns=['character', 'stroke_count'])
        
        # add this page's dataframe to the master dataframe
        masterDataFrame = pd.concat([masterDataFrame, df])
    except Exception:
        # Dump what we've scraped so far
        masterDataFrame.to_csv('characters_and_strokes.csv', index=False)
        # show how far we made it, so we don't have to start from scratch next time
        print(f'error encountered after {pageNumber} pages')

# we've scraped it, export to a csv file for safekeeping
masterDataFrame.to_csv('characters_and_strokes.csv', index=False)