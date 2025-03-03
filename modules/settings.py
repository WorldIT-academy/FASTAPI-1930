import fastapi, os
import fastapi.templating as templating
import fastapi.staticfiles as staticfiles
#
app = fastapi.FastAPI()

# Path directory for templates
PATH_TEMPLATES = os.path.abspath(os.path.join(__file__, '..', '..', 'templates'))
TEMPLATES = templating.Jinja2Templates(directory= PATH_TEMPLATES)
# Path directory for static files
PATH_STATIC = os.path.abspath(os.path.join(__file__, '..', '..', 'static'))
app.mount(
    path= '/static',
    app = staticfiles.StaticFiles(directory= PATH_STATIC),
    name= 'static'
)