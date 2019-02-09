import json
from application import app
from application.models.frequenciaDAO import frequenciaDAO
from application.views.FrequenciaView import FrequenciaView, ListaView
from application.views.SocioView import SocioView
from application.views.UsuarioView import UsuarioView


frequencia_view = FrequenciaView.as_view('frequencia_view')

app.add_url_rule('/frequencia/', view_func=frequencia_view, methods=['GET', 'POST'])
app.add_url_rule('/frequencia/<int:id>', view_func=frequencia_view, methods=['GET','PUT'])


lista_view = ListaView.as_view('lista_view')

app.add_url_rule('/lista/', view_func=lista_view, methods=['GET','POST'])
app.add_url_rule('/lista/<int:id>', view_func=lista_view, methods=['GET','PUT'])


socio_view = SocioView.as_view('socio_view')

app.add_url_rule('/socio/', view_func=socio_view, methods=['GET'])
app.add_url_rule('/socio/<int:id>', view_func=socio_view, methods=['GET'])


usuario_view = UsuarioView.as_view('usuario_view')

app.add_url_rule('/usuario/', view_func=usuario_view, methods=['GET','POST'])
app.add_url_rule('/usuario/<int:id>', view_func=usuario_view, methods=['GET','PUT'])
