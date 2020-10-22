import matplotlib.pyplot as plt
from matplotlib.ticker import PercentFormatter
import numpy as np
import pandas as pd
import matplotlib.font_manager
from matplotlib.font_manager import FontProperties
import sinocrypt


def countCharacters(text):
    blankDict = dict()
    freqdict = dict()
    textLength = len(text)

    # Count the number of unique characters
    for i in text:
        if i in blankDict.keys():
            blankDict[i] += 1
        else:
            blankDict[i] = 1

    # Determine the frequency of each character
    for k, v in blankDict.items():
        freqdict[k] = round((v / textLength) * 100, 2)

    # Return a sorted list in descending frequency
    return(dict(sorted(freqdict.items(), key=lambda item: item[1], reverse=True)))


if __name__ == "__main__":

    # Initiate mpl
    fig = plt.figure()
    fig.suptitle("SinoCrypt v1.0 Frequency Analysis", fontsize=16)
    plt.subplot(2, 2, 1)

    # Frequency analysis for English language
    englishLetterFreq = {'E': 12.70, 'T': 9.06, 'A': 8.17, 'O': 7.51, 'I': 6.97, 'N': 6.75, 'S': 6.33, 'H': 6.09, 'R': 5.99, 'D': 4.25, 'L': 4.03, 'C': 2.78,
                         'U': 2.76, 'M': 2.41, 'W': 2.36, 'F': 2.23, 'G': 2.02, 'Y': 1.97, 'P': 1.93, 'B': 1.29, 'V': 0.98, 'K': 0.77, 'J': 0.15, 'X': 0.15, 'Q': 0.10, 'Z': 0.07}

    plt.bar(list(englishLetterFreq.keys()), list(englishLetterFreq.values()))
    plt.gca().set_title('English Language Distribution')

    # Frequency analysis for test plaintext
    plaintext = "sinocryptisnotoverlycryptographicallyrigidyetprogramaticallytriumphant"
    plt.subplot(2, 2, 2)
    count = countCharacters(str.upper(plaintext))
    plt.bar(count.keys(), count.values())
    plt.xticks(list(count.keys()))
    plt.gca().set_title('Plaintext Distribution')

    # Frequency analysis for v1.0 ciphertext
    ciphertext = "簿要算题大戳囔整魔是攀察德譬题囊只蹦然馕么翻鬣籍题来翻乙激经说个乙然就馕藩是进说从鬣去嚼器戳题时藤乚新乚灌是下乚道道馕嚼翻是霸新整所乚模魔"
    plt.subplot(2, 2, 3)
    ciCount = countCharacters(ciphertext)
    plt.bar(ciCount.keys(), ciCount.values())
    plt.gca().set_title('Ciphertext Distribution')

    # Set the xticks and change font so it can display chinese characters
    plt.xticks(list(ciCount.keys()))
    for tick in plt.gca().get_xticklabels():
        tick.set_fontname('SimSun')

    
    # Let's decode the ciphertext to make the analysis easier to understand
    plt.subplot(2, 2, 4)
    keys = []
    for i in ciCount.keys():
        keys.append(str.upper(sinocrypt.decrypt(i)))

    # use np.arange() or it'll drop duplicate x tick values
    N = len(keys)
    ind = np.arange(N)
    
    plt.bar(ind, ciCount.values())
    plt.xticks(ind, keys)
    plt.gca().set_title('Decoded Ciphertext Distribution')

    # Format the axes
    for axis in fig.get_axes():
        axis.set_ylim([0, 13])
        axis.yaxis.set_major_formatter(PercentFormatter())

    # Display the plots
    plt.show()