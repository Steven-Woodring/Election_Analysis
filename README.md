# Election Analysis with Python
### Utilizing Python to automate the certification of hypothetical election results

## Overview of Election Audit
This analysis is an election audit of hypothetical vote results from a U.S. Congressional District in Colorado. Utilizing Python in Visual Studio Code, I automated the audit process to return a vote summary and an election winner from the raw data. This same script can hopefully be used in the future to certify results from not only other Congressional Districts, but also Senatorial Districts and local elections.

## Election Audit Results
-	There were 369,711 total votes cast in this congressional election
-	There were 38,855 votes cast in Jefferson County, making up 10.5% of the total votes
-	There were 306,055 votes cast in Denver County, making up 82.8% of the total votes
-	There were 24,801 votes cast in Arapahoe County, making up 6.7% of the total votes
-	Denver County had by far the largest number of votes out of the three counties
-	Charles Casper Stockham received 85,213 votes, or 23.0% of the total popular vote
-	Diane DeGette received 272,892 votes, or 73.8% of the total popular vote
-	Raymon Anthony Doane received 11,606 votes, or 3.1% of the total popular vote
-	Diane DeGette handily won the election, receiving 272,892 votes or 73.8% of the total

<img width="276" alt="Screen Shot 2022-01-09 at 8 18 26 PM" src="https://user-images.githubusercontent.com/95303422/148708972-3ae834f9-7b1b-4d06-8356-dbaa0cab1432.png">

## Election Audit Summary
The election commission should absolutely consider using this script – with some modifications – for any future election. As an alternative to certifying elections in Microsoft Excel, this Python program will return results much quicker and without the risk of mistakes. The code will work for any election data file in which each row is a different vote, and the columns contain (1) the region where the vote was taken and (2) the candidate receiving the vote.

The script can be easily modified to fit different winning requirements. For example, in some elections, it is required that the winning candidate must receive at least 50% of the popular vote. In this case, the below line of code would be altered to require instead that (vote_percentage > 50).

<img width="513" alt="Screen Shot 2022-01-09 at 7 39 54 PM" src="https://user-images.githubusercontent.com/95303422/148709030-ff951832-c5b7-485c-beaa-0e3ea93dc0ca.png">

In another scenario, the winning candidate may be determined based on the electoral vote rather than the popular vote. In this case, the regions will have to be further broken down to arrive at a winner for each region, and that candidate would then receive the votes allotted to that region. Luckily, the format of the raw data file will not have to be modified in this situation.
