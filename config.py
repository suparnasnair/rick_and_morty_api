"""
Flask configuration
"""

SECRET_KEY = 'rFsad!3dfs&df2$2###@@df'
# the below statement is added to suppress the deprecated warning
# issued by SQLAlchemy module
FLASK_ENV = 'production'
SQLALCHEMY_TRACK_MODIFICATIONS = False
