from flask import Blueprint, request, jsonify
from database.models import Expense, db
from utils.auth_middleware import auth_required

expense_bp = Blueprint('expense', __name__)

@expense_bp.route('/expenses', methods=['POST'])
@auth_required
def add_expense():
    data = request.json

    expense = Expense(
        user_id=request.user_id,
        amount=data['amount'],
        category=data['category'],
        description=data.get('description')
    )
    db.session.add(expense)
    db.session.commit()

    return jsonify({"message": "Expense added"})


@expense_bp.route('/expenses', methods=['GET'])
@auth_required
def get_expenses():
    expenses = Expense.query.filter_by(user_id=request.user_id).all()

    result = [{
        "id": e.id,
        "amount": e.amount,
        "category": e.category,
        "description": e.description,
        "date": e.date.strftime("%Y-%m-%d %H:%M:%S")
    } for e in expenses]

    return jsonify(result)


@expense_bp.route('/expenses/<int:id>', methods=['DELETE'])
@auth_required
def delete_expense(id):
    expense = Expense.query.filter_by(id=id, user_id=request.user_id).first()

    if not expense:
        return jsonify({"message": "Expense not found"}), 404

    db.session.delete(expense)
    db.session.commit()

    return jsonify({"message": "Expense deleted"})
