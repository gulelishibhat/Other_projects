
#set the home directory is the R_Data_learn as folder and titanic subfolder

#titanic <- read_csv("~/Desktop/R_Data_learn/titanic.csv"); a way to set is go to session and change the directory 
# go to import dataset and just add the link

#library(readr)
#View(titanic); if you click it on the Data it 

#summary(titanic) ; give the mean,median and quartile and all small information.

#how to merge the two csv da
#?data frame; for help
#rep ; for help
#test[1,4]; it;s checking the element of the 1st row and 4th column of the data
# the code below add the new column name survived and new data set 
test.survived <-data.frame(Survived = rep("None",nrow(test)),test[,])
# take the train and append to the test.survived by one by one
data.combined <- rbind(train,test.survived)
#to see the struture of our data
str(data.combined)

#attribute factor is the way of encoding the charcter data into the numeric data type.
# What is the use of dollar $, not money it's the way to go to the special colum of this data
data.combined$Survived <- as.factor(data.combined$Survived)
data.combined$Pclass <- as.factor(data.combined$Pclass)

#table is the attribute  it gives the summary in form of table

table(data.combined$Survived)


#Ditribution across classes
table(data.combined$Pclass)

#Create the hypothesis,upper class passenger or rich folks are more likely to get survived

train$Pclass <- as.factor(train$Pclass)
# the way to plot of histogram of number of of three class passeger category surviving
ggplot(train,aes(x=Pclass,fill = factor(Survived))) +
  geom_histogram(width = 0.5,stat = "count") +
  xlab("Pclass") +
  ylab("Total Count") +
  labs(fill = "Survived")

#gives the general sense of data at first and second.
head(as.character(train$Name))

#is there any name repeated??
length(unique(as.character(data.combined$Name)))
#? length function give the length
# we found some data repeated in name = 2,
# first get the duplicate names and store them as a vector
dup.names <- as.character(data.combined[which(duplicated(as.character(data.combined$Name))),"Name"])

#check in the record if the combined data set is just repeated or is unique
#see the record of the dup.names from record
data.combined[which(data.combined$Name %in% dup.names),]

#what to do with Miss, Mrs??
library(stringr)
# Any correction with other variables (e.g , sibsp)
misses <- data.combined[which(str_detect(data.combined$Name,"Miss.")),]
misses[1:5,]

mrs <- data.combined[which(str_detect(data.combined$Name,"Mrs.")),]
mrs[1:10,]


males <- data.combined[which(train$Sex == "male"),]
males[1:5,]


#create the utility function;
extractTitle <- function(Name) {
  Name <- as.character(Name)
  
  if (length(grep("Miss.",Name))>0) {
    return("Miss.")
  } else if (length(grep("Master.",Name))>0) {
    return(("Master."))
  } else if (length(grep("Mrs.", Name))>0) {
    return("Mrs.")
  } else if (length(grep("Mr", Name))>0) {
    return("Mr.")
  } else {
    return("Other")
  }
}
titles <- NULL
for ( i in 1:nrow(data.combined)) {
  titles <- c(titles,extractTitle(data.combined[i,"Name"]))
}
data.combined$title <- as.factor(titles)
#histogram plot of the 
ggplot(data.combined[1:891,], aes(x = title, fill = Survived)) +
    geom_bar(binwith = 0.5, count = stat) +
    facet_wrap(~Pclass)+
    ggtitle("Pclass") +
    xlab("Title") +
    ylab("Total Count") +
    labs(fill = "Survived")

