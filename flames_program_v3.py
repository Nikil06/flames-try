import customtkinter as ctk
from flames_module import Flames
from flames_module import HistoryItem

ctk.set_appearance_mode('dark')
ctk.set_default_color_theme('green')
currentFrame = ''
flameFrameName, historyFrameName, creditsFrameName = "Flame Test", "History", "Credits"


class BaseFrameTab(ctk.CTkFrame):
    def __init__(self, master):
        super(BaseFrameTab, self).__init__(master = master, width = 420,
                                           height = 340, fg_color = 'transparent')
        self.pack(padx = 10, pady = 10, fill = 'both', expand = True)


class FlamesFrame(BaseFrameTab):

    def __init__(self, master):
        super(FlamesFrame, self).__init__(master)

        title_label = ctk.CTkLabel(master = self, text = 'F.L.A.M.E.S.',
                                   font = ctk.CTkFont(size = 25), height = 2)
        title_label.pack(pady = 10)

        empty_label1 = ctk.CTkLabel(master = self, text = '', height = 10)
        empty_label1.pack(fill = 'x', pady = 0)

        self.Entry1_frame = ctk.CTkFrame(master = self, height = 10)
        self.Entry1_frame.pack(fill = 'x', pady = 10)

        self.Entry2_frame = ctk.CTkFrame(master = self, height = 10)
        self.Entry2_frame.pack(fill = 'x', pady = 10)

        empty_label1 = ctk.CTkLabel(master = self, text = '', height = 5)
        empty_label1.pack(fill = 'x', pady = 0)

        self.button_frame = ctk.CTkFrame(master = self, height = 15)
        self.button_frame.pack(fill = 'x', pady = 10)

        Name1Label = ctk.CTkLabel(master = self.Entry1_frame, text = 'Candidate 1:-',
                                  font = ctk.CTkFont(size = 16))
        Name1Label.pack(side = ctk.LEFT, padx = 10, fill = 'x', expand = True)

        self.Name1Entry = ctk.CTkEntry(master = self.Entry1_frame, placeholder_text = "Candidate 1")
        self.Name1Entry.pack(side = ctk.RIGHT, fill = 'x', expand = True)

        Name2Label = ctk.CTkLabel(master = self.Entry2_frame, text = 'Candidate 2:-',
                                  font = ctk.CTkFont(size = 16))
        Name2Label.pack(padx = 10, side = ctk.LEFT, fill = 'x', expand = True)

        self.Name2Entry = ctk.CTkEntry(master = self.Entry2_frame, placeholder_text = "Candidate 2")
        self.Name2Entry.pack(side = ctk.RIGHT, fill = 'x', expand = True)

        self.FlameButton = ctk.CTkButton(master = self.button_frame, text = 'FLAME',
                                         command = lambda: onFlamePressed(self, app))
        self.FlameButton.pack(padx = 10, side = 'left', fill = 'x', expand = True)

        self.ResetButton = ctk.CTkButton(master = self.button_frame, text = 'Reset',
                                         command = lambda: onResetPressed(self))
        self.ResetButton.pack(padx = 10, side = ctk.RIGHT, fill = 'x', expand = True)

        self.relation_status = ctk.CTkLabel(master = self, text = '', wraplength = 350,
                                            font = ctk.CTkFont(size = 16))
        self.relation_status.pack(pady = 5)

        self.comment_label = ctk.CTkLabel(master = self, text = '', wraplength = 400,
                                          font = ctk.CTkFont(size = 14))
        self.comment_label.pack(pady = 5)


class HistoryFrame(BaseFrameTab):

    def __init__(self, master):
        super(HistoryFrame, self).__init__(master)

        self.label = ctk.CTkLabel(self, text = 'History', font = ctk.CTkFont(size = 28))
        self.label.pack(pady = 10)

        self.history_frame = ctk.CTkFrame(self)
        self.history_frame.pack(fill = 'both', padx = 10, pady = 10, expand = True)

        self.scrollable_label_button_frame = ScrollableLabelButtonFrame(master = self.history_frame,
                                                                        command = self.label_button_frame_event)
        self.scrollable_label_button_frame.pack(fill = 'both', padx = 10, pady = 10, expand = True)

    def label_button_frame_event(self, item):
        print(f"Deleted {item}")
        self.scrollable_label_button_frame.remove_item(item)


class ScrollableLabelButtonFrame(ctk.CTkScrollableFrame):
    def __init__(self, master, command=None, **kwargs):
        super().__init__(master, **kwargs)
        self.grid_columnconfigure(0, weight=1)

        self.command = command
        self.label_list = []
        self.button_list = []
        self.item_list = []

    def add_item(self, item: HistoryItem):
        count = self.item_list.count(item)
        if count > 0:
            print('Already added')
            return
        else:
            label = ctk.CTkLabel(self, text = item.display_str, compound = "left", padx = 5, anchor = "w")
            button = ctk.CTkButton(self, text = "Del", width = 25, height = 24)
            if self.command is not None:
                button.configure(command = lambda: self.command(item))
            label.grid(row = len(self.label_list), column = 0, pady = (0, 10), sticky = "w")
            button.grid(row = len(self.button_list), column = 1, pady = (0, 10), padx = 5)
            self.label_list.append(label)
            self.button_list.append(button)
            self.item_list.append(item)

    def remove_item(self, item):
        for label, button in zip(self.label_list, self.button_list):
            if item == label.cget("text"):
                label.destroy()
                button.destroy()
                self.label_list.remove(label)
                self.button_list.remove(button)
                return


class CreditsFrame(BaseFrameTab):

    def __init__(self, master):
        super(CreditsFrame, self).__init__(master)

        self.label = ctk.CTkLabel(self, text = 'Credits page', font = ctk.CTkFont(size = 28))
        # self.label.grid(row = 0)
        self.label.pack()


def onResetPressed(frame: FlamesFrame):
    entry1 = frame.Name1Entry.get()
    entry2 = frame.Name2Entry.get()

    if entry1 != '':
        frame.Name1Entry.delete(0, ctk.END)
    if entry2 != '':
        frame.Name2Entry.delete(0, ctk.END)

    frame.relation_status.configure(True, text = '')
    frame.comment_label.configure(True, text = '')


class NavFrame(ctk.CTkFrame):
    def __init__(self, master):
        super(NavFrame, self).__init__(master, width = 180, height = 340)
        self.pack(side = 'right', padx = 10, pady = 10, fill = 'y')

        # Test Area
        self.flame_navButton = ctk.CTkButton(self, text = 'FLAME Test', corner_radius = 0,
                                             command = lambda: navigateFrames(app, flameFrameName))
        # self.flame_navButton.grid(row = 0, padx = 5, pady = 5)
        self.flame_navButton.pack(padx = 5, pady = 5)

        # History Nav button
        self.history_navButton = ctk.CTkButton(self, text = 'History', corner_radius = 0,
                                               command = lambda: navigateFrames(app, historyFrameName))
        # self.history_navButton.grid(row = 1, padx = 5, pady = 5)
        self.history_navButton.pack(padx = 5, pady = 5)

        # Credits Nav Button
        self.credits_navButton = ctk.CTkButton(self, text = 'Credits', corner_radius = 0,
                                               command = lambda: navigateFrames(app, creditsFrameName))
        # self.credits_navButton.grid(row = 2, padx = 5, pady = 5)
        self.credits_navButton.pack(padx = 5, pady = 5)


class App(ctk.CTk):

    def __init__(self):
        super(App, self).__init__()

        self.width = 640
        self.height = 360
        self.current_frame = flameFrameName

        self.title_name = 'F.L.A.M.E.S.'
        self.geometry(f'{self.width}x{self.height}')
        self.resizable(True, True)
        self.title(self.title_name)

        self.main_frame = ctk.CTkFrame(self, width = 420, height = 340)
        self.main_frame.pack(side = 'right', padx = 10, pady = 10, fill = 'both', expand = True)

        self.flames_frame = FlamesFrame(self.main_frame)
        self.history_frame = HistoryFrame(self.main_frame)
        self.credits_frame = CreditsFrame(self.main_frame)

        self.nav_frame = NavFrame(self)
        self.nav_frame.pack(fill = 'y', padx = 10, pady = 10)

        if self.current_frame == flameFrameName:
            self.bind('<Return>', lambda event: onFlamePressed(self.flames_frame, self))
            self.bind('<Escape>', lambda event: onResetPressed(self.flames_frame))


def navigateFrames(_app: App, frameName: str):
    nav_frame = _app.nav_frame

    nav_frame.flame_navButton.configure(fg_color = "green" if frameName == flameFrameName else 'transparent')
    nav_frame.history_navButton.configure(fg_color = "green" if frameName == historyFrameName else 'transparent')
    nav_frame.credits_navButton.configure(fg_color = "green" if frameName == creditsFrameName else 'transparent')

    if frameName == flameFrameName:
        _app.flames_frame.pack(fill = "both", expand = True)
        currentFrame = flameFrameName
    else:
        _app.flames_frame.pack_forget()
    if frameName == historyFrameName:
        _app.history_frame.pack(fill = "both", expand = True)
        currentFrame = historyFrameName
    else:
        _app.history_frame.pack_forget()
    if frameName == creditsFrameName:
        _app.credits_frame.pack(fill = "both", expand = True)
        currentFrame = creditsFrameName
    else:
        _app.credits_frame.pack_forget()


def onFlamePressed(frame: FlamesFrame, _app: App):
    name1 = str(frame.Name1Entry.get())
    name2 = str(frame.Name2Entry.get())

    if name1 == '' or name2 == '':
        pass
    else:
        flames = Flames(name1, name2)
        flames.flameTest()
        frame.relation_status.configure(text = f"{name1.capitalize()} and {name2.capitalize()}" +
                                               f" have their results as {flames.relationStatus}")
        frame.comment_label.configure(text = flames.comment)

        item = HistoryItem(name1, name2, flames.relationStatus)
        if not _app.history_frame.scrollable_label_button_frame.item_list.count(item) > 0:
            _app.history_frame.scrollable_label_button_frame.add_item(item)


app = App()
navigateFrames(app, historyFrameName)
app.mainloop()
