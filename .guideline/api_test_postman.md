# Test API

[REF](https://dev.to/nobleobioma/build-a-crud-django-rest-api-46kc)

## Add Book

curl -X POST -H "Authorization: Token 1565c60a136420bc733b10c4a165e07698014acb" -d '{"title":"CRUD Django", "description":"Walkthrough for CRUD in DJANGO", "author": 1}' localhost:8000/api/addbook

## How to test with postman

[REF](https://dev.to/loopdelicious/using-jwt-to-authenticate-and-authorize-requests-in-postman-3a5h)

## Postman add test auto save token obtain

const response = pm.response.json()
pm.environment.set("jwt_token", response.access)

## Add Authorization in header of the request

Authorization> JWT {{jwt_token}}
