from flask import Blueprint, jsonify, request
from flask_login import login_required
from app.models import User, Transaction, FriendRequest, db
from app.forms import FriendRequestForm, SignUpForm
from sqlalchemy import or_

user_routes = Blueprint('users', __name__)


@user_routes.route('/')
@login_required
def users():
    users = User.query.all()
    return {'users': [user.to_dict() for user in users]}


@user_routes.route('/<int:id>')
@login_required
def user(id):
    user = User.query.get(id)
    return user.to_dict()


@user_routes.route('/<int:id>', methods=["PUT"])
@login_required
def update_user_balance(id):
    user = User.query.get(id)
    return user.to_dict()


@user_routes.route('/<int:id>/friends')
@login_required
def get_all_friends(id):
    user = User.query.get(id)
    following = {friend.id: friend.to_dict_friends()
                 for friend in user.following}
    followed = {friend.id: friend.to_dict_friends()
                for friend in user.followed}
    friends = { **following, **followed }
    return {'friends': friends}


@user_routes.route('/<int:id>/friends', methods=["POST"])
@login_required
def new_friend(id):
    form = FriendRequestForm()
    form['csrf_token'].data = request.cookies['csrf_token']
    if form.validate_on_submit():
        friend_id = form.data['sender_id']
        user = User.query.get(id)
        new_friend = User.query.get(friend_id)
        user.friend(new_friend)
        db.session.commit()
        return new_friend.to_dict_friends()


@user_routes.route('/<int:id>/friends/transactions')
@login_required
def get_all_transactions(id):
    user = User.query.get(id)
    followed_ids = [friend.id for friend in user.followed]
    following_ids = [friend.id for friend in user.following]
    friendIds = followed_ids + following_ids
    transactions = Transaction.query.filter(or_(Transaction.payee_id == user.id,
        Transaction.payer_id == user.id,
        Transaction.payee_id.in_(friendIds),
        Transaction.payee_id.in_(friendIds),
        ))
    return {'transactions': [transaction.to_dict() for transaction in transactions]}


@user_routes.route('/<int:id>/friend-requests')
@login_required
def get_all_friend_requests(id):
    friend_requests = FriendRequest.query.filter(or_(
        FriendRequest.sender_id == id,
        FriendRequest.recipient_id == id
        ))
    return {'friend_requests': [request.to_dict() for request in friend_requests]}