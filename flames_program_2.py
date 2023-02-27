import customtkinter as ctk
import flames_module

ctk.set_appearance_mode('dark')
ctk.set_default_color_theme('green')
currentFrame = ''
flameFrameName, historyFrameName, creditsFrameName = "Flame Test", "History", "Credits"


class BaseFrameTab(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super(BaseFrameTab, self).__init__(master)

        width = 300
        height = 340

        self.configure(True, width = width, height = height)
        self.pack(side = 'right', fill = "y", padx = 10, pady = 10, expand = True)


class FlamesFrame(BaseFrameTab):

    def __init__(self, master, **kwargs):
        super(FlamesFrame, self).__init__(master, **kwargs)

        title_label = ctk.CTkLabel(master = self, text = 'F.L.A.M.E.S.',
                                   font = ctk.CTkFont(size = 25))
        title_label.grid(row = 0, columnspan = 2, pady = 10, sticky = 'ew')

        empty_label1 = ctk.CTkLabel(master = self, text = '')
        empty_label1.grid(row = 1)

        Name1Label = ctk.CTkLabel(master = self, text = 'Candidate 1:- ',
                                  font = ctk.CTkFont(size = 16))
        Name1Label.grid(row = 2, column = 0, pady = 5)

        self.Name1Entry = ctk.CTkEntry(master = self, placeholder_text = "Candidate 1")
        self.Name1Entry.grid(row = 2, column = 1, pady = 5)

        Name2Label = ctk.CTkLabel(master = self, text = 'Candidate 2:- ',
                                  font = ctk.CTkFont(size = 16))
        Name2Label.grid(row = 3, column = 0, pady = 5)

        self.Name2Entry = ctk.CTkEntry(master = self, placeholder_text = "Candidate 2")
        self.Name2Entry.grid(row = 3, column = 1, pady = 5)

        self.FlameButton = ctk.CTkButton(master = self, text = 'FLAME',
                                         command = lambda: onFlamePressed(self))
        self.FlameButton.grid(row = 5, column = 0, padx = 10, pady = 15, sticky = 'ew')

        self.ResetButton = ctk.CTkButton(master = self, text = 'Reset',
                                         command = lambda: onResetPressed(self))
        self.ResetButton.grid(row = 5, column = 1, pady = 5, padx = 5, sticky = 'ew')

        self.relation_status = ctk.CTkLabel(master = self, text = '', wraplength = 350,
                                            font = ctk.CTkFont(size = 16))
        self.relation_status.grid(row = 6, columnspan = 2, pady = 10, sticky = 'ew')

        self.comment_label = ctk.CTkLabel(master = self, text = '', wraplength = 350,
                                          font = ctk.CTkFont(size = 14))
        self.comment_label.grid(row = 7, columnspan = 2, pady = 10, sticky = 'ew')

        for i in range(self.grid_size()[0]):
            self.columnconfigure(index = i, weight = 1)


''''
class NavFrame(ctk.CTkFrame):
    def __init__(self, master, _app: App):
        super(NavFrame, self).__init__(master = master, width = 200, height = 340)

        self.FlameNav_button = ctk.CTkButton(self, text = 'Flame Test',
                                             command = lambda: navigateFrames(self, _app, flameFrameName))
        self.FlameNav_button.grid(row = 0, padx = 5, pady = 5)

        self.HistoryNav_button = ctk.CTkButton(self, text = 'History',
                                               command = lambda: navigateFrames(self, _app, historyFrameName))
        self.HistoryNav_button.grid(row = 1, padx = 5, pady = 5)

        self.CreditsNav_button = ctk.CTkButton(self, text = 'Credits',
                                               command = lambda: navigateFrames(self, _app, creditsFrameName))
        self.CreditsNav_button.grid(row = 2, padx = 5, pady = 5)

        navigateFrames(self, _app, flameFrameName)
'''
'''
def navigateFrames(navFrame: NavFrame, _app: App, frameName: str):
    if frameName == flameFrameName:
        navFrame.CreditsNav_button.configure(True, fg_color = 'transparent')
        navFrame.HistoryNav_button.configure(True, fg_color = 'transparent')
        navFrame.FlameNav_button.configure(True, fg_color = 'green')
        currentFrame = flameFrameName
    elif frameName == historyFrameName:
        navFrame.CreditsNav_button.configure(True, fg_color = 'transparent')
        navFrame.FlameNav_button.configure(True, fg_color = 'transparent')
        navFrame.HistoryNav_button.configure(True, fg_color = 'green')
        currentFrame = historyFrameName
    elif frameName == creditsFrameName:
        navFrame.FlameNav_button.configure(True, fg_color = 'transparent')
        navFrame.HistoryNav_button.configure(True, fg_color = 'transparent')
        navFrame.CreditsNav_button.configure(True, fg_color = 'green')
        currentFrame = creditsFrameName
    else:
        print('ERROR in navigation between frame')
    
    if frameName == flameFrameName:
        _app.flames_frame.grid(row = 0, column = 1, sticky = "nsew")
    else:
        _app.flames_frame.grid_forget()

    if frameName == historyFrameName:
        _app.history_frame.grid(row = 0, column = 1, sticky = "nsew")
    else:
        _app.history_frame.grid_forget()

    if frameName == creditsFrameName:
        _app.credits_frame.grid(row = 0, column = 1, sticky = "nsew")
    else:
        _app.credits_frame.grid_forget()
'''


def onResetPressed(frame: FlamesFrame):
    entry1 = frame.Name1Entry.get()
    entry2 = frame.Name2Entry.get()

    if entry1 != '':
        frame.Name1Entry.delete(0, ctk.END)
    if entry2 != '':
        frame.Name2Entry.delete(0, ctk.END)

    frame.relation_status.configure(True, text = '')
    frame.comment_label.configure(True, text = '')


def onFlamePressed(frame: FlamesFrame):
    name1 = str(frame.Name1Entry.get())
    name2 = str(frame.Name2Entry.get())

    if name1 == '' or name2 == '':
        pass
    else:
        flames = flames_module.Flames(name1, name2)
        flames.flameTest()
        frame.relation_status.configure(text = f"{name1.capitalize()} and {name2.capitalize()}" +
                                               f" have their results as {flames.relationStatus}")
        frame.comment_label.configure(text = flames.comment)


class NavFrame(ctk.CTkFrame):
    def __init__(self, master):
        super(NavFrame, self).__init__(master = master)

        self.configure(True, width = 300, height = 340)

        empty_label = ctk.CTkLabel(self, text = '')
        empty_label.grid(row = 0, pady = 10)

        self.FlameNav_button = ctk.CTkButton(self, text = 'Flame Test',
                                             command = lambda: print('navigate flame tab'))
        self.FlameNav_button.grid(row = 1, padx = 5, pady = 5)

        self.HistoryNav_button = ctk.CTkButton(self, text = 'History',
                                               command = lambda: print('navigate history tab'))
        self.HistoryNav_button.grid(row = 2, padx = 5, pady = 5)

        self.CreditsNav_button = ctk.CTkButton(self, text = 'Credits',
                                               command = lambda: print('navigate credits tab'))
        self.CreditsNav_button.grid(row = 3, padx = 5, pady = 5)


class App(ctk.CTk):

    def __init__(self):
        super(App, self).__init__()

        self.width = 640
        self.height = 360
        self.current_frame = flameFrameName

        self.title_name = 'F.L.A.M.E.S.'
        self.geometry(f'{self.width}x{self.height}')
        self.resizable(False, False)
        self.title(self.title_name)

        self.nav_frame = NavFrame(self)
        self.nav_frame.pack(side = 'left', fill = "both", padx = 10, pady = 10)

        self.flames_frame = FlamesFrame(self).pack(side = 'left', fill = "both", padx = 10, pady = 10)
        # self.history_frame = BaseFrameTab(self)
        # self.credits_frame = BaseFrameTab(self)

        if self.current_frame == flameFrameName:
            self.bind('<Return>', lambda event: onFlamePressed(self.flames_frame))
            self.bind('<Escape>', lambda event: onResetPressed(self.flames_frame))

    def navigate_frames(self):
        pass


app = App()

app.mainloop()
