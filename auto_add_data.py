from restdjangotutorials import settings
from quickstart.models import Snippet
from quickstart.serializers import SnippetSerializer
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
import io

class SnippetData:
    def __init__(self, data):
        if not data or 'code' not in data:
            raise SystemError("Please pass some snippet data, atleast the code.")
        self._code = data['code']

    # Add a snippet to the database
    def add_snippet(self):
        snippet = Snippet(code=self._code)
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


class Runner:

    def menu(self):
        print("Please enter a piece of code in any language: \n")

    def game_loop(self):
        while True:
            self.menu()
            code = input()
            if code == 'q':
                SystemExit("Thank you for playing")
            snippet = SnippetData({'code': code})
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

            print("************** Wanna Continue? Enter q/Q to exit, anything else goes ***************")
            input = input()
            if input == 'q' or input =='Q':
                SystemExit("Buh-bye")
            else:
                continue


if __name__ == '__main__':
    runner = Runner()
    runner.game_loop()








    
