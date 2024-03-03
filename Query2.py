import os
from ply import yacc
from lexer2 import lexer, tokens
import requests

news = ""
# Define the grammar rules
def p_document(p):
    '''
    document : news_content
    '''

def p_news_content(p):
    '''
    news_content :  BEGINNEWS content ENDNEWS
                | BEGINRESPONSE content ENDRESPONSE
    '''

def p_content(p):
    '''
    content : SKIPTAG content content
            | TEXT content
            |
    '''
    global news
    if len(p)==3:
        news = p[1] + news



# Define error handling for parsing
def p_error(p):
    p.lexer.skip(1)
    #print(f"Syntax error at '{p.value}'")


def get_html_content(url):
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        }
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            return response.text
        else:

            print(f"Error: Failed to fetch content. Status code: {response.status_code}")
            return None

    except requests.RequestException as e:
        # Print an error message if there is an exception during the request
        print(f"Error: {e}")
        return None

def extract_data(html_content):
    lexer.input(html_content)
    result = parser.parse()

if __name__ == "__main__":
    parser = yacc.yacc()
    news_url = ['2019', '2023', '2024', 'January_2020', 'February_2020', 'March_2020', 'April_2020', 'May_2020', 'June_2020', 'July_2020', 'August_2020', 'September_2020', 'October_2020', 'November_2020', 'December_2020',
                'January_2021', 'February_2021', 'March_2021', 'April_2021', 'May_2021', 'June_2021', 'July_2021', 'August_2021', 'September_2021', 'October_2021', 'November_2021', 'December_2021',
                'January_2022', 'February_2022', 'March_2022', 'April_2022', 'May_2022', 'June_2022', 'July_2022', 'August_2022', 'September_2022', 'October_2022', 'November_2022', 'December_2022']
    
    try: 
        os.makedirs('News')
    except:
        pass
    url = 'https://en.wikipedia.org/wiki/Timeline_of_the_COVID-19_pandemic_in_'
    for timeline_url in news_url:
        web = url + timeline_url
        timeline_html_content = get_html_content(web)
        extract_data(timeline_html_content)
        with open(f'./News/{timeline_url}.txt', 'w', encoding='utf-8') as file:
            file.write(news)
     
    try: 
        os.makedirs('Response')
    except:
        pass
    url = 'https://en.wikipedia.org/wiki/Responses_to_the_COVID-19_pandemic_in_'
    for timeline_url in news_url[3:-2]:
        web = url + timeline_url
        timeline_html_content = get_html_content(web)
        extract_data(timeline_html_content)
        with open(f'./Response/{timeline_url}.txt', 'w', encoding='utf-8') as file:
            file.write(news)