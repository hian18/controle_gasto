from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from .models import Categoria,Despesa

admin=Admin(name='CG', template_mode='bootstrap3')


class EntradaView(ModelView):
    column_list=['categorias','valor','data','desc']
    column_filters=['categorias']
    

class CategoriaView(ModelView):
    form_excluded_columns=['despesas']

def configure_admin(app):
    admin.init_app(app)
    admin.add_view(CategoriaView(Categoria,app.db.session))
    admin.add_view(EntradaView(Despesa,app.db.session))