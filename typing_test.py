import time as tm
import random as rnd

def get_para_from_file(file_path):
    with open(file_path, 'r') as file:
        paragraphs = file.read().split('\n\n')
        return paragraphs

def typing_test(paragraph):
    print("Type the following paragraph:\n")
    print(paragraph)
    
    input("\nPress Enter when you are ready to start typing.\n")
    
    start_time = tm.time()
    usr_input = input("Start typing here: ")
    end_time = tm.time()
    
    return usr_input, end_time - start_time

def calculate_metrics(original_text, usr_input, elapsed_time):
    actual_words = original_text.split()
    typed_words = usr_input.split()
    
    correct_words = 0
    for w1, w2 in zip(actual_words, typed_words) :
        if w1 == w2 :
            correct_words += 1
    accuracy = (correct_words / len(actual_words)) * 100
    
    words_per_minute = (len(typed_words) / elapsed_time) * 60
    
    return accuracy, words_per_minute

def main():
    file_path = "sample_paragraphs.txt"  
    
    paragraphs = get_para_from_file(file_path)
    rnd.shuffle(paragraphs)
    
    paragraph = rnd.choice(paragraphs)
    usr_input, elapsed_time = typing_test(paragraph)
    accuracy, words_per_minute = calculate_metrics(paragraph, usr_input, elapsed_time)
    
    print("\nTyping Test Results:")
    print(f"Accuracy: {accuracy:.2f}%")
    print(f"Words per Minute: {words_per_minute:.2f}")
    print(f"Time Taken: {elapsed_time:.2f}")
    print("------------------------\n")

if __name__ == "__main__":
    main()
