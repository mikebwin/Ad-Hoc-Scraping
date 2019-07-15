<H2> To get follower counts for social media

<H5>REQUIREMENTS:

```pip install -r requirements.txt```

- BeautifulSoup4

- Selenium


<H5> SELENIUM INSTALLATION <H5>

- Get the correct driver for Chrome [here](https://selenium-python.readthedocs.io/installation.html#drivers)

- Unzip from download and get the path to the directory containing the exec file. 

- Run the command: `echo export PATH="/YOUR/PATH/HERE:$PATH" >> ~/.bash_profile` (on Mac, for WIN10: go with the GUI)


<H5> RUNNING

```python scraper.py```

- There is a text file called "handles.txt", list all the handle names each on separate lines with no header.

- Will run through the entirety of the list before outputting to a file called "results.csv"

- Scrapes posts, followers, following
