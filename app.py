from flask import Flask, render_template, request
import pandas as pd
import pickle
import numpy as np

popularity_df = pickle.load(open('popularity.pkl','rb'))
pt = pickle.load(open('pt.pkl','rb'))
books = pickle.load(open('books.pkl','rb'))
similarity_score = pickle.load(open('similarity_score.pkl','rb'))
book_list = pickle.load(open('book_list.pkl','rb'))


app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html',
                           book_name=list(popularity_df['Book-Title'].values),
                           author=list(popularity_df['Book-Author'].values),
                           image=list(popularity_df['Image-URL-M'].values),
                           votes=list(popularity_df['num_ratings'].values),
                           rating=np.round(list(popularity_df['avg_ratings'].values), 2)
                           )

@app.route('/recommend')
def decommend_ui():
    return render_template('recommend.html')

@app.route('/recommend_books', methods=['POST'])
def recommend():

    user_input = request.form.get('user_input')
    indi = np.where(pt.index == user_input)[0][0]
    print('\n',indi)
    print('\n')
    # distances = similarity_score[index]
    similar_items = sorted(list(enumerate(similarity_score[indi])), key=lambda x: x[1], reverse=True)[1:13]

    data = []
    for i in similar_items:
        item = []
        temp_df = books[books['Book-Title'] == pt.index[i[0]]]
        item.extend(list(temp_df.drop_duplicates('Book-Title')['Book-Title'].values))
        item.extend(list(temp_df.drop_duplicates('Book-Title')['Book-Author'].values))
        item.extend(list(temp_df.drop_duplicates('Book-Title')['Image-URL-M'].values))

        data.append(item)

    print(data)
    return render_template('recommend.html', data = data, name = list(book_list['Book-Title'].values))

# @app.route('/list', methods=["POST"])
# def list():
#     return render_template('recommend.html', name = list(book_list['Book-Title'].values))


if __name__ == '__main__':
    app.run(debug=True)
