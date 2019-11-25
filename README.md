*This is the rADAr group repository for the project in Applied Data Analysis 2019/2020* \
Acquati Francesco \
Del Sole Claudio \
Macchi Gabriele \
Vicentini Marco

# Title
Climate Change and Global Inequalities: in-depth analysis of FAO database.

# Abstract
Wealth inequality, global warming and natural resources exploitation are some of the most discussed issues of the last decades. In our project we want to assess the influence that agriculture and livestock farming have on these different topics and how these problems could be solved. \
The effect of agriculture will be evaluated by measuring the produced carbon dioxide, the use of pesticides, whether resources are equally distributed on the production chain and eventually how these affect the availability of natural resources. Both the influence of single products and single countries on these matters will be assessed. This will provide us insights on what nations play a key role in accumulating the agriculture-originated wealth of third countries. Hence, we will evaluate nations reciprocal influence. We will also try to comprehend how all these factors can be correlated to the world hunger and how the UN could try to alleviate the issue.

# Research questions
In the following, we will try to provide answers to these questions and detect the causes:
- Are the resources produced by agriculture equally distributed among the workers or is there a strong bias in favour of companies?
- Based on the CO2 emission and the use of pesticides, what is the environmental impact of agriculture on the producing countries and on the importing countries?
- What are the consequences of the agriculture industry on the availability of natural and energetic resources?
- What are the differences among nations and products? Is there any similar pattern in the poor and rich nations?
- Once all these questions have been answered, could any of these issues be a possible concurrent cause for world hunger? How could these be possibly solved?

# Dataset
We plan to use at least part of the many datasets provided by FAOSTAT. They consist on time-series and cross-sectional data about worldwide food production and agriculture-related topics: trade and food balance, emissions, agri-environmental indicators, land use. \
Datasets are available for download on Kaggle or directly on [FAO website](http://www.fao.org/faostat/en/#data), are provided in csv format and apper to be already well formatted: grouping, selecting and other basic operations should be straightforward. Morover, since the amount of data is conveniently split in different files, which individually do not usually exceed 200-300 MB, the project should be manageable without the support of a remote cluster. \
Accessory data about demographic or economic aspects which may turn out to be useful during project development could be easily retrieved from main international institutions websites, for example:
- [United Nations](http://data.un.org/Explorer.aspx);
- [World Bank](https://data.worldbank.org/).

# A list of internal milestones up until project milestone 2
- Setup the project: November 4

    According to TA's answers, discuss the feasibility of the project and possibile changes.
    
    Define the precise targets of the project: what do we want as a final result?

    Find out how to clean and divide the data, assigning tasks to each member of the group.

    Discuss a way to put the results together.

- Let's start working! : November 11

    Start working on the project in parallel.

    Keep updating the group on individual results and try to merge them.

- Finish Processing & Analyzing: November 18

    Finish all the divided tasks and start merging all the work.
    
    Discuss the results and keep working on the project.

- Finalization for milestone 2: November 25

    Clean and well explain the code.
    
    Start writing the report.
    
    Any other business...
    
# Questions for TAs
- Is it a good and interesting idea?
- What should we change or improve?
- Is the aim of this project too complex or not feasible?
- The environmental impact could be also correlated to other agents that we are not considering: how to handle this problem?

# Milestone 2 Updates

## Task delivery
Our data is analyzed in the notebook `Milestone_2.ipynb`.

## Description
After a first analysis of our data we now have a more complete understanding of what we have and how it could be further examined. While some obvious assumption can be already confirmed, we now have new clues we will need to study:
- From FAO data we have very detailed information about livestock and harvest production; we initially evaluated the data considering only the total production.
- Concerning the pollution, data was considered only in terms of equivalent CO2 produced and in the use of pesticides. Since FAO specifically attributes the CO2 prodution to different agriculture tasks, we were able to distinguish the CO2 produced wheter it came from livestock farming or harvesting.
- As we can deduce from our worldmaps, the countries that produce and pollute the most are generally always the same: China, USA, India, Brazil, Russia, Nigeria, Mexico, South Africa etc. These are also some of the largest in the world in terms of area and population: it will be interesting to analyze how the population, its density and the land area (either in terms of total area and harvestable area) impact on the production and pollution.
- Concerning the fertilizers dataset, we did not have a unique dataset since FAO changed the way of collecting data in 2002. However, for this year only, we had data stored either in the old and the new manner. This allowed us to make some analyses in order to obtain a consistent and uniform dataset. From 2002 we also have a useful index that expresses the use of fertilizers per area harvested. It will be interesting to evaluate how its correlation with the production per area harvested varies among countries.
- Considering the international trade, we found out that some of the top countries as for import and export are not among the ones that produce the most.
- We also found out that countries that have the highest percentages of area dedicated to agriculture are not the ones that produce the most: this is obviously due to the fact that they are not the largest countries in terms of area. However, it would be interesting to study the relations between the area dedicated to agriculture (subdivided in different categories: cropland, meadows area, arable area) and the total crop and livestock production.
- The data we collected about the use of natural resources for agriculture (water, energy) and the soil quality, may be used to assess the impact of production trends in time on the local environment.
- The main problem we ran into when using the world maps was the fact that some countries changed their borders over time and some did not initially exist. This is the case of USSR that existed only until 1991, when it then splitted into many different countries.

## Future tasks
We created an interactive way to obtain time series for each country so that we are now able to quickly analyze data from selected countries once at a time and compare them. This will provide us an easy way to detect presence of unexpected behaviours in specific countries. We will now focus on the top polluting and producting countries and analyze how their behaviours changed over the last decades, following the hints we provided in this task's description.
