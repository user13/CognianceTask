# Cogniace task for QA intern position 
_Created by Konstantin Zimenkov_

**Environment:** [Eclipse Luna][1]

**Server:** [http://qainterview.cogniance.com/candidates][2] 

**API Documentation:**

Server allowed methods: 

**GET**, ```http://qainterview.cogniance.com/candidates/```, gives a list of all candidates.  

**GET**, ```http://qainterview.cogniance.com/candidates/<cand_id>```, shows a 
candidate with ```id=<cand_id>```. 

**POST**, ```http://qainterview.cogniance.com/candidates/```, adds a new candidate. 

**DELETE**, ```http://qainterview.cogniance.com/candidates/<cand_id>```, deletes a 
candidate with ```id=<cand_id>```. 
***

For **running** scripts you need:

- open ```Command line```

- move to folder with scripts

- run comand: ```python name_file.py``` or ```python name_file.py -b```

***

My project contain next files:

**1.** ```ServerApi.py```

This file contain methods that implement current API.

**2.** ```Test.py```

Contain tests methods.
First methods check the correctness work on way of the of comparing status_code with the most familiar codes (200, 201 and [other][3]).
Three last tests(test_checkDelete, test_checkShowById, test_chekAdd) verefy  that methods working as expected.

_**Note:**_ Running 19 tests:

- 18 successfully,

- one failed. Method ```GET/<cand_id>``` do not work as expected. If exist record with this ```<cand_id>``` response show us record with the smallest ```<cand_id>``` in all list or first record in this list.

**3.** ```Datamining.py```

This script calculates % of successful requests per hour from file ```dataminung.log``` and store answer in file ```result``` in next format: 
Hour: ```#```. Count of all request: ```#```. Count of success request: ```#```. Result = ```#```%


  [1]: https://eclipse.org/home/index.php
  [2]: http://qainterview.cogniance.com/candidates
  [3]: http://en.wikipedia.org/wiki/List_of_HTTP_status_codes