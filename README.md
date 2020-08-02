<h1>Introduction/Business Problem</h1>

<p>Baton Rouge is the capital city of Louisiana. There are 220,236 people living in Baton Rouge alone, making it the second largest city in Louisiana behind New Orleans.
There are over 800,000 people living in the Baton Rouge metropolitan area, and the population has grown 3.4% within the past 10 years.
I will be focusing on East Baton Rouge Parish, the most populated parish in the Baton Rouge Metropolitan area. **</p>

<p>It is home to Louisiana State University (LSU), one of the top rated universities in Louisiana. LSU is very cheap for both in and out of state students combined
with having a high acceptance rate means there are always new students moving into Baton Rouge. Freshman are required to live on campus their first year.
It is also the 9th largest port in the United States. Workers come and go from the Mississippi River with goods to ship and hungry bellies every day.</p>

<p>All of these residents and workers need a place to eat. Students get tired of dining halls and don't have kitchens in their dorms. Shipping workers are
excited to have a real meal after coming from overseas. Regular working class adults sometimes forget or are too lazy to cook for themselves.
Louisiana has a very diverse food culture and almost all styles of food have a place in Baton Rouge.</p>

<p>Restaurants are a great investment, if planned properly. Unfortunately almost half of all restaurants fail during the first year of opening. 
There are many factors to consider such as location, service style, and the actual food being sold. I hope to be able to provide some answers to
these factors using location data.</p>

<p>**For those unfamiliar with Louisiana, a parish is akin to a county in other states.</p>

<h1>Data</h1>

<p>Restaurant location is a complex issue in order to answer this I will use the US census data  (1) to geta general understanding of the population.
Then I will use the Louisiana Commercial Real Estate Database (2) for rent and pricing data in the correct commercial zones (Commercial, Light Commercial,
and Heavy Commercial) in accordance to Chapter 8 Zoning Laws of East Baton Rouge Parish (3).</p>

<p>OpenBr has a housing dataset (4) that can be used to get an understanding of how much property costs in each area to get an understanding of the
demographics of each neighborhood. I will use Baton Rouge crime data (5) to address any serious concerns about the location of the restaurant.</p>

<p>I will use the foursquare api (6) to get a better understanding of the competition within each area by looking at the types of restaurants that
are available in each neighborhood.</p>

<ol>
  <li> https://www.census.gov/quickfacts/fact/dashboard/batonrougecitylouisiana,LA,US/PST045219</li>
  <li> https://www.lacdb.com/commercial-real-estate/louisiana/baton%20rouge</li>
  <li> https://www.brla.gov/DocumentCenter/View/2270/Chapter-8---Zoning-Districts-PDF</li>
  <li> https://data.brla.gov/Housing-and-Development/Property-Information/re5c-hrw9</li>
  <li> https://www.brla.gov/203/Baton-Rouge-Police-Department</li>
  <li> https://foursquare.com/</li>
</ol>
