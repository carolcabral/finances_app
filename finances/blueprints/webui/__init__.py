from flask import Blueprint
from .views import index, delete, update, reports, admin, add_expense

bp = Blueprint("webui", __name__, static_folder="static", template_folder="templates")

bp.add_url_rule("/", view_func=index)
bp.add_url_rule("/delete/<int:id>", view_func=delete)
bp.add_url_rule("/update/<int:id>", view_func=update)
bp.add_url_rule("/reports", view_func=reports)
bp.add_url_rule("/admin", view_func=admin)
bp.add_url_rule("/expense", view_func=add_expense)


def init_app(app):
    app.register_blueprint(bp)