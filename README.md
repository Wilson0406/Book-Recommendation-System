# Book-Recommendation-System

### Check Out the Book Recommendation System Here:
<a href="https://books-mate.herokuapp.com/">BooksMate</a>
## Description:
<p>A Book Recommendation System which recommends the users a selection of books based on their interests.
It also has a separate page for the list of all books.</p>
<p>Data used for this project was taken from <a href="https://www.kaggle.com/datasets/arashnic/book-recommendation-dataset">here</a>.</p>

### 1. Data Cleaning and Pre-Processing
The dataset consists of three tables; Books, Users, and Ratings. Data from all three tables are cleaned and preprocessed separately.<br><br>

### 2. Algorithms Implemented:
#### 2.1 Popularity Based Recommendation :

* ##### Popular in the Whole Collection <br>
We have sorted the dataset according to the total ratings each of the books have received in non-increasing order and then recommended top 50 books.

#### 2.2 Content Based Recommendation
This system recommends books by calculating similarities in Book Titles. For this, TF-IDF feature vectors were created for unigrams and bigrams of Book-Titles; only those books' data has been considered which are having at least 50 ratings.

### 3. Libraries Used:

* ipython-notebook - Python Text Editor
* sklearn - Machine learning library
* numpy, scipy- number python library
* pandas - data handling library

### 4. Frontend

* HTML, CSS & Javascript was used for the frontend of the application.


[![Made with Jupyter](https://img.shields.io/badge/Made%20with-Jupyter-orange?style=for-the-badge&logo=Jupyter)](https://jupyter.org/try)
[![Made with Bootstrap](https://img.shields.io/badge/UI%20build%20with-Bootstrap-purple?style=for-the-badge&logo=Bootstrap)](https://getbootstrap.com/)
[![Made with Flask](https://img.shields.io/badge/WebApp%20made%20with-Flask-yellow?style=for-the-badge&logo=flask)](https://flask.palletsprojects.com/en/2.1.x/)

<br>

Cooked with <span style="color: #e25555;">&#9829;</span> by [WilsonVD](https://github.com/Wilson0406)
