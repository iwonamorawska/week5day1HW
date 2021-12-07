from flask import Blueprint
from flask import render_template

blog=Blueprint('blog', __name__, template_folder='blog_templates')
@blog.route('/blog_post')
def blog_1():
    return render_template('blog.html')
