*This is the rADAr group repository for the project in Applied Data Analysis 2019/2020* \
Acquati Francesco \
Del Sole Claudio \
Macchi Gabriele \
Vicentini Marco

# Title
Climate Change and Global Inequalities: in-depth analysis of FAO database.

# Abstract
Wealth inequality, global warming and natural resources exploitation are some of the most discussed issues of the last decades. In our project we want to assess the influence that agriculture and livestock farming have on these different topics and how these problems could be solved. \
The effect of agriculture will be evaluated by measuring the produced carbon dioxide, the use of fertilizers, whether resources are equally distributed on the production chain and eventually how these affect the availability of natural resources. Both the influence of single products and single countries on these matters will be assessed. This will provide us insights on which nations play a key role in accumulating the agriculture-originated wealth of third countries.

# Research questions
In this project we will try to provide answers to these questions and detect the causes:
- Are the resources produced by agriculture equally distributed within local population, or does the country show strong bias in favour of the richests?
- What are the differences among different products in terms of carbon footprint and relevance for global emissions?
- What are the differences among nations? Is there any similar pattern in the poor and rich nations, as for production composition?
- Which are the most important nations as for international trade of agriculture products? Which import and export more?

# Dataset
We use part of the many datasets provided by FAOSTAT. They consist on time-series and cross-sectional data about worldwide food production and agriculture-related topics: trade and food balance, emissions, agri-environmental indicators, land use. \
Datasets are available for download on Kaggle or directly on [FAO website](http://www.fao.org/faostat/en/#data), are provided in csv format and apper to be already well formatted: grouping, selecting and other basic operations should be straightforward. Morover, since the amount of data is conveniently split in different files, which individually do not usually exceed 200-300 MB, the project should be manageable without the support of a remote cluster. \
Accessory data about demographic or economic aspects have been retrieved from main international institutions websites, for example:
- [United Nations](http://data.un.org/Explorer.aspx);
- [World Bank](https://data.worldbank.org/);
- [World Inequality Database](https://wid.world/data/)

# Organization of the Github repository
The repository contains the following notebooks, in which our analysis is carried out:
* DataCleaning.ipynb: all raw data from different sources are cleaned, and then saved in pickle format in the /pickle folder.
* GrangerCausality.ipynb: analysis on correlation / causality between global CO2 emissions and temperature changes on a global level, using Granger Causality test.
* GlobalInequality.ipynb: clustering of world countries according to their income distribution patterns in the last 50 years.
* TradeNetwork.ipynb: network analysis of international trades of agricultural products and analysis of the role major countries play in redistributing agricultural-originated resources.
* Products.ipynb: analysis of carbon footprint for different categories of products and assessment of their impact on global CO2 emissions.

# Website / Data Story
The project website, containing our Data Story and some amazing insights is available here! 
[Climate Change and Global Inequalities: in-depth analysis of FAO database.](https://gabbom.github.io/github-page/)
