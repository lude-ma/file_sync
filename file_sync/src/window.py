import Tkinter as tkinter
#import tkFileDialog as filedialog


from file_sync import WINDOW_NAME
from sync import sync


class Window(object):
    def __init__(self):
        self._root = tkinter.Tk()
        #self._root.title(WINDOW_NAME)
        #self._root.geometry('400x200')
        #self._source = tkinter.StringVar()
        #self._target = tkinter.StringVar()
        #self._copy = tkinter.IntVar()
        #self._construct()
        #tkinter.mainloop()

    def _construct(self):
        lbl1 = tkinter.Label(master=self._root, textvariable=self._source)
        lbl1.grid(row=0, column=1)
        button1 = tkinter.Button(text='Browse Source',
                                 command=self._browse_source)
        button1.grid(row=0, column=3)

        lbl2 = tkinter.Label(master=self._root, textvariable=self._target)
        lbl2.grid(row=1, column=1)
        button2 = tkinter.Button(text='Browse Target',
                                 command=self._browse_target)
        button2.grid(row=1, column=3)

        cb = tkinter.Checkbutton(master=self._root, text='create copy',
                                 variable=self._copy)
        cb.grid(row=2, column=1)

        button3 = tkinter.Button(text='Start', command=self._run_sync)
        button3.grid(row=3, column=1)

    def _browse_source(self):
        """Allow user to select a directory and store it in var self._source.

        :return: None
        """
        filename = '/'#filedialog.askdirectory()
        self._source.set(filename)

    def _browse_target(self):
        """Allow user to select a directory and store it in var self._target.

        :return: None
        """
        filename = '/'#filedialog.askdirectory()
        self._target.set(filename)

    def _run_sync(self):
        sync(self._source.get(), self._target.get(), bool(self._copy.get()))
