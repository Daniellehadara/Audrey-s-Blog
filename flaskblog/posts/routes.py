from flask import (render_template, url_for, flash,
                   redirect, request, abort, Blueprint)
from flask_login import current_user, login_required
from flaskblog import db
from flaskblog.models import Post
from flaskblog.posts.forms import PostForm
import os


posts = Blueprint('posts', __name__)

@posts.route("/posts/new", methods=['GET', 'POST'])
@login_required
def new_post():
    form = PostForm()
    if form.validate_on_submit():
        post = Post(title=form.title.data, content=form.content.data, author=current_user)
        db.session.add(post)
        db.session.commit()
        file = form.file.data
        base_dir = 'C:\\Users\\cohendh\\Documents\\GitHub\\MyBlog\\flaskblog\\static\\pics\\'
        if file is None:
            file_name = 'default_worrier.jpg'
            file.save(base_dir + file_name)
        else:
            file_name = post.title + '.jpg'
            f = open(base_dir + file_name, "a")
            file.save(base_dir + file_name)
        flash('Your posts has been created!', 'success')
        return redirect(url_for('main.home'))
    return render_template('create_post.html', title='New Post',
                           form=form, legend='New Post')


@posts.route("/posts/<int:post_id>")
def post(post_id):
    post = Post.query.get_or_404(post_id)
    return render_template('posts.html', title=post.title, post=post)


@posts.route("/posts/<int:post_id>/update", methods=['GET', 'POST'])
@login_required
def update_post(post_id):
    post = Post.query.get_or_404(post_id)
    if post.author != current_user:
        abort(403)
    form = PostForm()
    if form.validate_on_submit():
        post.title = form.title.data
        post.content = form.content.data
        db.session.commit()
        file = form.file.data
        try:
            file_name = post.title + '.jpg'
            base_dir = 'C:\\Users\\cohendh\\Documents\\GitHub\\MyBlog\\flaskblog\\static\\pics\\'
            f = open(base_dir + file_name, "a")
            file.save(base_dir + file_name)
        except Exception:
            pass
        flash('Your posts has been created!', 'success')
        return redirect(url_for('main.home'))
        return render_template('create_post.html', title='New Post',form=form, legend='New Post')
        flash('Your posts has been updated!', 'success')
        return redirect(url_for('posts.post', post_id=post.id))
    elif request.method == 'GET':
        form.title.data = post.title
        form.content.data = post.content
    return render_template('create_post.html', title='Update Post',
                           form=form, legend='Update Post')


@posts.route("/posts/<int:post_id>/delete", methods=['POST'])
@login_required
def delete_post(post_id):
    post = Post.query.get_or_404(post_id)
    if post.author != current_user:
        abort(403)
    db.session.delete(post)
    db.session.commit()
    flash('Your posts has been deleted!', 'success')
    return redirect(url_for('main.home'))