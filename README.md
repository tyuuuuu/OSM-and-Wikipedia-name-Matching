# OSM-and-Wikipedia-name-Matching

The main function of this python programing is used to match the geo name from OSM (OpenStreetMap is a open source project, all the information can be downloaded) with the name from Wikipedia.

The TaoYu-715311-Thesis.pdf is the report that record all the details and code explanation of this project.

#####################################################################
/OSM_extraction

OSM_process.py is used to extract the OSM entities from raw OSM data

simply run these commands in your python code

import OSM_process
file_list = ["map.osm"]
OSM_process.OSM_extraction(file_list,"map")

extraction_test.py is a test example


download.py is a script example to automatically download the map

#####################################################################
/online_wikientitiy_selection

online_parallel.py is the main method to automatically extract all the wiki entities with coordinates. the command to run this script is 

mpirun -np (number of processors) python online_parallel.py file1 file2 file2

file1 is the file stores all the entities you want to do selection

file2 is the file stores all the entities with coordinates

file3 is the file stores all the entities that can not link to


a example to run can be like this 
mpirun -np 100 python online_parallel.py name10000.txt result.txt wrong.txt


alieas_simple_parser.py is the script to find all the alias of a wiki entity

the command to run this script is 

mpirun -np (number of processors) python online_parallel.py file1 file2

file1 is the input file
format of file is:
50.1058 1.8358 AbbevilleFrance
48.8 11.85 AbensbergGermany
45.464722222222 -98.486388888889 AberdeenSouthDakota

file2 is the stored file

a example to run alieas_simple_parser.py is:
mpirun -np 100 python online_parallel.py result.txt all_name_with_coordinates.txt

All the test data are stored in test file

#####################################################################
/first_two_word_match  (use the first two words from OSM as keywords for inverted index)

inverted_index.py is the script to generate wiki inverted index and it is called in match_parallel.py

a example to run match_parallel.py is:
mpirun -np 100 python match_parallel.py map_result.txt

The data that used in the script is stored in Nectar server, "all_name_with_coordinates_redrict.txt", "all_name_redrict.txt" are two files needed

#####################################################################
/least_frequency_match   (use the two words with least frequency from OSM as keywords for inverted index)

inverted_index_frequency.py is the script to generate wiki inverted index and it is called in match_parallel_frequency.py

a example to run match_parallel_frequency.py is:
mpirun -np 100 python match_parallel_frequency.py map_result.txt

The data that used in the script is stored in Nectar server, "all_name_with_coordinates_redrict.txt", "all_name_redrict.txt" are two files needed

#####################################################################
/infobox_parser

parser_parallel.py is the script used to parse the infobox of wiki.

a example to run parser_parallel.py is:

mpirun -np 100 python parser_parallel.py matched_record.txt

#####################################################################
/tool

some simple code used as tools in this project
