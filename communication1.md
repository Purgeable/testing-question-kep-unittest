Some communication with [Eduard Bagov](https://www.upwork.com/freelancers/~01ce161462df65feaa)
(for further editing).

-------------


```
1. To answer your question in the job description I liked the second example.
In case if some hardcoded phrase is used in a lot of unit tests, that time I'd like to use the second example.
But if hardcoded phrase is used only in one place, I'd like to use that hardcoded value inside the test.
The variable name which stores hardcoded value should also be readable.

2. Test names should tell what is the test intention, it should look like technical description:
[the name of the tested method]_[expected input / tested state]_[expected behavior]

Please check http://stackoverflow.com/questions/155436/unit-test-naming-best-practices
I suggest to change all tests.

3. https://github.com/epogrebnyak/question-kep-unittest/blob/master/test_csv_data.py#L11-L15
Too few unit tests.
I suggest to add the following tests also:
a) cd.doc_to_lists("2015")
b) cd.doc_to_lists("2015\t")
c) cd.doc_to_lists("2015\n")
d) cd.doc_to_lists("")

4. No tests for csv_data.yield_dicts_from_file()

5. https://github.com/epogrebnyak/question-kep-unittest/blob/master/test_csv_data.py#L90-L94
This test only checks the length. Actually length can be correct, but the result of function can be wrong.
I suggest to add the content checking also.

6. Some big file tab.csv was created for testing purpoces. In case if class functions increase or new tests added, does it mean that new big testing files should be created? No!
You can use mocking to stub the reading process and simulate some state.
http://stackoverflow.com/questions/1289894/how-do-i-mock-an-open-used-in-a-with-statement-using-the-mock-framework-in-pyth

7. https://github.com/epogrebnyak/question-kep-unittest/blob/master/parsing_definitions.py#L87-L96
There are 3 places where exception can take place.
Some tests should be added to check if exception takes place when the function is in some predefined state. assertRaises() will check that expected exception happened.

Seems that's all what I noticed.
Please don't hesitate to ask me questions.


Let's discuss #1
I prefer to use hardcoded values inside each test
because these hardcoded values will be only in one test
in case if you use some values in different tests, that time I liked the class you created Match_CSV_Content
I didn't like YAML_2, CONTENT_2
setUp() method is being called first. Usually some initial settings are set in setUp() (edited)
It's just more constants, different string composition... why not include YAML_2, CONTENT_2 in test?
or you mean it shoudl be different test method or different test class for each set of constants?
honestly there is no big difference, you can use in both ways. but using class for me is better than global variables. but it is really no big issue.

you can include yaml in test if that yaml is used only in that test. in case if it is called from different places, you should make it either global or in class.
Evgeny Pogrebnyak Wednesday, April 26, 2017 11:11 AM
why not include YAML_2, CONTENT_2 in test?
Yes!!! For tests it's normal. you can use long names, thanks to do that you can understand which requirement is being tested at the moment.


Evgeny Pogrebnyak Wednesday, April 26, 2017 10:28 AM
Also "The variable name which stores hardcoded value should also be readable." - you mean longer and more descriptive name?
I agree. I also liked that.

Evgeny Pogrebnyak Wednesday, April 26, 2017 10:56 AM
I was wondering if making a class like Match_CSV_Content() is a good practice in unittest, becuase I just made this out of the blue.

#6 - Ok, you should have at least one test which checks if production csv is loaded
That time name the test properly because if other developer reads, he will not understand what you meant.
Using naming convention [the name of the tested method]_[expected input / tested state]_[expected behavior]
instead of this test_reading_default_csv() you can use test_CSV_Reader__full_file_load___all_rows_length_ok


Any use in suites in your opinion?
Something like below:
However I would personally add a TestLoader in order to handle the multiple Test Classes better
if __name__ == '__main__':
#test Classes List
testClasses = [ Test_StringAsYAML, Test_ParsingDefintion, Test_Get_Definitions ]

#create a test loader object
tloader = unittest.TestLoader()

#creation of an empty list
TestSuites_list = []
#for loop to create a new complete Test Suite which contains all the individuals Test Classes - Suites
for testClass in testClasses:
currentSuite = tloader.loadTestsFromTestCase(testClass)
TestSuites_list.append(currentSuite)

#Creation of the combined Final Complete Suite
final_suite = unittest.TestSuite(TestSuites_list)

# Creation of the Test runner object which prints results on standard error.
test_runner = unittest.TextTestRunner(verbosity=2)

#execute the suite
test_Results = test_runner.run(final_suite)


Eduard Bagrov
For unit tests using test suites is not so important. For each file you can create a test suite and add there all tests.
For integration tests you will be interested to check different tests together. There you have to create different suites. But for your task just add all tests together in one suite and that's all.
As all tests are atomar, they don't depend on each other, you need to run all tests one by one in one suite. (edited)
The code you pasted is good


For me important part is the naming convention and learn to use mocking
others are minor points


Evgeny Pogrebnyak
Mocking is very new to me, but it is more useful to more complex objects, rather than strings, probably
Do you ever write a test first, then the xode to pass it?
Code


yes, it is used for complex objects, like if you want to connect to the database, to do some query. If you do that inside each test case, it will be very difficult. Instead you use mocking, you say that I got some string, and test other stuff.
But for your task you can also use mocking, you don't need always open file, read data from the file. Just use mocking. (edited)
At my work place management always say about writing test, then code. I don't like that :smile:
In that way you will have to touch tests twice
Because the developer will change it's mind and change number of arguments
But your tests supposed to use less number of arguments



Sometimes you get to read that developpers should agree on function/module/class interface and not really change that
while writing the function code 
yes, we should agree. but as we do always very quickly, because clients or management need it very fast, you don't have enought time to think about number of arguments, etc...
that's why I don't like tests, then code. I prefer code, then I'll test very carefully

```
