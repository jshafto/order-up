from flask_login import UserMixin
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash

db = SQLAlchemy()




class Employee(db.Model, UserMixin):
  __tablename__ = "employees"
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(100), nullable=False)
  employee_number = db.Column(db.Integer, nullable=False, unique=True)
  hashed_password = db.Column(db.String(100), nullable=False)

  @property
  def password(self):
    return self.hashed_password

  @password.setter
  def password(self, password):
    self.hashed_password = generate_password_hash(password)

  def check_password(self, password):
    return check_password_hash(self.password, password)

class Menu(db.Model):
  __tablename__ = "menus"
  id = db.Column(db.Integer, primary_key = True)
  name = db.Column(db.String(30), nullable=False)


class MenuItem(db.Model):
  __tablename__ = "menu_items"
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(50), nullable=False)
  price = db.Column(db.Float, nullable=False)
  menu_id = db.Column(db.Integer, db.ForeignKey("menus.id"), nullable=False)
  menu_type_id = db.Column(db.Integer, db.ForeignKey("menu_item_types.id"), nullable=False)

  menu = db.relationship("Menu")
  type = db.relationship("MenuItemType")

class MenuItemType(db.Model):
  __tablename__ = "menu_item_types"
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(20), nullable=False)


class Table(db.Model):
  __tablename__ = "tables"
  id = db.Column(db.Integer, primary_key=True)
  number = db.Column(db.Integer, nullable=False, unique=True)
  capacity = db.Column(db.Integer, nullable=False)


# order_details = db.Table(
#   "menu_item_orders",
#   db.Model.metadata,
#   db.Column("menu_item_id", db.Integer, db.ForeignKey("menu_items.id"), primary_key=True),
#   db.Column("order_id", db.Integer, db.ForeignKey("orders.id"), primary_key=True),
# )


class Order(db.Model):
  __tablename__ = "orders"
  id = db.Column(db.Integer, primary_key=True)
  employee_id = db.Column(db.Integer, db.ForeignKey("employees.id"), nullable=False)
  table_id = db.Column(db.Integer, db.ForeignKey("tables.id"), nullable=False)
  finished= db.Column(db.Boolean, nullable=False)

  table = db.relationship("Table")
  employee = db.relationship("Employee")

class OrderDetails(db.Model):
  __tablename__ = "order_details"
  id = db.Column(db.Integer, primary_key=True)
  order_id = db.Column(db.Integer, db.ForeignKey("orders.id"), nullable=False)
  menu_item_id = db.Column(db.Integer, db.ForeignKey("menu_items.id"), nullable=False)

  order = db.relationship("Order")
  menu_item = db.relationship("MenuItem")
