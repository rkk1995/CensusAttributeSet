# Census Data Attribute Set Analysis

## [Data Set](https://s3.amazonaws.com/istreet-questions-us-east-1/443605/census.csv)
### First 5 entries. ~32000 total
![test](http://puu.sh/EeDZd/350b3ccd7d.png)

This repository contains a tool I made that takes 2 inputs:
  
  ##### parameters
  _numberofAttributes_: an integer
  _supportThreshold_: a float
  
  ##### constraints
  1<= _numberofAttributes_ <= # of features
  0<= _supportThreshold_ <= 1.0

<details><summary>Sample Case</summary>
<p>

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
</p>
</details>
