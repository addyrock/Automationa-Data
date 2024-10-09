import pandas as pd
import folium
from branca.element import Template, MacroElement

# Load the CSV file
df = pd.read_csv(r'C:\Users\arslan.arif\PycharmProjects\pythonProject2\Weather\Sites.csv')

# Specify the latitude and longitude for the initial center of the map
initial_lat = 31.517416  # Replace with your desired latitude
initial_lon = 74.37591  # Replace with your desired longitude

# Create a map centered at the specified location using OpenStreetMap tiles
mymap = folium.Map(location=[initial_lat, initial_lon], zoom_start=12, tiles='https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', attr='© OpenStreetMap contributors')
tiles='Select Division'
# Path to the traffic light icon
traffic_light_icon_path = r'C:\\Users\\arslan.arif\\PycharmProjects\\pythonProject2\\Weather\\2385317.png'

# Create a feature group for each division
division_groups = {}
for division in df['Division'].unique():
    division_groups[division] = folium.FeatureGroup(name=division)

# Add points to the map with detailed popups and labels, organized by division
for idx, row in df.iterrows():
    popup_content = f"""
    <b>Sr. No.:</b> {row['Sr. No.']}<br>
    <b>Site Name:</b> {row['Site Name']}<br>
    <b>Division:</b> {row['Division']}<br>
    <b>Road Name:</b> {row['Road Name']}<br>
    <b>Latitude:</b> {row['Latitude']}<br>
    <b>Longitude:</b> {row['Longitude']}<br>
    <b>Site Type:</b> {row['Site Type']}<br>
    <b>Side ID:</b> {row['Site ID']}
    """
    tooltip_content = row['Site Name']
    icon = folium.CustomIcon(traffic_light_icon_path, icon_size=(15, 30))
    marker = folium.Marker(
        location=[row['Latitude'], row['Longitude']],
        popup=folium.Popup(popup_content, max_width=300),
        tooltip=folium.Tooltip(tooltip_content),
        icon=icon
    )
    division_groups[row['Division']].add_child(marker)

# Add each division group to the map
for division, group in division_groups.items():
    mymap.add_child(group)

# Add LayerControl to switch between divisions
folium.LayerControl(collapsed=False).add_to(mymap)

# Create the dropdown menu with radio buttons
template = """
{% macro html(this, kwargs) %}
<!DOCTYPE html>
<html>
<head>
    <style>
        .control-panel {
            background-color: white;
            padding: 10px;
            border-radius: 5px;
            box-shadow: 0 0 15px rgba(0, 0, 0, 0.2);
            z-index: 999;
        }
        .control-panel input[type=radio] {
            margin-right: 5px;
        }
        .control-panel label {
            display: block;
            margin-bottom: 5px;
        }
    </style>
</head>
<body>
<div class="control-panel">
    <strong>Select Division:</strong><br>
    {% for division in this.divisions %}
    <label>
        <input type="radio" name="division" value="{{ division }}" onchange="filterMarkers('{{ division }}')"> {{ division }}
    </label>
    {% endfor %}
</div>
<script>
function filterMarkers(division) {
    var layers = document.getElementsByClassName('leaflet-control-layers-selector');
    for (var i = 0; i < layers.length; i++) {
        if (layers[i].nextElementSibling.innerText === division) {
            layers[i].click();
        }
    }
}
</script>
</body>
</html>
{% endmacro %}
"""

macro = MacroElement()
macro._template = Template(template)
macro.divisions = df['Division'].unique().tolist()
mymap.get_root().add_child(macro)

# Save the map to an HTML file
mymap.save(r'C:\\Users\\arslan.arif\\PycharmProjects\\pythonProject2\\Weather\\Sites.html')

print("Map has been created and saved as Sites.html")
