import time as tm
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

def typing_test(paragraph):
    print("Type the following paragraph:\n")
    print(paragraph)
    
    input("\nPress Enter when you are ready to start typing.\n")
    
    start_time = tm.time()
    elapsed_time_list = []
    words_typed_list = []
    usr_input = ""
    
    while usr_input != paragraph:
        elapsed_time = tm.time() - start_time
        elapsed_time_list.append(elapsed_time)
        
        usr_input = input("Start typing here: ")
        
        # Count words typed
        words_typed = len(usr_input.split())
        words_typed_list.append(words_typed)

    return elapsed_time_list, words_typed_list

def update_plot(single_frame, elapsed_time_list, words_typed_list, line):
    if single_frame < len(elapsed_time_list):
        wpm = (words_typed_list[single_frame] / elapsed_time_list[single_frame]) * 60
        line.set_data(elapsed_time_list[:single_frame+1], [(w / t) * 60 for w, t in zip(words_typed_list[:single_frame+1], elapsed_time_list[:single_frame+1])])
        return line,

def main():
    # Provide a sample paragraph
    paragraph = "This is a sample paragraph for typing test."

    elapsed_time_list, words_typed_list = typing_test(paragraph)

    fig, ax = plt.subplots()
    line, = ax.plot([], [], marker='o')
    ax.set_xlabel('Time (seconds)')
    ax.set_ylabel('Words Per Minute (WPM)')
    ax.set_title('Words Per Minute Over Time')

    ani = FuncAnimation(fig, update_plot, frames=len(elapsed_time_list), fargs=(elapsed_time_list, words_typed_list, line), interval=1000, repeat=False)

    plt.show()

    # Keep the figure open until the animation is done
    plt.show()

if __name__ == "__main__":
    main()
