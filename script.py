import matplotlib.pyplot as plt
import matplotlib.style as style
import numpy as np
import random
style.use('seaborn-poster')
######################################################
states = ["Free Energy Principle", "Trolley Problem", "Active Inference", "Bees", "Theory of Mind", 
          "Rubber Hand Illusion", "Water Polo", "ChatGPT", "Foundation Model", "Emergent", 
          "Benchmark", "Sunshine", "Neural Oscillations", "Connectome", "Karl Friston", 
          "Deep learning", "Möhnesee", "Embodiment", "Predictive Processing", "Leaky Integrate-and-Fire", "Consciousness", "Big Data", "Language model", "Valence"]
terms = [s.strip() for s in states]
########################################################
for t in range(1,101,1):
    if t == 1:
            random.shuffle(terms)
            terms.insert(12,"Free")
    else:
            terms.pop(12)
            random.shuffle(terms)
            terms.insert(12,"Free")
    
    rowlen= 5  # makes a 5x5 bingo board

    fig = plt.figure()
    ax = fig.gca()
    ax.set_xticks(np.arange(0, rowlen + 1))
    ax.set_yticks(np.arange(0, rowlen + 1))
    ax.set_xticklabels([])
    ax.set_yticklabels([])
    plt.grid(color='black',linewidth=1)
    for i, word in enumerate(terms[:rowlen**2]):
            x = (i % rowlen) + 0.5 - len(word)/50
            y = int(i / rowlen) + 0.45
            ax.annotate(word, xy=(x, y), xytext=(x, y))
            
    #plt.show()
    fig.savefig("%s-Bingo.pdf" %t)