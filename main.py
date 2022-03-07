from flask import Flask, render_template, redirect, url_for
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from forms import AddProductForm, SearchProductForm


app = Flask(__name__)
app.secret_key = 'tjrX2oWRCM3Tvarz38zlZM7Uc10'
Bootstrap(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///products-collection.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class Product(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(250), nullable=False)
    price = db.Column(db.Float(), nullable=False)

    def __repr__(self):
        return '<Product %r>' % self.name


db.create_all()


@app.route("/")
def home():
    return render_template("index.html")


@app.route('/add', methods=['GET', 'POST'])
def add_product():
    form = AddProductForm()
    if form.validate_on_submit():
        new_product = Product(
            name=form.product_name.data.lower(),
            price=form.product_price.data
        )
        db.session.add(new_product)
        db.session.commit()
        return redirect(url_for('search_product'))
    else:
        return render_template('add.html', form=form)


@app.route('/search', methods=['GET', 'POST'])
def search_product():
    form = SearchProductForm()
    if form.validate_on_submit():
        search_name = form.product_name.data.lower()
        product = db.session.query(Product).filter(Product.name == search_name).first()
        return render_template('search.html', product=product, form_filled=True, form=form)
    else:
        return render_template('search.html', products=[], form_filled=False, form=form)


if __name__ == '__main__':
    app.run(debug=True)
