"""
Anthony Quinn
19/01/2021
Web scraping the lottery.ie website.
"""

from bs4 import BeautifulSoup
import requests

def lottoNumber():
    html_text = requests.get('https://www.lottery.ie/draw-games/results/view?game=lotto').text
    soup = BeautifulSoup(html_text, 'lxml')
    lotto = soup.find('div', class_= 'draw-results draw-results-view clearfix')
    lotto_winning_number = lotto.find('div', class_='bonus')
    lotto_winning_number_label = lotto_winning_number.find('label').text
    return lotto_winning_number_label

print(" " + lottoNumber())