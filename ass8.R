install.packages("DataExplorer") 
library(DataExplorer)
choco = read.csv('flavors_of_cacao.csv', header = T, stringsAsFactors = F)
choco
summary(choco)
choco$Cocoa.Percent = as.numeric(gsub('%','',choco$Cocoa.Percent))
summary(choco)
choco$Review.Date = as.character(choco$Review.Date)
summary(choco)
plot_str(choco) # use for displaying Structure of dataset 
plot_missing(choco) # use for analysing number of missing values in dataset
plot_histogram(choco) #  use for continues variables
plot_density(choco) #  use for continues variables
plot_bar(choco) #  use for categorial variables
