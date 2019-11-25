# Milestone 2
Acquati Francesco \
Del Sole Claudio \
Macchi Gabriele \
Vicentini Marco

## Data organization
Our data is analyzed in the notebook Milestone_2.ipynb.

## Initial research questions
As stated in the Milestone 1, in our project we try to analyze and answer the following questions:
- Are the resources produced by agriculture equally distributed among the workers or is there a strong bias in favour of companies?
- Based on the CO2 emission and the use of pesticides, what is the environmental impact of agriculture on the producing countries and on the importing countries?
- What are the consequences of the agriculture industry on the availability of natural and energetic resources?
- What are the differences among nations and products? Is there any similar pattern in the poor and rich nations?
- Once all these questions have been answered, could any of these issues be a possible concurrent cause for world hunger? How could these be possibly solved?

## Milestonee 2 descriprition 
After a first analysis of our data we now have a more complete understanging of what we have and how it could be further examined. While some obvious assumption can be already confirmed, we now have new clues we will need to study:
- From FAO data we have very detailed information about livestock and harvest production. We initially evaluated the data considering only the total production.
- Concernging the pollution, data was considered only in terms of equivalent CO2 produced and in the use of pesticides. Since FAO specifically attributes the CO2 prodution to different agriculture tasks, we were able to distinguish the CO2 produced wheter it came from livestock farming or harvesting.
- As we can deduce from our worldmaps the countries that produce and pollute the most are generally always the same: China, USA, Inda, Brazil, Russia, Nigeria, Mexico, South Africa etc. These are also some of the largest in the world in terms of area and in terms of population. It will be interesting to analyze how the population, its density and the land area (either in terms of total area and harvestable area) impact on the production and pollution.
- Concerning the fertilizers dataset, we did not have a unique dataset since FAO changed the way of collecting data in 2002. However, for this year only, we had data stored either in the old and the new manner. This allowed us to make some analyses in order to obtain a consistent and uniform dataset. From 2002 we also have a useful index that expresses the use of fertilizers per area harvested. It will be interesting to evaluate how its correlation with the production per area harvested varies among countries.
- We created an interactive way to obtain time series for each country so that we are now able to quickly analyze data from selected countries once at a time and confront them. This will provide us an easy way to detect presence of unexpected behaviours in specific countries.
- Considering the international trade we found out that they are some of the most exporting and importing countries but, still they are not among the ones that produce the most.
