import time

lyrics_with_custom_delays = [
    (0, "Ako'y alipin ng pag-ibig mo", 4.1),
    (4, "Handang ibigin ang 'sang tulad mo", 4.5),
    (9, "Hangga't ang puso mo'y sa akin lang", 2),
    (14, "Hindi ka na malilinlang", 2),
    (20, "Ikaw ang ilaw sa dilim", 1),
    (24, "At ang liwanag ng mga bituin", 2),
]

def print_lyrics():
    start_time = time.time() 
    for timestamp, line, custom_delay in lyrics_with_custom_delays:
        current_time = time.time() - start_time  
        if current_time < timestamp:
            time.sleep(timestamp - current_time)  

        for word in line.split(): 
            for char in word:  
                print(char, end='', flush=True) 
                time.sleep(0.09)  

            print(' ', end='', flush=True)  

        print()  
        time.sleep(custom_delay)  


print_lyrics()
