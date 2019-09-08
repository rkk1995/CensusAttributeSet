# Census Data Attribute Set Analysis

### [Data Set](https://s3.amazonaws.com/istreet-questions-us-east-1/443605/census.csv)
#### First 5 entries. ~32000 total
![test](http://puu.sh/EeDZd/350b3ccd7d.png)

This repository contains a tool I made that finds patterns that help make important data-driven decisions. For example out of the first 10 lines:
* There are 7 people with (_capital-gain=None,capital-loss=None_)
* There are 5 people with (_native-country=United-States,capital-gain=None,capital-loss=None_)
* There are 5 people with (_native-country=United-States,capital-gain=None_)
* There are 8 people with (_native-country=United-States,capital-loss=None_)

The support of the set of attributes is defined as the ratio of "total number of records with the given attributes" to "total number of records in the dataset." For example:
* The support of (_capital-gain=None,capital-loss=None_) is 7/10 = .7
* The support of (_native-country=United-States,capital-gain=None,capital-loss=None_) is 5/10 = .5
* The support of (_native-country=United-States,capital-gain=None_) is 5/10 = .5
* The support of (_native-country=United-States,capital-loss=None_) is 8/10 = .8

### Function
Finds all the unique attribute sets of the given length that have the support greater than or equal to the given support threshold value.





  #### parameters
  _numberofAttributes_: an integer
  
  _supportThreshold_: a float
  
  #### constraints
  1<= _numberofAttributes_ <= # of features
  
  0<= _supportThreshold_ <= 1.0

### Sample Case

#### Sample Input

```python
4
0.6
```
#### Sample Output
```
native-country=United-States,race=White,capital-gain=None,capital-loss=None
native-country=United-States,income=Small,capital-gain=None,capital-loss=None
```


