# import folium library
import folium
# create a map object with initial zoom and map center
mapObj = folium.Map(location=[23.729211164246585, 90.40874895549243], zoom_start=2)

location1 = [23.729211164246585, 90.40874895549243]
popup1 = "<strong>project_name:</strong><br>JICA Support Program 3 for Strengthening Mathematics and Science Education in Primary Education Project</br><br><strong>Category</strong>: Education</br><br><strong>Affiliated Agency</strong>: Ministry of Primary and Mass Education, Directorate of Primary Education</br><br>>strong>Project Start Time</strong>: 4/1/2019</br><br><strong>Project end time</strong>: 6/30/2023</br><br><strong>Total Budget</strong>: JPY 380M</br><br><strong>completion_percentage</strong>: 77.36%</br>"

folium.Marker(location = location1,popup = popup1).add_to(mapObj)

location2 = [23.733211657612223, 90.40993638432778]
popup2 = "<strong>project_name:</strong><br>Project for Capacity Building of Nursing Services Phase 2</br><br><strong>Category</strong>: Health</br><br><strong>Affiliated Agency</strong>: Directorate General of Nursing and Midwifery Services (DGNM), Bangladesh Nursing and Midwifery Council (BNMC)</br><br>>strong>Project Start Time</strong>: 3/26/2022</br><br><strong>Project end time</strong>: 3/25/2026</br><br><strong>Total Budget</strong>: JPY 300M</br><br><strong>completion_percentage</strong>: 22.15%</br>"

folium.Marker(location = location2,popup = popup2).add_to(mapObj)

location3 = [23.728881264793493, 90.40888399782175]
popup3 = "<strong>project_name:</strong><br>The Project for Strengthening Health Systems through Organizing Communities</br><br><strong>Category</strong>: Health</br><br><strong>Affiliated Agency</strong>: Operational Plans (OPs) of the Ministry of Health and Family Welfare/ Sectors-Wide Program Management and Monitoring, Health Economics and Finance, Non-communicable Disease Control (NCDC), Community Based Healthcare (CBHC), Upazila Health Care (UHC), Hospital Services Management (HSM), Lifestyle and Health Education Promotion (L & HEP) </br><br>>strong>Project Start Time</strong>: 6/29/2017</br><br><strong>Project end time</strong>: 7/28/2022</br><br><strong>Total Budget</strong>: JPY 400M</br><br><strong>completion_percentage</strong>: 97.55%</br>"

folium.Marker(location = location3,popup = popup3).add_to(mapObj)

location4 = [23.780215725696586, 90.40895332665768]
popup4 = "<strong>project_name:</strong><br>Safe Motherhood Promotion Project</br><br><strong>Category</strong>: Health</br><br><strong>Affiliated Agency</strong>: Ministry of Health and Family Welfare*2, Directorate of Family Planning, Directorate of Health Services, District Family Planning Office, District Health Services Office, and Upazila Health Complex</br><br>>strong>Project Start Time</strong>: 7/1/2006</br><br><strong>Project end time</strong>: 6/30/2010</br><br><strong>Total Budget</strong>: JPY 350M</br><br><strong>completion_percentage</strong>: 100.00%</br>"

folium.Marker(location = location4,popup = popup4).add_to(mapObj)

location5 = [23.75363622259384, 90.39417243785537]
popup5 = "<strong>project_name:</strong><br>Safe Motherhood Promotion Project phase 2</br><br><strong>Category</strong>: Health</br><br><strong>Affiliated Agency</strong>: Ministry of Health and Family Welfare*2, Directorate of Family Planning, Directorate of Health Services, District Family Planning Office, District Health Services Office, and Upazila Health Complex</br><br>>strong>Project Start Time</strong>: 7/1/2011</br><br><strong>Project end time</strong>: 6/30/2016</br><br><strong>Total Budget</strong>: JPY 420M</br><br><strong>completion_percentage</strong>: 100.00%</br>"

folium.Marker(location = location5,popup = popup5).add_to(mapObj)

location6 = [23.728407931193587, 90.40787482665709]
popup6 = "<strong>project_name:</strong><br>National Integrity Strategy Support Project Phase 2</br><br><strong>Category</strong>: Governance</br><br><strong>Affiliated Agency</strong>: Cabinet Division of the Government of Bangladesh</br><br>>strong>Project Start Time</strong>: 7/1/2011</br><br><strong>Project end time</strong>: 6/30/2016</br><br><strong>Total Budget</strong>: JPY 400M</br><br><strong>completion_percentage</strong>: 100.00%</br>"

folium.Marker(location = location6,popup = popup6).add_to(mapObj)

location7 = [23.7284766533655, 90.40910864263893]
popup7 = "<strong>project_name:</strong><br>Project for Capacity Development of City Corporations (C4C)</br><br><strong>Category</strong>: Governance</br><br><strong>Affiliated Agency</strong>: Local Government Division (LGD), Ministry of Local Government, Rural Development and Cooperatives (MLGRD&C) </br><br>>strong>Project Start Time</strong>: 1/6/2016</br><br><strong>Project end time</strong>: 6/05/2021</br><br><strong>Total Budget</strong>: JPY 410M</br><br><strong>completion_percentage</strong>: 99.50%</br>"

folium.Marker(location = location7,popup = popup7).add_to(mapObj)

location8 = [23.7284766533655, 90.40910864263893]
popup8 = "<strong>project_name:</strong><br>Strengthening Paurashava Governance Project (SPGP)</br><br><strong>Category</strong>: Governance</br><br><strong>Affiliated Agency</strong>: Local Government Division (LGD), Ministry of Local Government, Rural Development and Cooperatives (MLGRD&C)</br><br>>strong>Project Start Time</strong>: 2014-02-15</br><br><strong>Project end time</strong>: 2018-10-16</br><br><strong>Total Budget</strong>: JPY 150M</br><br><strong>completion_percentage</strong>: 100.00%</br>"
folium.Marker(location = location8,popup = popup8).add_to(mapObj)

location9 = [23.7708680271343, 90.38098892695923]
popup9 = "<strong>project_name:</strong><br>Strengthening Public Investment Management System (SPIMS) Project Phase 2</br><br><strong>Category</strong>: Governance</br><br><strong>Affiliated Agency</strong>: Programming Division, Planning Commission, Ministry of Planning</br><br>>strong>Project Start Time</strong>: 2019-09-28</br><br><strong>Project end time</strong>: 2023-09-27</br><br><strong>Total Budget</strong>: JPY 350M</br><br><strong>completion_percentage</strong>: 80.48%</br>"

folium.Marker(location = location9,popup = popup9).add_to(mapObj)

location10 = [23.7284766533655, 90.40910864263893]
popup10 = "<strong>project_name:</strong><br>Upazila Integrated Capacity Development Project (UICDP)</br><br><strong>Category</strong>: Governance</br><br><strong>Affiliated Agency</strong>: Local Government Division (LGD), Ministry of Local Government, Rural Development and Cooperatives (MLGRD&C)</br><br>>strong>Project Start Time</strong>: 2017-09-16</br><br><strong>Project end time</strong>: 2022-12-15</br><br><strong>Total Budget</strong>: JPY 405M</br><br><strong>completion_percentage</strong>: 100.00%</br>"
folium.Marker(location = location10,popup = popup10).add_to(mapObj)




location11 = [23.728917093659554, 90.40956388277749]
popup11 = "<strong>project_name:</strong><br>The Integrated Energy and Power Master Plan Project in Bangladesh</br><br><strong>Category</strong>: Energy and Mining</br><br><strong>Affiliated Agency</strong>: MoPEMR (Ministry of Power, Energy and Mineral Resources)</br><br>>strong>Project Start Time</strong>: 2021-06-22</br><br><strong>Project end time</strong>: 2024-01-31</br><br><strong>Total Budget</strong>: JPY 285M</br><br><strong>completion_percentage</strong>: 58.87%</br>"
folium.Marker(location = location11,popup = popup11).add_to(mapObj)





location12 = [23.728917093659554, 90.40956388277749]
popup12 = "<strong>project_name:</strong><br>The Project for Gas Network System Digitalization and Improvement of Operational Efficiency in Gas Sector in Bangladesh</br><br><strong>Category</strong>: Energy and Mining</br><br><strong>Affiliated Agency</strong>: Energy and Mineral Resources Division (EMRD) Ministry of Power, Energy and Mineral Resources MoPEMR)</br><br>>strong>Project Start Time</strong>: 2020-01-27</br><br><strong>Project end time</strong>: 2022-12-22</br><br><strong>Total Budget</strong>: JPY 180M</br><br><strong>completion_percentage</strong>: 99.43%</br>"
folium.Marker(location = location12,popup = popup12).add_to(mapObj)

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
