class Config:
    SQLALCHEMY_DATABASE_URI = "postgresql://postgres:admin@localhost/flask_contacts"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = "AHAH3493H392H3209U32HAKL983"
    
class Development(Config):
    Debug=True
    
class Testing(Config):
    pass


config = {
    "development": Development,
    "testing": Testing
}