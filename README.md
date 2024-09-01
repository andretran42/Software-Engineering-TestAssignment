# Software Engineering Skills Test
Generates annotated images of leaf node elements given an XML file and a corresponding PNG image

## Description
This project was assigned as part of the CSCI 435 skills assesment. 

## To run
Ensure that Pillow is installed:
```
pip install Pillow
```
Place corresponding xml and png images into separate "Data" folder and "Images" folder respectively.
On Windows, run with
```
py highlight.py
```
And on Mac / Linux, run using
```
python3 highlight.py
```

## Design
I decided to split up the data and images into two separate folder for more thorough organization.
The basic flow of the program is to 
1. gather the input xml files
2. TRY search for corresponding PNG
3. TRY parse XML file
4. gather the corner bounding boxes for each leaf node
5. Output image

Issues:
One given XML file seemed to be invalid XML, and I chose to use try/except blocks rather than try to parse the invalid file. 
