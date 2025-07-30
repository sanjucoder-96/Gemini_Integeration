
import os
import subprocess


def volume_up():
    os.system("nircmd.exe changesysvolume 5000")
    return "volume increased"

def volume_down():
    os.system("nircmd.exe changesysvolume -5000")
    return "volume decreased"

def mute_volume():
    os.system("nircmd.exe mutesysvolume 1")
    return "muted volume"

def unmute_volume():
    os.system("nircmd.exe mutesysvolume 2")
    return "unmuted volume"

def shut_down():
    os.system("shutdown /s /t 5")
    return "Terminating....."



folder_shortcuts = {
    "downloads": os.path.expanduser("~\\Downloads"),
    "documents": os.path.expanduser("~\\Documents"),
    "pictures": os.path.expanduser("~\\Pictures"),
    "music": os.path.expanduser("~\\Music"),
    "desktop": os.path.expanduser("~\\Desktop")
}

def open_folder_by_name(name):
    path = folder_shortcuts.get(name.lower())
    if path and os.path.exists(path):
        os.startfile(path)
        return f"Opening {name} folder"
    else:
        return f"Folder '{name}' not found"
