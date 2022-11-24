# Render HTML web pages

# import from django
from django.http import HttpResponse


def home_view(request):
    # Take in a request from django and return html as a response

    #get something from the database

    name = "shiv"
    H1_STRING = f"""
    <h1>Biking {name}</h1>
    """
    P_STRING = """
     <p>Eren Jaeger </p>
     """
    HTML_STRING= H1_STRING + P_STRING
    return HttpResponse(HTML_STRING)
