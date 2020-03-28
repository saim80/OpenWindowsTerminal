from subprocess import call
from fman import DirectoryPaneCommand
from fman.url import splitscheme, as_human_readable

class OpenWindowsTerminal(DirectoryPaneCommand):
    def __call__(self):
        url = self.pane.get_path()
        scheme, path = splitscheme(url)
        if scheme != 'file://':
            show_alert('No such path supported.')
            return
        local_path = as_human_readable(url)
        call(['wt', '-d', local_path])