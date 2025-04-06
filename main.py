import rumps
from os import system
from collect_data import get_current_track

play_pause_script = "osascript -e 'tell application \"Spotify\" to playpause'"

class SpotifyStatusBarApp(rumps.App):
    def __init__(self):
        super(SpotifyStatusBarApp, self).__init__(get_current_track())
        #self.menu = ['play/plause']

    @rumps.clicked('play/pause')
    def idk(self, _):
        system(play_pause_script)

    @rumps.timer(1)
    def update_title(self, _):
        self.title = get_current_track()

if __name__ == '__main__':
    SpotifyStatusBarApp().run()