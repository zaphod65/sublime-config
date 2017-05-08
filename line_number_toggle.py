import sublime
import sublime_plugin
class ToggleLineNumberCommand(sublime_plugin.ApplicationCommand):
    def run(self):
        settings = sublime.load_settings("Preferences.sublime-settings")
        line_numbers = not settings.get("line_numbers")
        settings.set('line_numbers', line_numbers)
        sublime.save_settings("Preferences.sublime-settings")