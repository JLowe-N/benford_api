# Problem Statement

## Challenge 1

 Benford's Law. In 1938, Frank Benford published a paper showing the distribution of the leading digit in many disparate sources of data. In all these sets of data, the number 1 was the leading digit about 30% of the time. Benford’s law has been found to apply to population numbers, death rates, lengths of rivers, mathematical distributions given by some power law, and physical constants like atomic weights and specific heats.

Create a python-based web application (use of tornado or flask is fine) that

1) can ingest the attached example file (census_2009b) and any other flat file with a viable target column. Note that other columns in user-submitted files may or may not be the same as the census data file and users are known for submitting files that don't always conform to rigid expectations. How you deal with files that don't conform to the expectations of the application is up to you, but should be reasonable and defensible.

2) validates Benford’s assertion based on the '7_2009' column in the supplied file

3) Outputs back to the user a graph of the observed distribution of numbers with an overlay of the expected distribution of numbers. The output should also inform the user of whether the observed data matches the expected data distribution.

Stretch challenge: The delivered package should contain a docker file that allows us to docker run the application and test the functionality directly.


## Challenge 2
Widgets Create a basic system description and document a normalized schema from the attached widgets (widgets.tsv) text file.  Include 1) what you think this system would do 2) what you feel would be a reasonable database structure for the data and a reasonable architecture for the system 3) any questions or concerns you have regarding this dataset/system that might need to be answered before establishing an ideal database/solution for such a system. It's a very open-ended problem.

## Challenge 3: Python Stack Trace Interpretation

See the "Python Stack Traces" attachment which lists several python stack traces. Your task is to examine the stack traces and provide a brief response for each one that summarizes what the problem or likely problem is, and the first line of code you would jump to in your code editor given the trace.