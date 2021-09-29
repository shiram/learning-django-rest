from quickstart.models import Snippet
from quickstart.serializers import SnippetSerializer
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
import io
from django.core.management.base import BaseCommand

class SnippetData:
    def __init__(self, data):
        self._code = data['code']
        self._title = data['title']

    # Add a snippet to the database
    def add_snippet(self):
        snippet = Snippet(title=self._title, code=self._code)
        snippet.save()
        print("Finished adding snippet.")
        return snippet

    # Serialize a snippet
    def serialize_snippet(self, snippet):
        serializer = SnippetSerializer(snippet)
        return serializer.data

    # Convert/render serialized data to json
    def json_seriliazed_data(self, data):
        content = JSONRenderer().render(data)
        return content

    # Deserialize a stream of json data to Snippet types
    def json_deserialize_data(self, data):
        stream = io.BytesIO(data)
        data = JSONParser().parse(stream)
        serializer = SnippetSerializer(data=data)
        if serializer.is_valid():
            print("The validated data.")
            print(serializer.validated_data)
            serializer.save()
            return serializer
        raise SystemError("Data is not valid")

    def querysetSerialized(self):
        serializer = SnippetSerializer(Snippet.objects.all(), many=True)
        return serializer.data

def display_results(data):
    snippet = SnippetData(data)
    snippet_data = snippet.add_snippet()

    print("The Snippet You Created")
    print(snippet_data)
    print("\n")

    snippet_serializer = snippet.serialize_snippet(snippet_data)
    print("The serialized data")
    print(snippet_serializer)
    print("\n")

    snippet_json_data = snippet.json_seriliazed_data(snippet_serializer)
    print("The json serialized data")
    print(snippet_json_data)
    print("\n")

    deserialize_json_snippet = snippet.json_deserialize_data(snippet_json_data)
    print("The deserialized data has been stored.")
    print(deserialize_json_snippet)
    print("\n")

class Command(BaseCommand):
    help = 'Takes a code snippet and adds it to the database, simulating its calls with serialization, and deserialization, then storing it again.'


    def add_arguments(self, parser):
        parser.add_argument('title', help='The title of the code snippet to add.')
        parser.add_argument('code', help='The code snippet to be added.')

    def handle(self, *args, **kwargs):
        print("The Arguments are: %s" % kwargs)
        display_results(kwargs)

