import itertools
from tkinter import *
from typing_para_list import content


class SpeedWindow(Tk):
    def __init__(self):
        super().__init__()
        self.title('Speed typing test app')
        self.config(pady=50, padx=50, bg='#68b0e6')
        self.maxsize(1000, 1000)
        self.title_label()
        self.timer_label()
        self.typing_area()
        self.reset()
        self.start()
        self.hidden_tag()

        self.typed_list = []
        self.stop = None
        # the below is declared to check the textbox with user key input
        self.typing_position = 0

    def title_label(self):
        self.label = Label(text='1 Minute Type test', pady=25, font=('Arial', 20, 'bold'), bg='#68b0e6', fg='white')
        self.label.grid(row=0, column=0, sticky='e')

    def timer_label(self):
        self.time = Label(text='Timer:60 Secs', pady=25, bg='#68b0e6', font=('Arial', 15, 'bold'), fg='white')
        self.time.grid(row=1, column=0)

    def typing_area(self):
        self.textarea = Text(font=('lucida', 15), wrap="word", height=10, width=40, pady=10, padx=10, fg='grey')
        self.textarea.grid(row=2, column=0, columnspan=2, pady=20)
        self.textarea.insert('1.0', 'Press start button to access your typing speed.......')
        self.textarea.tag_config("correct", foreground="black")
        self.textarea.tag_config("incorrect", foreground="red")
        # self.textarea.bind("<<Modified>>", self.on_text_change)

    def reset(self):
        self.reset_button = Button(text='Restart', padx=5, pady=5, bg='#FFD6A5', command=self.restart, state='disabled')
        self.reset_button.grid(row=3, column=0, sticky='w')

    def start(self):
        self.start_button = Button(text='Start', padx=9, pady=6, bg='#FFD6A5', command=self.start_action)
        self.start_button.grid(row=3, column=1, sticky='e')

    # the entry widget is hidden so that user can focus fully on text widget with highlighting color as their reference
    def hidden_tag(self):
        self.hide = Entry(bg='#68b0e6', fg='#68b0e6', borderwidth=0, highlightthickness=0, insertbackground='#68b0e6') # last keyargs is to make cursor invisible
        self.hide.grid(row=4, column=0)
        self.hide.bind("<KeyRelease>", self.start_check)

    def start_action(self):
        self.textarea.delete('1.0', END)
        typing_material = content()
        self.hide.focus_set()
        self.textarea.insert('1.0', typing_material)
        self.time.config(text='Timer:60 Secs')
        self.start_button.config(state='disabled')
        time = 59
        self.reset_button.config(state='normal')
        self.after(2000, self.timer, time)

##########################Working of timer, calculation and textdetection###############################################
    def restart(self):
        try:
            self.new_root.destroy()
        except:
            pass
        self.after_cancel(self.stop)
        self.time.config(fg="white")
        self.typed_list = []
        self.typing_position = 0
        self.start_action()
        self.start_button.config(state='active', bg='#FFD6A5')

    def timer(self, time):
        if time < 0:
            self.after_cancel(self.stop)
            self.time.config(text="Time's Up......", fg='black')
            self.result_window()
            self.final_calculations()
            self.reset_button.config(state='normal')
        elif time < 10:
            self.time.config(text=f'Timer:{time} Secs', fg='red')
            self.stop = self.after(1000, self.timer, time - 1)
        elif time < 60:
            self.time.config(text=f'Timer:{time} Secs')
            self.stop = self.after(1000, self.timer, time - 1)

    def start_check(self, event):
        typed = event.char   #can't use event.keysym because of list calculations and spaces
        if typed == 'BackSpace' or typed == 'Delete' or event.keysym == 'Alt_L' or event.keysym == 'Alt_R' \
                or event.keysym == 'Shift_L' or event.keysym == 'Shift_R' or event.keysym == 'Control_L' \
                or event.keysym == 'Control_R':
            # when user user the above keys the typing list is not appended
            return 'break'
        else:
            self.typed_list.append(typed)
        if self.typed_list[self.typing_position] == self.textarea.get('1.0', END)[self.typing_position]:
            self.textarea.tag_add('correct', f'1.{self.typing_position}')  #higlighling the text black
        else:
            self.textarea.tag_add('incorrect', f'1.{self.typing_position}') #highlighting the text red
        self.typing_position += 1

        # Check if the highlighter has reached predetermined typing position, so that the textarea can scroll for user to see below text
        if int(self.textarea.index(f'1.{self.typing_position}').split('.')[1]) % 400 == 0:
            self.textarea.yview_scroll(8, 'units')  # scrolls the textarea by 8 lines

    def final_calculations(self):
        # IF USER DOES NOT TYPE ANYTHING
        if not self.typed_list:
            words_per_minute = 0
            self.wpm_value.config(text=f'{words_per_minute} wpm')
            acc = 0
            self.accuracy.config(text=f'{acc}%')
            self.get_highscore(words_per_minute, acc)
        else:
            # filtered_list = list((filter(None, self.typed_list)))  # used to filter shift key to mitigate none values
            content = self.textarea.get('1.0', END)
            # Calculating words per minute
            typingarea_content = [item for item in content]   # can use split() instead of grouping down below
            correct_words = [''.join(group) for key, group in itertools.groupby(typingarea_content[:len(self.typed_list)],    # to get words from text area till where the user has stopped
                                                                                lambda x: x == " ") if not key]
            # THe below step is done so that if the user enters any words , space without looking at the paragraph to achieve maximum speed , this step keeps the user in check
            typed_words = [letter for letter in self.typed_list if letter != ' '] # Removes space
            for i in range(len(self.typed_list)):  # THis step introduces space in the typed_words according to paragraph so that extra space does not affect the list
                if typingarea_content[i] == ' ':
                    typed_words.insert(i, ' ')
            user_words = [''.join(group) for key, group in itertools.groupby(typed_words, lambda x: x == " ") if
                          not key]  # will work only if grouping elements are next to each other
            missed_words = sum([1 for u, c in zip(user_words, correct_words) if u != c])

            # Calculating the words per minute
            mins = 1
            words_per_minute = (len(self.typed_list)/5 - missed_words)/mins
            self.wpm_value.config(text=f'{round(words_per_minute, 2)} wpm')

            #Calculating the accuracy    Note: please note one can even user (correct characters/total characters)--> typed
            acc = (len(correct_words)-missed_words)/len(correct_words) * 100
            self.accuracy.config(text=f'{acc:.2f}%')

            # High score
            self.get_highscore(words_per_minute, acc)

    def get_highscore(self, words_per_minute, acc):
        # High score storing and displaying
        with open('highscore.txt') as f:
            score = f.read()
            high_score = float(score.split()[0])
            accuracy = float(score.split()[1])
            self.highscore_val.config(text=f'{high_score} with {accuracy:.2f} accuracy')
            # comparing highest score with current score and accuracy of 45 is kept so that when user types randomly fast it does not count as highest score
            if words_per_minute > high_score and acc >= 45:
                with open('highscore.txt', 'w') as f:
                    f.write(f'{words_per_minute} {acc}')
            elif words_per_minute == high_score and acc >= 45:
                if acc >= accuracy:
                    with open('highscore.txt', 'w') as f:
                        f.write(f'{words_per_minute} {acc}')

################################################################################################################

##########################new window popup results###############################################
    def result_window(self):
        self.new_root = Toplevel()
        self.new_root.minsize(250, 250)
        self.new_root.title('Typing Result')
        self.new_root.config(padx=20, pady=20, bg='#1D5D9B')
        self.new_root.geometry('+%d+%d' % (self.winfo_x()+550, self.winfo_y()+150))
        self.new_root.protocol("WM_DELETE_WINDOW", self.on_result_window_close)   # using this so that when new window is closed using 'X' the start button is activated again

        self.final_label()
        self.words_per_minute()
        self.wpm()
        self.accuracy_label()
        self.accuracy_percent()
        self.high_score_label()
        self.high_score()
        self.close()

    def final_label(self):
        self.final_tag = Label(self.new_root, text='Great!! Your Results', bg='#1D5D9B', font=('lucida', 20, 'bold'), fg='#F6F4EB')
        self.final_tag.grid(row=0, column=0, pady=10)

    def words_per_minute(self):
        self.wpm_label = Label(self.new_root, text='Words per minute:', bg='#1D5D9B', font=('arial', 15), fg='#F6F4EB')
        self.wpm_label.grid(row=1, column=0)

    def wpm(self):
        self.wpm_value = Label(self.new_root, text='wpm', bg='#1D5D9B', font=('arial', 15, 'bold'), fg='#F6F4EB')
        self.wpm_value.grid(row=1, column=1)

    def accuracy_label(self):
        self.accuracy_lbl = Label(self.new_root, text='Accuracy:', bg='#1D5D9B', font=('arial', 15), fg='#F6F4EB')
        self.accuracy_lbl.grid(row=2, column=0)

    def accuracy_percent(self):
        self.accuracy = Label(self.new_root, text='wpm', bg='#1D5D9B', font=('arial', 15, 'bold'), fg='#F6F4EB')
        self.accuracy.grid(row=2, column=1)

    def high_score_label(self):
        self.highscore_lbl = Label(self.new_root, text='Highest Score:', bg='#1D5D9B', font=('arial', 15), fg='#F6F4EB')
        self.highscore_lbl.grid(row=3, column=0)

    def high_score(self):
        self.highscore_val = Label(self.new_root, text='highscore', bg='#1D5D9B', font=('arial', 15, 'bold'), fg='#F6F4EB')
        self.highscore_val.grid(row=3, column=1)

    def close(self):
        self.close_button = Button(self.new_root, text='Close', padx=9, pady=6, bg='#FFD6A5', command=self.quit_function)
        self.close_button.grid(row=4, column=0, padx=20, pady=20, sticky='e')

    def quit_function(self):
        self.start_button.config(state='active', bg='#FFD6A5')
        self.new_root.destroy()

    def on_result_window_close(self):
        self.new_root.destroy()
        self.start_button.config(state='active', bg='#FFD6A5')
################################################################################################################


if __name__ == '__main__':
    window = SpeedWindow()
    window.mainloop()

