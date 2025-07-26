from search import open_link,search_youtube
from sysop import volume_down,volume_up,mute_volume,unmute_volume,shut_down,open_folder_by_name
from weather import get_weather_update
from main import news
def none():
    return f"Your query is ambigiuous"
function={
    "weather":get_weather_update,
    "vol_up":volume_up,
    "vol_down":volume_down,
    "terminate":shut_down,
    "navigate":open_folder_by_name,
    "browse":open_link,
    "youtube":search_youtube,
    "news":news,
    "none":none

}