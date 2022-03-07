from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, SubmitField
from wtforms.validators import DataRequired


class AddProductForm(FlaskForm):
    product_name = StringField(label="Product Name: ", validators=[DataRequired()])
    product_price = FloatField(label="Product Price", validators=[DataRequired()])
    btn_done = SubmitField(label="Add")


class SearchProductForm(FlaskForm):
    product_name = StringField(label="Product Name: ", validators=[DataRequired()])
    btn_done = SubmitField(label="Search")
