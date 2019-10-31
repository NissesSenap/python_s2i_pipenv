import responder
from marshmallow import Schema, fields

description = "This is a sample server for a pet store."
terms_of_service = "http://example.com/terms/"
contact = {
    "name": "API Support",
    "url": "http://www.example.com/support",
    "email": "support@example.com",
}
license = {
    "name": "Apache 2.0",
    "url": "https://www.apache.org/licenses/LICENSE-2.0.html",
}


api = responder.API(
    title="Web Service",
    version="1.0",
    openapi="3.0.2",
    docs_route="/docs",
    description=description,
    terms_of_service=terms_of_service,
    contact=contact,
    license=license,
)


@api.schema("Pet")
class PetSchema(Schema):
    name = fields.Str()


@api.route("/")
def route(req, resp):
    """A cute furry animal endpoint.
    ---
    get:
        description: Get a random pet
        responses:
            200:
                description: A pet to be returned
                content:
                    application/json:
                        schema:
                            $ref: '#/components/schemas/Pet'
    """
    resp.media = PetSchema().dump({"name": "little orange"})


if __name__ == "__main__":
    api.run(address="0.0.0.0", port=8080)
