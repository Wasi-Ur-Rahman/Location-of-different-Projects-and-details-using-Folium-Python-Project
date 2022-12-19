# import folium library
import folium
# create a map object with initial zoom and map center
mapObj = folium.Map(location=[23.729211164246585, 90.40874895549243], zoom_start=5)

location1 = [23.729211164246585, 90.40874895549243]
popup1 = "<strong>project_name:</strong><br>JICA Support Program 3 for Strengthening Mathematics and Science Education in Primary Education Project</br><br><strong>Category</strong>: Education</br><br><strong>Affiliated Agency</strong>: Ministry of Primary and Mass Education, Directorate of Primary Education</br><br>>strong>Project Start Time</strong>: 4/1/2019</br><br><strong>Project end time</strong>: 6/30/2023</br><br><strong>Total Budget</strong>: JPY 380M</br><br><strong>completion_percentage</strong>: 77.36%</br>"

folium.Marker(location = location1,popup = popup1).add_to(mapObj)



# inject html into the map html
mapObj.get_root().html.add_child(folium.Element("""
<div style="position: fixed; 
     top: 50px; left: 70px; width: 150px; height: 70px; 
     background-color:orange; border:2px solid grey;z-index: 900;">
    <h5>Hello World!!!</h5>
    <button>Test Button</button>
</div>
"""))

mapObj.save('output.html')
