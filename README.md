<h1>Housing Sales Prices & Venues Data Analysis of Baton Rouge, LA</h1>
<h2>Introduction/Business Problem</h2>
<h3>General Description & Discussion of the Background</h3>
                <p>Baton Rouge is the capital city of Louisiana. There are 220,236 people living in Baton Rouge alone,
                    making it the second largest city in Louisiana behind New Orleans.
                    There are over 800,000 people living in the Baton Rouge metropolitan area, and the population has
                    grown 3.4% within the past 10 years.
                    I will be focusing on East Baton Rouge Parish, the most populated parish in the Baton Rouge
                    Metropolitan area. **</p>
                <p>It is home to Louisiana State University (LSU), one of the top-rated universities in Louisiana. LSU
                    is very cheap for both in and out of state students combined with having a high acceptance rate
                    means
                    there are always new students moving into Baton Rouge. Freshman are required to live on campus their
                    first year.
                    It is also the 9th largest port in the United States. Workers come and go from the Mississippi River
                    with goods to ship and hungry bellies every day. </p>
                <p>All these residents and workers need a place to eat. Students get tired of dining halls and don't
                    have kitchens in their dorms.
                    Shipping workers are excited to have a real meal after coming from overseas. Regular working-class
                    adults sometimes forget or are too lazy to cook for themselves.
                    Louisiana has a very diverse food culture and almost all styles of food have a place in Baton
                    Rouge. </p>
<h3>Target Audience</h3>
                <p> Restaurants are a great investment, if planned properly. Unfortunately, almost half of all
                    restaurants fail during the first year of opening. My target audience would be anyone who is looking
                    to start in the
                    restaurant business within Baton Rouge area. There are many factors to consider such as location,
                    service style, and the actual food being sold. </p>
                </p>It is essential to understand the variety of restaurants in each neighborhood. Identifying a market
                gap within a specific neighborhood could lead to that restaurant being
                successful. Versus opening a restaurant in a neighborhood that doesn’t need your food and failing. </p>
                <p class="text-muted">**For those unfamiliar with Louisiana, a parish is akin to a county in other
                    states.</p>
<h3>Data</h3>
                <p>Restaurant location is a complex issue in order to answer this I will use Zillow <span><a
                        href="https://www.zillow.com/baton-rouge-la/home-values/">(1)</a></span>, a popular house
                    purchasing website, data to get housing information for demographics of each neighborhood.</p>
                <p>Additionally, I will use the foursquare API <span><a href="https://foursquare.com/">(2)</a></span> to
                    get a better understanding of the competition within each area by looking at the types of
                    restaurants that are available in each neighborhood to see which is common and which is popular.</p>
                <p>Geolocation<a href="https://opendata.arcgis.com/datasets/7c5e82ef83834de2ad2478efc86744ae_0.geojson">(3)</a>
                    data was utilized getting the neighborhood latitude and longitude coordinates for Baton Rouge. </p>
                    
<h3>Results</h3>
<p>IThe most common restaurants in cluster 0 are primarily American Restaurants and burger joints. These are located in the Northern most neighborhoods and the southern half of Baton Rouge. This is located in the area where the average housing index is the highest at $218,431. Most common Restaurants in cluster 1 are "Food." This means that they are not typical restaurants. These are places that serve food, but aren't restaurants like a food bank. This is located in the area where the average housing index is the lowest at $77,200. The last cluster's most common restaurants Fast Food Take Out locations. This is located in the area where the average housing index is in the middle at $92,246.</p>
<p>Addtionally I sorted and segmented the top most popular venues of each neighbor. There I found that within cluster 0 the most common restaurants in this cluster are Fast Food Take Out locations. This is located in the area where the average housing index is in the middle at $92,246. Within cluster 1 the most common restaurants are Fast Food Take Out locations. This is located in the area where the average housing index is in the middle at $92,246. Lastly within cluster 3 the most common restaurants are American Restaurants. This is located in the area where the average housing index is in the middle at $66,175. </p>

<h3>Discussion</h3>
<p>
I used the python folium library to visualize geographic details of Baton Rouge and its neighborhoods. I utilized the Foursquare API to explore the restaurants in each neighborhood and segment them. I designed the limit as 50 venues. I used the section "food" and sorted by popularity. The radius is the maximum distance between the two geolocations converted to meters from each neighborhood based on their given latitude and longitude information. The radius is the maximum distance between the two geolocations converted to meters from each neighborhood based on their given latitude and longitude information. The search resulted in 1514 venues with 57 unique restaurant categories. Each of these results was run through a KMeans clustering algorithm. The best K was determined using the elbow method. 3 clusters was determined to be the best grouping.
 </p>

<h3>Conclusions</h3>
<p>
I think it's important to consider both the most common restaurants in each area and the most popular restaurants in each area. A potential restaurant opener would want to avoid opening in clusters where their restaurant is too common. They would also want to open in a location where their restaurant type is more popular. There is much more work that can be done to analyze this data further such as looking into which specific restaurants are popular or common in each neighborhood.
</p>



<ol>
                        <li><a href="https://opendata.arcgis.com/datasets/7c5e82ef83834de2ad2478efc86744ae_0.geojson">https://opendata.arcgis.com/datasets/7c5e82ef83834de2ad2478efc86744ae_0.geojson</a>
                        </li>
                        <li><a href="https://www.zillow.com/baton-rouge-la/home-values/">https://www.zillow.com/baton-rouge-la/home-values/</a>
                        </li>
                        <li><a href="https://foursquare.com/">https://foursquare.com/</a></li>
</ol>
