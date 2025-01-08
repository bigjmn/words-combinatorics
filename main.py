import numpy as np 
import matplotlib.pyplot as plt

from calculate_combos import word_dist, chars_to_combos 

WORDLIST_PATH = "wordlist.txt"
WORDBLOCKS = 3 
PLOT_RANGE = [5,30]

LOG_SCALE = True 

def main():
    vectorized_combos = np.vectorize(lambda x: chars_to_combos(x, wordlengths_arr, WORDBLOCKS))

    wordlengths_arr = word_dist(WORDLIST_PATH)
    x_min, x_max = PLOT_RANGE 
    x_axis = np.linspace(x_min, x_max, (x_max-x_min), dtype=int)

    w_heights = vectorized_combos(x_axis)
    loglabel = ""
    fig, ax = plt.subplots()
    
    
    # y_axis = chars_to_combos(x_axis, wordlengths_arr, WORDBLOCKS)

    ax.bar(x_axis, w_heights)
    plt.xlabel('Characters (including hyphens)')
    plt.ylabel('(common) word combinations')
    if LOG_SCALE:
        ax.set_yscale('log')
        
        loglabel = " (logarithic)"
    plt.title(f"password combos of {WORDBLOCKS} words{loglabel}")
    
    plt.show()

if __name__ == "__main__":
    main()